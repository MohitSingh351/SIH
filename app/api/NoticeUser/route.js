import { MongoClient } from "mongodb";
import { NextResponse } from "next/server";

export async function POST(request) {
    let body = await request.json()
    const uri = process.env.MONGO_URI
    const client = new MongoClient(uri)
    try {
        const Newdatabase = client.db('Users')
        const Newcollection = Newdatabase.collection('UserList')
        const finduser = await Newcollection.findOne({ "email": body.email })
        if (!finduser) {
            await Newcollection.insertOne(body)
            const CreateUser = Newdatabase.collection(body.nickname)
            await CreateUser.insertOne({"demo" : 1})
            return NextResponse.json({ "success": true })
        } else {
            return NextResponse.json({ "success": true })
        }
    }
    finally {
        await client.close()
    }
}