import React from 'react';

interface SummaryBubbleProps {
  name: string;
  content: string;
  backgroundColor?: string; // Add backgroundColor as an optional prop
}

// This is a general component which create dive given a specified colour, title and content
const SummaryBubble: React.FC<SummaryBubbleProps> = ({ name, content, backgroundColor }) => {
  return (
    <div className="mx-2 border rounded-[30px] h-[420px] transition-transform duration-300 transform hover:scale-105" style={{ backgroundColor: backgroundColor || '#fff' }}>
        <div className="my-5 text-lg text-center font-semibold">{name}</div>
        <div className="mt-2 text-sm">{content}</div>
    </div>
  );
};

export default SummaryBubble;