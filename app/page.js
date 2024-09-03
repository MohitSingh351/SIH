'use client'
import { useEffect } from "react";
import Link from "next/link";
import Button from "@/components/Button.js"
import InstructionCard from "@/components/InstructionCard.js";
import AOS from 'aos';
import 'aos/dist/aos.css';

export default function Home() {

  useEffect(() => {
    AOS.init();
  }, [])

  const OpenInstructionBox = () => {
    const InstructionBox = document.getElementsByClassName('instructionCard')[0]
    InstructionBox.classList.add("instructionCardVisible")
  }
  return (
    <main className="HomePage w-full flex items-center justify-evenly relative overflow-hidden">
      <InstructionCard />
      <div className="w-[58%] h-full flex flex-col items-center justify-center gap-8">
        <div className="flex flex-col items-center justify-center gap-4">
          <div data-aos="fade-right" data-aos-delay="300" className="flex flex-col justify-center gap-2 text-4xl font-bold">
            <span>
              <span className="text-sky-600">Crop Care :</span> <span>Check Your Plant's</span>
            </span>
            <span>
              health instantly and  easily
            </span>
          </div>
          <div data-aos="zoom-in-right" data-aos-delay="600" className="px-44 text-slate-700 text-lg">
            Easily identify plant diseases by uploading a photo of your plant's leaf, Get
            instant results, treatment options. and care tips to keep your plants thriving,
          </div>
        </div>
        <div className="flex items-center gap-6 w-[61%]">
          <div data-aos="fade-right" data-aos-delay="800" className="flex items-center gap-2 cursor-pointer Navbtn relative" onClick={OpenInstructionBox}>
            <span className="text-lg font-semibold">Instruction : How to ?</span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6">
              <path strokeLinecap="round" strokeLinejoin="round" d="M4.5 12h15m0 0l-6.75-6.75M19.5 12l-6.75 6.75"></path>
            </svg>
          </div>
          <Link href={"/UploadPhoto"} data-aos="fade-left" data-aos-delay="800" className="takeAsnapBtn">
            <span className="circle1"></span>
            <span className="circle2"></span>
            <span className="circle3"></span>
            <span className="circle4"></span>
            <span className="circle5"></span>
            <span className="text">Scan Plant</span>
          </Link>
        </div>
        <div className="-ml-96" data-aos="zoom-in-down" data-aos-delay="800">
          <Button />
        </div>
      </div>
      <div className="w-[40%] h-full flex items-center justify-center">
        <img data-aos="fade-left" data-aos-delay="300" src="image.jpg" alt="Not Found" className="h-[60%] rounded-lg" />
      </div>
    </main>
  );
}