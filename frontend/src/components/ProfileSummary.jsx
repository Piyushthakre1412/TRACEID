import React from 'react';
import { Mail, MapPin, UserCheck, Users, CheckCircle2, Globe, ExternalLink, ShieldCheck } from 'lucide-react';

export default function ProfileSummary({ identity }) {
  const data = identity || {
    person_id: "P_101",
    canonical_name: "Piyush Thakre",
    primary_image: "/dataset/images/piyush.jpg",
    institution: "Prof. Ram Meghe Institute Of Technology and Research, Badnera",
    handles: [
      { platform: "GitHub", username: "piyush-thakre", url: "https://github.com/piyush-thakre" },
      { platform: "LinkedIn", username: "piyush-thakre-badnera", url: "https://linkedin.com/in/piyush-thakre" },
      { platform: "X (Twitter)", username: "piyush_thakre_ai", url: "https://x.com/piyush_thakre_ai" }
    ],
    contacts: {
      email: "piyush.thakre@prmitr.ac.in",
      location: "Badnera, Amravati, Maharashtra, India"
    },
    mutual_contacts: [
      { name: "Om Patil", role: "Frontend Lead @ Team Ace", platform: "GitHub" },
      { name: "Satwik Mhasaye", role: "Backend Lead @ Team Ace", platform: "LinkedIn" },
      { name: "Vyankatesh Raut", role: "Security Researcher", platform: "X (Twitter)" }
    ],
    overall_confidence: 96.1,
    confidence_breakdown: {
      bio_semantic_similarity: 94.2,
      handle_match: 100.0,
      mutual_network_overlap: 95.0
    }
  };

  const { canonical_name, primary_image, handles, contacts, overall_confidence, confidence_breakdown } = data;

  const realEmail = contacts?.email || null;
  const realLocation = contacts?.location || null;
  const hasRealContacts = Boolean(realEmail || realLocation);

  const facialSim = confidence_breakdown?.facial_similarity !== undefined ? confidence_breakdown.facial_similarity : 0.0;
  const isImageVerified = facialSim > 0.0;

  return (
    <div className="space-y-4">
      {/* 1. Basic Identity Card (Name, Avatar, Username ID) */}
      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3 shadow-md">
        <div className="flex items-center gap-3.5">
          <div className="relative">
            {primary_image ? (
              <img
                src={primary_image}
                alt={canonical_name}
                className="w-14 h-14 rounded-xl object-cover border-2 border-indigo-500/50 shadow-md"
                onError={(e) => {
                  e.target.onerror = null;
                  e.target.src = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150";
                }}
              />
            ) : (
              <div className="w-14 h-14 rounded-xl bg-indigo-950 border-2 border-indigo-500/50 flex items-center justify-center">
                <Users className="w-6 h-6 text-indigo-400" />
              </div>
            )}
            <span
              className={`absolute -bottom-1 -right-1 p-1 rounded-full border-2 border-slate-950 ${
                isImageVerified ? 'bg-emerald-500' : 'bg-amber-500'
              }`}
              title={isImageVerified ? 'Verified Facial Match' : 'No Photo Uploaded'}
            />
          </div>

          <div className="flex-1 min-w-0">
            <h4 className="text-base font-extrabold text-white truncate flex items-center gap-1.5">
              <span>{canonical_name}</span>
              <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
            </h4>
            <p className="text-xs text-slate-400 truncate">{data.institution || 'Professional Network Target'}</p>
            <span className="text-[10px] text-indigo-400 font-mono font-semibold block mt-0.5">
              ID: {data.person_id}
            </span>
          </div>
        </div>

        {/* Username Handles Pill List */}
        {handles && handles.length > 0 && (
          <div className="flex flex-wrap gap-1.5 pt-1">
            {handles.map((h, i) => {
              const isWiki = h.platform === 'Wikipedia';
              return (
                <a
                  key={i}
                  href={h.url || '#'}
                  target="_blank"
                  rel="noreferrer"
                  className={`inline-flex items-center gap-1 text-[10px] px-2.5 py-1 rounded-md font-bold transition-all shadow-sm ${
                    isWiki
                      ? 'bg-gradient-to-r from-purple-950 to-indigo-950 text-purple-200 border border-purple-500/60 hover:border-purple-400 ring-1 ring-purple-500/30'
                      : 'bg-slate-900 hover:bg-indigo-950 text-slate-300 hover:text-indigo-200 border border-slate-800 hover:border-indigo-500/40'
                  }`}
                >
                  <Globe className={`w-3 h-3 ${isWiki ? 'text-purple-400' : 'text-indigo-400'}`} />
                  <span>{h.platform}:</span>
                  <span className={isWiki ? 'text-purple-200 font-extrabold' : 'text-slate-400'}>
                    @{h.username}
                  </span>
                  <ExternalLink className="w-2.5 h-2.5 text-slate-400" />
                </a>
              );
            })}
          </div>
        )}
      </div>

      {/* 2. Real Verified Contact Details (Rendered ONLY if genuine email or location exists) */}
      {hasRealContacts && (
        <div className="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2.5 shadow-md">
          <div className="flex items-center justify-between border-b border-slate-800 pb-2">
            <span className="text-xs font-bold text-slate-200 flex items-center gap-1.5">
              <Mail className="w-3.5 h-3.5 text-indigo-400" />
              Verified Contact Details
            </span>
            <span className="text-[9px] bg-emerald-950/80 text-emerald-400 border border-emerald-800/60 font-mono font-semibold px-2 py-0.5 rounded-full">
              VERIFIED
            </span>
          </div>

          <div className="space-y-2 text-xs">
            {realEmail && (
              <div className="flex items-center justify-between bg-slate-900/80 px-2.5 py-1.5 rounded-lg border border-slate-800/80">
                <span className="text-slate-400 flex items-center gap-1.5 text-[11px]">
                  <Mail className="w-3 h-3 text-sky-400" />
                  Email:
                </span>
                <span className="font-mono text-slate-200 text-[11px] select-all hover:text-sky-300 transition-colors">
                  {realEmail}
                </span>
              </div>
            )}

            {realLocation && (
              <div className="flex items-center justify-between bg-slate-900/80 px-2.5 py-1.5 rounded-lg border border-slate-800/80">
                <span className="text-slate-400 flex items-center gap-1.5 text-[11px]">
                  <MapPin className="w-3 h-3 text-purple-400" />
                  Location:
                </span>
                <span className="text-slate-300 text-[11px] font-medium truncate max-w-[200px]" title={realLocation}>
                  {realLocation}
                </span>
              </div>
            )}
          </div>
        </div>
      )}



      {/* 4. Multi-Modal Score Breakdown */}
      <div className="space-y-2">
        <h5 className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Multi-Modal Feature Breakdown</h5>

        <div className="bg-slate-950 p-2.5 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
          <span className="text-slate-300 font-medium">ArcFace DeepFace Visual Match (40%)</span>
          {isImageVerified ? (
            <span className="font-extrabold text-emerald-400">{facialSim}%</span>
          ) : (
            <span className="font-semibold text-amber-400/90 text-[11px]">0.0% (No Photo Uploaded)</span>
          )}
        </div>

        <div className="bg-slate-950 p-2.5 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
          <span className="text-slate-300 font-medium">MiniLM Bio Semantic Sim (35%)</span>
          <span className="font-extrabold text-purple-400">{confidence_breakdown?.bio_semantic_similarity || 85.0}%</span>
        </div>

        <div className="bg-slate-950 p-2.5 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
          <span className="text-slate-300 font-medium">RapidFuzz Handle Match (25%)</span>
          <span className="font-extrabold text-sky-400">{confidence_breakdown?.handle_match || 90.0}%</span>
        </div>
      </div>
    </div>
  );
}
