import React from 'react'

const InstructionCard = () => {
    const CloseInstructionBox = () => {
        const InstructionBox = document.getElementsByClassName('instructionCard')[0]
        InstructionBox.classList.remove("instructionCardVisible")
    }
    return (
        <div className="instructionCard absolute top-0 left-0 bg-white border-2 border-black rounded-xl h-[70%] w-[50%] z-10 overflow-scroll">
            <span className="flex items-center justify-between w-full px-4 py-2">
                <h1 className="text-2xl font-semibold sticky top-2 text-sky-600">Instructions</h1>
                <img src="cross.gif" alt="Not Found" className="h-8 w-8 cursor-pointer" onClick={CloseInstructionBox} />
            </span>
        </div>
    )
}

export default InstructionCard