'use client'
import { useUser } from '@auth0/nextjs-auth0/client';
import { useEffect } from "react";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import AOS from 'aos';
import 'aos/dist/aos.css';

const Navbar = () => {
    const { user, error, isLoading } = useUser();
    const router = useRouter()
    const pathname = usePathname()
    const NoticeUser = async () => {
        const res = await fetch('/api/NoticeUser', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(user),
        })
        let response = await res.json()
    }

    if (user) {
        NoticeUser()
    }

    useEffect(() => {
        AOS.init();

        let addScript = document.createElement('script')
        addScript.setAttribute('src', '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit')
        document.body.appendChild(addScript)
        window.googleTranslateElementInit = googleTranslateElementInit
    }, [])

    const googleTranslateElementInit = () => {
        new google.translate.TranslateElement({
            pageLanguage: 'en',
        }, 'google_translate_element');
    }

    const ConfirmLogOut = () => {
        let input = confirm("Do you really want to LogOut ?");
        if (input) {
            router.push("/api/auth/logout")
        } else {
            return false
        }
    }
    return (
        <nav data-aos="fade-down" className="w-full h-16 flex justify-evenly items-center sticky top-0 bg-white">
            <Link href={"/"} className="logo flex items-center gap-2 cursor-pointer">
                <img className="w-10 h-10" src="logo.png" alt="Not Available" />
                <span className="text-xl font-bold">CropCare</span>
            </Link>
            <span className="btns flex items-center gap-4 h-full">
                <Link href="/" className={`${pathname === "/" ? "font-semibold underline underline-offset-4 text-sky-600" : ""} text-lg transition-all relative Navbtn h-[40%] w-14 flex flex-col items-center justify-center`}>Home</Link>
                <Link href="/UploadPhoto" className={`${pathname === "/UploadPhoto" ? 'font-semibold underline underline-offset-4 text-sky-600' : ""} text-lg transition-all Navbtn relative h-[40%] w-32 flex flex-col items-center justify-center`}>Upload Photo</Link>
                <Link href="/DignosisHistory" className={`${pathname === "/DignosisHistory" ? 'font-semibold underline underline-offset-4 text-sky-600' : ""} text-lg transition-all Navbtn relative h-[40%] w-36 flex flex-col items-center justify-center`}>Dignosis History</Link>
                <Link href="/AboutUs" className={`${pathname === "/AboutUs" ? 'font-semibold underline underline-offset-4 text-sky-600' : ""} text-lg transition-all Navbtn relative h-[40%] w-20 flex flex-col items-center justify-center`}>About Us</Link>
            </span>
            {!user && <a href="/api/auth/login" className="login flex items-center gap-2 rounded-full border-2 border-sky-600 px-4 cursor-pointer transition-all hover:bg-sky-600 hover:text-white">
                <span className="text-lg">Login</span>
                <img src="Login-Avatar.gif" alt="Not Found" className="h-8 w-8" />
            </a>
            }
            {user && <div onClick={ConfirmLogOut} className='flex items-center gap-1 px-2 py-1 border border-sky-600 rounded-full cursor-pointer'>
                <img src={user.picture} alt="Not Found" className='h-8 w-8 rounded-full' />
                <span>{user.name}</span>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ff0020" fill="none">
                    <path d="M15 17.625C14.9264 19.4769 13.3831 21.0494 11.3156 20.9988C10.8346 20.987 10.2401 20.8194 9.05112 20.484C6.18961 19.6768 3.70555 18.3203 3.10956 15.2815C3 14.723 3 14.0944 3 12.8373L3 11.1627C3 9.90561 3 9.27705 3.10956 8.71846C3.70555 5.67965 6.18961 4.32316 9.05112 3.51603C10.2401 3.18064 10.8346 3.01295 11.3156 3.00119C13.3831 2.95061 14.9264 4.52307 15 6.37501" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
                    <path d="M21 12H10M21 12C21 11.2998 19.0057 9.99153 18.5 9.5M21 12C21 12.7002 19.0057 14.0085 18.5 14.5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
            </div>
            }
            <div id='google_translate_element' className='w-fit'></div>
        </nav>
    )
}

export default Navbar