'use client'
import { useState, useEffect } from "react"
import AOS from 'aos';
import 'aos/dist/aos.css';

const page = () => {

  useEffect(() => {
    AOS.init();
  }, [])

  const [img, setImg] = useState("logo.png")

  function convertToBase64(file) {
    return new Promise((resolve, reject) => {
      const fileReader = new FileReader()
      fileReader.readAsDataURL(file);
      fileReader.onload = () => {
        resolve(fileReader.result)
      }
      fileReader.onerror = (error) => {
        reject(error)
      }
    })
  }

  const ChangeImg = async (e) => {
    const file = e.target.files[0]
    const base64 = await convertToBase64(file)
    setImg(base64)
  }
  return (
    <main className="flex flex-col items-center justify-evenly upmain">
      <div data-aos="fade-right" data-aos-delay="300" className="flex flex-col w-[50%] gap-3 px-4">
        <span className="font-semibold text-xl">How to Take a Clear Photo</span>
        <div>
          <div>Ensure the plant is well-lit with natural light.</div>
          <div>Keep the camera steady to avoid blurring.</div>
          <div>Focus on the plant , especially affected areas.</div>
          <div>Avoid background distractions.</div>
        </div>
      </div>
      <div data-aos-delay="500" data-aos="flip-down" className="flex flex-col items-center justify-evenly w-[50%] h-[60%] bg-blue-200 rounded-3xl">
        <img data-aos-delay="650" data-aos="zoom-out" src={img} alt="Not Found" className="h-[70%] rounded-2xl aspect-square" />
        <div className="flex items-center justify-evenly w-[98%]">
          {/* <div className="w-[45%] py-2 rounded-full flex items-center justify-center bg-purple-800 text-white cursor-pointer gap-2 transition-all hover:bg-purple-900">
            <img src="camera.gif" alt="Not Available" className="h-8" />
            <span>Click Photo</span>
          </div> */}
          <label data-aos-delay="800" data-aos="fade-right" htmlFor="file-upload" className="w-[45%] py-2 rounded-full flex items-center justify-center bg-purple-800 text-white cursor-pointer gap-2 transition-all hover:bg-purple-900">
            <img src="upload.gif" alt="Not Available" className="h-8" />
            <span>Upload Image</span>
          </label>
          <input id="file-upload" type="file" className="hidden" onChange={(e) => { ChangeImg(e) }} />
          <div data-aos-delay="800" data-aos="fade-left" className="w-[45%] py-2 bg-sky-600 flex items-center justify-center gap-2 text-white rounded-full cursor-pointer hover:bg-sky-700 transition-all">
            <img src="analyse.gif" alt="Not Found" className="h-8" />
            <span>Analyze Image</span>
          </div>
        </div>
      </div>
      <div className="italic">
        <span className="text-red-600">Note</span> : To change the uploaded image , just re-upload photo by clicking on upload image button
      </div>
    </main>
  )
}

export default page
