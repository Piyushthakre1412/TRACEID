import React from 'react';
import { Calendar, Award, GraduationCap, Code } from 'lucide-react';

export default function ActivityTimeline({ timeline }) {
  const events = timeline || [
    { year: "2023", event: "Enrolled at PRMITR Badnera", category: "education" },
    { year: "2026", event: "Project ACE Created for Hack Synthesis 3.0", category: "hackathon" }
  ];

  const getCategoryIcon = (cat) => {
    switch (cat) {
      case 'education': return <GraduationCap className="w-4 h-4 text-sky-400" />;
      case 'hackathon': return <Award className="w-4 h-4 text-amber-400" />;
      default: return <Code className="w-4 h-4 text-indigo-400" />;
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-2xl h-full flex flex-col">
      <h3 className="text-lg font-bold text-white flex items-center gap-2 mb-4">
        <Calendar className="w-5 h-5 text-sky-400" />
        Activity Timeline
      </h3>

      <div className="flex-1 space-y-4 overflow-y-auto pr-2">
        {events.map((item, idx) => (
          <div key={idx} className="flex gap-4 items-start relative pl-4 border-l border-slate-800">
            <div className="absolute -left-2 top-0.5 w-3.5 h-3.5 rounded-full bg-slate-950 border border-indigo-500 flex items-center justify-center" />
            <div className="bg-slate-950 border border-slate-800 p-3 rounded-lg flex-1">
              <div className="flex items-center justify-between mb-1">
                <span className="text-xs font-bold text-indigo-400">{item.year}</span>
                <span className="p-1 rounded bg-slate-900">{getCategoryIcon(item.category)}</span>
              </div>
              <p className="text-xs text-slate-300 font-medium">{item.event}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
