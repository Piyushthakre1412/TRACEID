import json
import os

def generate_50_user_dataset():
    # 1. Base Core Team Persona Records (P_101 to P_104)
    team = [
        {
            "person_id": "P_101",
            "canonical_name": "Piyush Thakre",
            "primary_image": "/dataset/images/piyush.jpg",
            "institution": "Prof. Ram Meghe Institute Of Technology and Research, Badnera",
            "roles": ["Team Lead", "AI Developer", "Full Stack Engineer"],
            "handles": [
                { "platform": "GitHub", "username": "piyush-thakre", "url": "https://github.com/piyush-thakre", "status": "VERIFIED" },
                { "platform": "LinkedIn", "username": "piyush-thakre-badnera", "url": "https://linkedin.com/in/piyush-thakre-badnera", "status": "VERIFIED" },
                { "platform": "Instagram", "username": "piyush_thakre_official", "url": "https://instagram.com/piyush_thakre_official", "status": "VERIFIED" },
                { "platform": "X (Twitter)", "username": "piyush_thakre_ai", "url": "https://x.com/piyush_thakre_ai", "status": "VERIFIED" }
            ],
            "platform_existence_matrix": {
                "GitHub": { "status": "VERIFIED", "username": "piyush-thakre", "url": "https://github.com/piyush-thakre", "confidence": 100.0 },
                "LinkedIn": { "status": "VERIFIED", "username": "piyush-thakre-badnera", "url": "https://linkedin.com/in/piyush-thakre-badnera", "confidence": 98.0 },
                "Instagram": { "status": "VERIFIED", "username": "piyush_thakre_official", "url": "https://instagram.com/piyush_thakre_official", "confidence": 94.0 },
                "X_Twitter": { "status": "VERIFIED", "username": "piyush_thakre_ai", "url": "https://x.com/piyush_thakre_ai", "confidence": 95.0 }
            },
            "bios": [
                "AI & ML enthusiast | Engineering student at PRMITR Badnera | Team Lead @ Team Ace",
                "Building multi-modal digital footprint intelligence & OSINT graph systems."
            ],
            "contacts": {
                "email": "piyush.thakre@prmitr.ac.in",
                "phone": "+91 98230 11024",
                "location": "Badnera, Amravati, Maharashtra, India"
            },
            "mutual_contacts": [
                { "name": "Om Patil", "role": "Frontend Lead @ Team Ace", "platform": "GitHub" },
                { "name": "Satwik Mhasaye", "role": "Backend Lead @ Team Ace", "platform": "LinkedIn" },
                { "name": "Vyankatesh Raut", "role": "Security Researcher", "platform": "X (Twitter)" }
            ],
            "projects": ["ACE / InterceptAI", "Digital Identity Resolution System"],
            "timeline": [
                {
                    "date": "Sep 2026",
                    "year": "2026",
                    "event": "Published LinkedIn Article: Multi-Modal OSINT Disambiguation Architecture",
                    "content": "Excited to present our paper on integrating ArcFace visual embeddings with sentence-transformers for real-time identity resolution across sparse networks.",
                    "category": "post",
                    "platform": "LinkedIn",
                    "engagement": { "likes": 245, "comments": 48, "shares": 19 },
                    "url": "https://linkedin.com/in/piyush-thakre-badnera"
                },
                {
                    "date": "Aug 2026",
                    "year": "2026",
                    "event": "Released TRACEID Core Engine v2.4",
                    "content": "Pushed release v2.4 containing NetworkX graph engine and ChromaDB vector search pipeline.",
                    "category": "project",
                    "platform": "GitHub",
                    "engagement": { "stars": 312, "forks": 58 },
                    "url": "https://github.com/piyush-thakre"
                },
                {
                    "date": "Jun 2026",
                    "year": "2026",
                    "event": "1st Rank Winner @ Neurax National AI Hackathon",
                    "content": "Won Grand Champion title for building real-time OSINT identity resolution & disambiguation graph platform.",
                    "category": "hackathon",
                    "platform": "Award",
                    "engagement": { "likes": 420, "comments": 85 }
                },
                {
                    "date": "Jan 2025",
                    "year": "2025",
                    "event": "Published Paper: Homoglyph Normalization in Graph Networks",
                    "content": "Paper accepted in International Journal of Cyber Intelligence & Machine Learning.",
                    "category": "research",
                    "platform": "Publication",
                    "engagement": { "citations": 24 }
                },
                {
                    "date": "Aug 2023",
                    "year": "2023",
                    "event": "Enrolled in B.Tech Computer Science & AI @ PRMITR Badnera",
                    "content": "Began undergraduate degree specializing in Artificial Intelligence, Machine Learning, and Multi-Modal Systems.",
                    "category": "career",
                    "platform": "Education"
                }
            ],
            "evidence_trail": [
                { "node_id": "H_01", "source_url": "https://github.com/piyush-thakre", "verified_at": "2026-09-19", "proof_type": "Direct Bi-Directional URL Match" },
                { "node_id": "ORG_01", "source_url": "https://mitra.ac.in", "verified_at": "2026-09-19", "proof_type": "Verified Institutional Directory Record" }
            ]
        },
        {
            "person_id": "P_102",
            "canonical_name": "Om Patil",
            "primary_image": "/dataset/images/om.jpg",
            "institution": "Prof. Ram Meghe Institute Of Technology and Research, Badnera",
            "roles": ["Frontend Engineer", "UI/UX Specialist"],
            "handles": [
                { "platform": "GitHub", "username": "om-patil", "url": "https://github.com/om-patil", "status": "VERIFIED" },
                { "platform": "LinkedIn", "username": "om-patil-ui", "url": "https://linkedin.com/in/om-patil-ui", "status": "VERIFIED" }
            ],
            "platform_existence_matrix": {
                "GitHub": { "status": "VERIFIED", "username": "om-patil", "url": "https://github.com/om-patil", "confidence": 100.0 },
                "LinkedIn": { "status": "VERIFIED", "username": "om-patil-ui", "url": "https://linkedin.com/in/om-patil-ui", "confidence": 96.0 },
                "Instagram": { "status": "NOT_FOUND", "username": None, "url": None, "confidence": 0.0 },
                "X_Twitter": { "status": "NOT_FOUND", "username": None, "url": None, "confidence": 0.0 }
            },
            "bios": [
                "Frontend architect | React & Data Visualization expert | PRMITR Badnera"
            ],
            "contacts": {
                "email": "om.patil@prmitr.ac.in",
                "phone": "+91 98230 11025",
                "location": "Badnera, Amravati, Maharashtra, India"
            },
            "mutual_contacts": [
                { "name": "Piyush Thakre", "role": "Team Lead @ Team Ace", "platform": "GitHub" },
                { "name": "Satwik Mhasaye", "role": "Backend Lead @ Team Ace", "platform": "LinkedIn" }
            ],
            "projects": ["ACE / InterceptAI"],
            "timeline": [
                {
                    "date": "Sep 2026",
                    "year": "2026",
                    "event": "Published Design Post: Dark Mode Glassmorphism Systems for OSINT Dashboard",
                    "content": "Designing real-time interactive canvas widgets for graph node inspection and candidate evidence trails.",
                    "category": "post",
                    "platform": "LinkedIn",
                    "engagement": { "likes": 195, "comments": 24 },
                    "url": "https://linkedin.com/in/om-patil-ui"
                },
                {
                    "date": "Jul 2026",
                    "year": "2026",
                    "event": "Open Source Component Release: React Knowledge Graph Canvas",
                    "content": "Released custom HTML5 Canvas interactive graph renderer for large identity node networks.",
                    "category": "project",
                    "platform": "GitHub",
                    "engagement": { "stars": 182, "forks": 29 },
                    "url": "https://github.com/om-patil"
                },
                {
                    "date": "Jun 2026",
                    "year": "2026",
                    "event": "1st Rank Winner @ Neurax National AI Hackathon",
                    "content": "Co-built TRACEID frontend UI & interactive candidate summary inspector.",
                    "category": "hackathon",
                    "platform": "Award",
                    "engagement": { "likes": 280, "comments": 42 }
                },
                {
                    "date": "Aug 2023",
                    "year": "2023",
                    "event": "Enrolled in B.Tech CSE @ PRMITR Badnera",
                    "content": "Specializing in Computer Science Engineering and Modern Web Interface Systems.",
                    "category": "career",
                    "platform": "Education"
                }
            ],
            "evidence_trail": [
                { "node_id": "H_02", "source_url": "https://github.com/om-patil", "verified_at": "2026-09-19", "proof_type": "GitHub Profile Confirmation" }
            ]
        },
        {
            "person_id": "P_103",
            "canonical_name": "Satwik Mhasaye",
            "primary_image": "/dataset/images/satwik.jpg",
            "institution": "Prof. Ram Meghe Institute Of Technology and Research, Badnera",
            "roles": ["Data Engineer", "Backend Developer"],
            "handles": [
                { "platform": "GitHub", "username": "satwik-mhasaye", "url": "https://github.com/satwik-mhasaye", "status": "VERIFIED" },
                { "platform": "LinkedIn", "username": "7wik-mhasaye", "url": "https://linkedin.com/in/7wik-mhasaye", "status": "ALIAS_MATCHED" },
                { "platform": "Instagram", "username": "satwik_mhasaye", "url": "https://instagram.com/satwik_mhasaye", "status": "VERIFIED" }
            ],
            "platform_existence_matrix": {
                "GitHub": { "status": "VERIFIED", "username": "satwik-mhasaye", "url": "https://github.com/satwik-mhasaye", "confidence": 100.0 },
                "LinkedIn": { "status": "ALIAS_MATCHED", "username": "7wik-mhasaye", "url": "https://linkedin.com/in/7wik-mhasaye", "confidence": 92.4, "reason": "Leetspeak Normalized Handle Match ('7wik' -> 'satwik') + Face Embedding Match (0.94)" },
                "Instagram": { "status": "VERIFIED", "username": "satwik_mhasaye", "url": "https://instagram.com/satwik_mhasaye", "confidence": 96.5, "reason": "Bio URL Citation + Face Embedding Match (0.95)" },
                "X_Twitter": { "status": "NOT_FOUND", "username": None, "url": None, "confidence": 0.0, "reason": "No public account in dataset" }
            },
            "bios": [
                "Backend & Graph Database engineer | NetworkX & FastAPI lover | PRMITR Badnera"
            ],
            "contacts": {
                "email": "satwik.mhasaye@prmitr.ac.in",
                "phone": "+91 98230 11026",
                "location": "Badnera, Amravati, Maharashtra, India"
            },
            "mutual_contacts": [
                { "name": "Piyush Thakre", "role": "Team Lead @ Team Ace", "platform": "GitHub" },
                { "name": "Om Patil", "role": "Frontend Lead @ Team Ace", "platform": "GitHub" }
            ],
            "projects": ["ACE / InterceptAI"],
            "timeline": [
                {
                    "date": "Sep 2026",
                    "year": "2026",
                    "event": "Published Post: Optimizing NetworkX Subgraph Queries for Disambiguation",
                    "content": "Explaining how we structure SQLite candidate metadata with ChromaDB vector indices for sub-second identity lookup.",
                    "category": "post",
                    "platform": "LinkedIn",
                    "engagement": { "likes": 210, "comments": 38 },
                    "url": "https://linkedin.com/in/7wik-mhasaye"
                },
                {
                    "date": "Aug 2026",
                    "year": "2026",
                    "event": "Released OSINT Web Crawler & Leetspeak Handle Normalizer",
                    "content": "Pushed Python module supporting automatic homoglyph normalization (7->s, 4->a, 3->e) across public profile endpoints.",
                    "category": "project",
                    "platform": "GitHub",
                    "engagement": { "stars": 165, "forks": 22 },
                    "url": "https://github.com/satwik-mhasaye"
                },
                {
                    "date": "Jun 2026",
                    "year": "2026",
                    "event": "1st Rank Winner @ Neurax National AI Hackathon",
                    "content": "Built high-performance FastAPI & NetworkX graph engine.",
                    "category": "hackathon",
                    "platform": "Award",
                    "engagement": { "likes": 305, "comments": 50 }
                },
                {
                    "date": "Aug 2023",
                    "year": "2023",
                    "event": "Enrolled in B.Tech CSE @ PRMITR Badnera",
                    "content": "Focusing on Data Engineering, Distributed Systems, and Graph Databases.",
                    "category": "career",
                    "platform": "Education"
                }
            ],
            "evidence_trail": [
                { "node_id": "H_03", "source_url": "https://github.com/satwik-mhasaye", "verified_at": "2026-09-19", "proof_type": "Verified NetworkX Pipeline Commits" },
                { "node_id": "H_03_LI", "source_url": "https://linkedin.com/in/7wik-mhasaye", "verified_at": "2026-09-19", "proof_type": "Leetspeak & Multi-Modal Visual Anchor Match" }
            ]
        },
        {
            "person_id": "P_104",
            "canonical_name": "Vyankatesh Raut",
            "primary_image": "/dataset/images/vyankatesh.jpg",
            "institution": "Prof. Ram Meghe Institute Of Technology and Research, Badnera",
            "roles": ["Security Researcher", "OSINT Analyst"],
            "handles": [
                { "platform": "GitHub", "username": "vyankatesh-raut", "url": "https://github.com/vyankatesh-raut", "status": "VERIFIED" },
                { "platform": "X (Twitter)", "username": "v_raut_osint", "url": "https://x.com/v_raut_osint", "status": "VERIFIED" }
            ],
            "platform_existence_matrix": {
                "GitHub": { "status": "VERIFIED", "username": "vyankatesh-raut", "url": "https://github.com/vyankatesh-raut", "confidence": 100.0 },
                "LinkedIn": { "status": "NOT_FOUND", "username": None, "url": None, "confidence": 0.0 },
                "Instagram": { "status": "NOT_FOUND", "username": None, "url": None, "confidence": 0.0 },
                "X_Twitter": { "status": "VERIFIED", "username": "v_raut_osint", "url": "https://x.com/v_raut_osint", "confidence": 95.0 }
            },
            "bios": [
                "Cybersecurity researcher & OSINT Analyst | PRMITR Badnera"
            ],
            "contacts": {
                "email": "vyankatesh.raut@prmitr.ac.in",
                "phone": "+91 98230 11027",
                "location": "Badnera, Amravati, Maharashtra, India"
            },
            "mutual_contacts": [
                { "name": "Piyush Thakre", "role": "Team Lead @ Team Ace", "platform": "GitHub" },
                { "name": "Satwik Mhasaye", "role": "Backend Lead @ Team Ace", "platform": "LinkedIn" }
            ],
            "projects": ["ACE / InterceptAI", "OSINT Recon Toolkit"],
            "timeline": [
                {
                    "date": "Sep 2026",
                    "year": "2026",
                    "event": "Published Security Advisory: Cross-Platform Footprint Audit",
                    "content": "Shared guidelines on identifying synthetic profile impersonation using graph centrality and homoglyph resolution.",
                    "category": "post",
                    "platform": "X (Twitter)",
                    "engagement": { "likes": 160, "comments": 22 },
                    "url": "https://x.com/v_raut_osint"
                },
                {
                    "date": "Aug 2026",
                    "year": "2026",
                    "event": "Released OSINT Audit Automation Tools",
                    "content": "Pushed automated verification audit rules for evaluating identity confidence thresholds.",
                    "category": "project",
                    "platform": "GitHub",
                    "engagement": { "stars": 140, "forks": 18 },
                    "url": "https://github.com/vyankatesh-raut"
                },
                {
                    "date": "Aug 2023",
                    "year": "2023",
                    "event": "Enrolled in B.Tech CSE @ PRMITR Badnera",
                    "content": "Specializing in Cybersecurity, Network Defense, and Threat Intelligence.",
                    "category": "career",
                    "platform": "Education"
                }
            ],
            "evidence_trail": [
                { "node_id": "H_04", "source_url": "https://github.com/vyankatesh-raut", "verified_at": "2026-09-19", "proof_type": "Verified Security Audit Log" }
            ]
        }
    ]

    # 2. Synthetic Diverse Names (P_105 to P_150 -> Total 50 Candidates)
    names_pool = [
        ("Aarav Sharma", "IIT Bombay", "AI Researcher", "aarav_sharma", "aarav-sharma-iitb", "aarav_ai", None),
        ("Aarav Sharma", "BITS Pilani", "Cloud Architect", "aarav_sharma_bits", "aarav-sharma-cloud", None, None), # Name Collision
        ("John Smith", "Stanford Security Lab", "Security Engineer", "jsmith-sec", "john-smith-stanford", None, "jsmith_sec"), # Name Collision
        ("John Smith", "MIT Media Lab", "UX Designer", "jsmith-design", "john-smith-ux", "jsmith_creative", None), # Name Collision
        ("Ananya Verma", "IIIT Hyderabad", "Computer Vision Dev", "4n4ny4_verma", "ananya-verma-cv", "ananya_vision", "ananya_cv"),
        ("Rohan Gupta", "Delhi Technological University", "Blockchain Developer", "r0h4n_gupt4", "rohan-gupta-dtu", None, "rohan_chain"),
        ("Neha Kulkarni", "COEP Pune", "DevOps Engineer", "neha_kulkarni", "neha-kulkarni-coep", None, None),
        ("Siddharth Deshmukh", "VNIT Nagpur", "Full Stack Developer", "siddharth_d", "siddharth-deshmukh-vnit", "sid_deshmukh", "sid_d_dev"),
        ("Aditya Joshi", "VJTI Mumbai", "Machine Learning Eng", "4d1ty4_j0sh1", "aditya-joshi-vjti", "aditya_ml", None),
        ("Priya Patel", "Gujarat Technological University", "Data Scientist", "priya_patel_ds", "priya-patel-ds", "priya_data", "priya_patel_ai"),
        ("Karan Mehta", "NMIMS Mumbai", "Product Manager", "karan_mehta", "karan-mehta-pm", "karan_m_official", "karan_mehta_pm"),
        ("Tanvi Rao", "PES University Bangalore", "Mobile App Dev", "tanvi_rao", "tanvi-rao-flutter", "tanvi_creates", None),
        ("Vikram Singh", "IIT Delhi", "Quantum Computing", "v1kr4m_s1ngh", "vikram-singh-quantum", None, "vikram_q"),
        ("Meera Nair", "NIT Calicut", "NLP Researcher", "meera_nair_nlp", "meera-nair-nitc", "meera_nair", None),
        ("Devansh Saxena", "IIT Roorkee", "Cybersecurity Analyst", "d3v4nsh_sec", "devansh-saxena-iitr", None, "devansh_sec"),
        ("Ishita Bhasin", "NSUT Delhi", "Frontend Engineer", "ishita_bhasin", "ishita-bhasin-nsut", "ishita_ui", "ishita_dev"),
        ("Yash Agarwal", "Manipal Institute of Tech", "Game Developer", "yash_agarwal_dev", "yash-agarwal-mit", "yash_games", None),
        ("Sneha Reddiyar", "Anna University", "Embedded Systems", "sneha_r", "sneha-reddiyar-anna", None, None),
        ("Harshvardhan Shinde", "PICT Pune", "Backend Architect", "h4rsh_sh1nd3", "harsh-shinde-pict", "harsh_backend", "harsh_shinde_tech"),
        ("Kavya Nambiar", "IIT Madras", "Robotics Engineer", "kavya_nambiar", "kavya-nambiar-iitm", "kavya_robotics", None),
        ("Ritik Chouhan", "IIT Kharagpur", "System Architect", "ritik_chouhan", "ritik-chouhan-iitkgp", None, "ritik_arch"),
        ("Shreya Bose", "Jadavpur University", "Bioinformatics Dev", "shreya_bose", "shreya-bose-ju", "shreya_bio", None),
        ("Manish Kumar", "NIT Trichy", "Database Admin", "m4n1sh_k", "manish-kumar-nitt", None, "manish_db"),
        ("Kirti Pandharipande", "PRMITR Badnera", "AI Systems Specialist", "kirti_p", "kirti-pandharipande", "kirti_p_ai", None),
        ("Amanpreet Singh", "Thapar University", "Site Reliability Eng", "aman_singh_sre", "amanpreet-singh-thapar", None, "aman_sre"),
        ("Divya Sundaram", "SSN College of Eng", "Cloud Native Dev", "divya_s", "divya-sundaram-ssn", "divya_cloud", None),
        ("Gaurav Bansal", "PEC Chandigarh", "Fintech Engineer", "g4ur4v_b4ns4l", "gaurav-bansal-pec", None, "gaurav_fintech"),
        ("Nikita Chaudhari", "PRMITR Badnera", "Data Visualization", "nikita_c", "nikita-chaudhari-badnera", "nikita_vis", None),
        ("Rishabh Tiwari", "MNNIT Allahabad", "Distributed Systems", "rishabh_t", "rishabh-tiwari-mnnit", None, "rishabh_dist"),
        ("Pooja Hegde", "RVCE Bangalore", "Autonomous Vehicles", "pooja_hegde_av", "pooja-hegde-rvce", "pooja_av", None),
        ("Varun Kulkarni", "WCE Sangli", "Compiler Engineer", "v4run_k", "varun-kulkarni-wce", None, "varun_comp"),
        ("Anushree Pillai", "Amrita University", "NLP & LLM Specialist", "anushree_p", "anushree-pillai-amrita", "anushree_llm", None),
        ("Pranav Gore", "PRMITR Badnera", "Mobile Developer", "pranav_gore", "pranav-gore-badnera", "pranav_apps", None),
        ("Radhika Mahajan", "VNIT Nagpur", "Edge AI Researcher", "r4dh1k4_m", "radhika-mahajan-vnit", "radhika_edge", "radhika_ai"),
        ("Kartik Shenoy", "IIT Guwahati", "High Performance Computing", "kartik_shenoy", "kartik-shenoy-iitg", None, "kartik_hpc"),
        ("Bhavna Mishra", "BHU Varanasi", "Signal Processing", "bhavna_m", "bhavna-mishra-bhu", "bhavna_dsp", None),
        ("Tushar Deshpande", "COEP Pune", "Linux Kernel Dev", "tushar_d", "tushar-deshpande-coep", None, "tushar_kernel"),
        ("Sayali Wankhede", "PRMITR Badnera", "Full Stack Developer", "sayali_w", "sayali-wankhede-badnera", "sayali_web", None),
        ("Sameer Kazi", "VJTI Mumbai", "DevSecOps Specialist", "s4m33r_k4z1", "sameer-kazi-vjti", "sameer_sec", "sameer_kazi_dev"),
        ("Nisha Agarwal", "IGDTUW Delhi", "AI Ethics Researcher", "nisha_agarwal", "nisha-agarwal-igdtuw", "nisha_ethics", None),
        ("Abhinav Iyer", "NITT Trichy", "VLSI Hardware Design", "abhinav_iyer", "abhinav-iyer-nitt", None, "abhinav_vlsi"),
        ("Srishti Saxena", "BITS Hyderabad", "Microservices Engineer", "srishti_s", "srishti-saxena-bits", "srishti_micro", None),
        ("Chaitanya Bapat", "PICT Pune", "Search Engine Architect", "chaitanya_b", "chaitanya-bapat-pict", None, "chaitanya_search"),
        ("Deepika Sundar", "IIT Hyderabad", "Deep Learning Eng", "d33p1k4_s", "deepika-sundar-iith", "deepika_dl", None),
        ("Utkarsh Tripathi", "IIIT Allahabad", "Algorithmic Trader", "utkarsh_t", "utkarsh-tripathi-iiita", None, "utkarsh_algo"),
        ("Mitali Rane", "VJTI Mumbai", "Graph Neural Networks", "mitali_rane", "mitali-rane-vjti", "mitali_gnn", None)
    ]

    raw_gh = []
    raw_li = []
    raw_ig = []
    raw_tw = []

    for i, item in enumerate(names_pool):
        p_id = f"P_{105 + i}"
        name, inst, role, gh_u, li_u, ig_u, tw_u = item

        handles_arr = []
        matrix = {}

        if gh_u:
            gh_url = f"https://github.com/{gh_u}"
            handles_arr.append({ "platform": "GitHub", "username": gh_u, "url": gh_url, "status": "VERIFIED" })
            matrix["GitHub"] = { "status": "VERIFIED", "username": gh_u, "url": gh_url, "confidence": 100.0 }
            raw_gh.append({
                "platform": "GitHub",
                "username": gh_u,
                "url": gh_url,
                "name": name,
                "bio": f"{role} at {inst}",
                "avatar_url": f"https://api.dicebear.com/7.x/avataaars/svg?seed={gh_u}"
            })
        else:
            matrix["GitHub"] = { "status": "NOT_FOUND", "username": None, "url": None, "confidence": 0.0 }

        if li_u:
            li_url = f"https://linkedin.com/in/{li_u}"
            handles_arr.append({ "platform": "LinkedIn", "username": li_u, "url": li_url, "status": "VERIFIED" })
            matrix["LinkedIn"] = { "status": "VERIFIED", "username": li_u, "url": li_url, "confidence": 98.0 }
            raw_li.append({
                "platform": "LinkedIn",
                "username": li_u,
                "url": li_url,
                "name": name,
                "headline": f"{role} at {inst}",
                "institution": inst,
                "avatar_url": f"https://api.dicebear.com/7.x/avataaars/svg?seed={li_u}"
            })
        else:
            matrix["LinkedIn"] = { "status": "NOT_FOUND", "username": None, "url": None, "confidence": 0.0 }

        if ig_u:
            ig_url = f"https://instagram.com/{ig_u}"
            handles_arr.append({ "platform": "Instagram", "username": ig_u, "url": ig_url, "status": "VERIFIED" })
            matrix["Instagram"] = { "status": "VERIFIED", "username": ig_u, "url": ig_url, "confidence": 94.0 }
            raw_ig.append({
                "platform": "Instagram",
                "username": ig_u,
                "url": ig_url,
                "name": name,
                "bio": f"{role} | {inst}",
                "avatar_url": f"https://api.dicebear.com/7.x/avataaars/svg?seed={ig_u}"
            })
        else:
            matrix["Instagram"] = { "status": "NOT_FOUND", "username": None, "url": None, "confidence": 0.0 }

        if tw_u:
            tw_url = f"https://x.com/{tw_u}"
            handles_arr.append({ "platform": "X (Twitter)", "username": tw_u, "url": tw_url, "status": "VERIFIED" })
            matrix["X_Twitter"] = { "status": "VERIFIED", "username": tw_u, "url": tw_url, "confidence": 95.0 }
            raw_tw.append({
                "platform": "X (Twitter)",
                "username": tw_u,
                "url": tw_url,
                "name": name,
                "bio": f"Building & Researching {role} @ {inst}",
                "avatar_url": f"https://api.dicebear.com/7.x/avataaars/svg?seed={tw_u}"
            })
        else:
            matrix["X_Twitter"] = { "status": "NOT_FOUND", "username": None, "url": None, "confidence": 0.0 }

        email_prefix = name.lower().replace(" ", ".")
        inst_clean = inst.lower().replace(" ", "").replace("institute", "").replace("technology", "").replace("of", "").replace("college", "")[:8]
        contacts_obj = {
            "email": f"{email_prefix}@{inst_clean}.ac.in",
            "phone": f"+91 98230 {41105 + i}",
            "location": f"{inst.split()[-1]}, India"
        }
        mutual_contacts_arr = [
            { "name": f"Dr. {name.split()[0]} Research Lead", "role": f"Faculty Advisor @ {inst}", "platform": "LinkedIn" },
            { "name": f"{name.split()[0]} Collaborator", "role": "Co-Author & Contributor", "platform": "GitHub" }
        ]

        cand_obj = {
            "person_id": p_id,
            "canonical_name": name,
            "primary_image": f"https://api.dicebear.com/7.x/avataaars/svg?seed={p_id}",
            "institution": inst,
            "roles": [role],
            "handles": handles_arr,
            "platform_existence_matrix": matrix,
            "bios": [f"{role} specializing in multi-modal systems at {inst}."],
            "contacts": contacts_obj,
            "mutual_contacts": mutual_contacts_arr,
            "projects": [f"{name.lower().replace(' ', '-')}-research", "Verified Identity Target"],
            "timeline": [
                {
                    "date": "Sep 2026",
                    "year": "2026",
                    "event": f"Published LinkedIn Article: Scalable Systems in {role}",
                    "content": f"Exploring advanced architecture patterns for {role} at {inst}. Shared performance benchmarks and code snippets.",
                    "category": "post",
                    "platform": "LinkedIn",
                    "engagement": { "likes": 120 + (i * 3) % 150, "comments": 18 + i % 25 },
                    "url": handles_arr[1]["url"] if len(handles_arr) > 1 else (handles_arr[0]["url"] if handles_arr else None)
                },
                {
                    "date": "Jul 2026",
                    "year": "2026",
                    "event": f"Open Source Release: {name.split()[0].lower()}-{role.lower().replace(' ', '-')}-kit",
                    "content": f"Published production repository for {role} tools and automated evaluation pipelines.",
                    "category": "project",
                    "platform": "GitHub",
                    "engagement": { "stars": 85 + (i * 7) % 200, "forks": 14 + i % 30 },
                    "url": handles_arr[0]["url"] if handles_arr else None
                },
                {
                    "date": "May 2026",
                    "year": "2026",
                    "event": f"Finalist @ National {role.split()[-1]} Innovation Challenge",
                    "content": f"Awarded top placement for developing automated AI solutions at {inst}.",
                    "category": "hackathon",
                    "platform": "Award",
                    "engagement": { "likes": 160 + (i * 4) % 180, "comments": 30 }
                },
                {
                    "date": "Aug 2024",
                    "year": "2024",
                    "event": f"Joined {inst} as {role}",
                    "content": f"Appointed as {role} leading technical research and project development.",
                    "category": "career",
                    "platform": "Education"
                }
            ],
            "evidence_trail": [
                { "node_id": f"H_{p_id}_01", "source_url": handles_arr[0]["url"] if handles_arr else f"https://institution.edu/{p_id}", "verified_at": "2026-09-19", "proof_type": "Verified Institutional Directory Record" }
            ]
        }
        team.append(cand_obj)

    # Add core team profiles to raw platform dataset
    for c in team[:4]:
        for h in c["handles"]:
            plat = h["platform"]
            if plat == "GitHub":
                raw_gh.append({"platform": "GitHub", "username": h["username"], "url": h["url"], "name": c["canonical_name"], "bio": c["bios"][0], "avatar_url": c["primary_image"]})
            elif plat == "LinkedIn":
                raw_li.append({"platform": "LinkedIn", "username": h["username"], "url": h["url"], "name": c["canonical_name"], "headline": c["roles"][0], "institution": c["institution"], "avatar_url": c["primary_image"]})
            elif plat == "Instagram":
                raw_ig.append({"platform": "Instagram", "username": h["username"], "url": h["url"], "name": c["canonical_name"], "bio": c["bios"][0], "avatar_url": c["primary_image"]})
            elif plat == "X (Twitter)":
                raw_tw.append({"platform": "X (Twitter)", "username": h["username"], "url": h["url"], "name": c["canonical_name"], "bio": c["bios"][0], "avatar_url": c["primary_image"]})

    # Save candidates_dataset.json
    dataset_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dataset"))
    os.makedirs(dataset_dir, exist_ok=True)
    
    cand_path = os.path.join(dataset_dir, "candidates_dataset.json")
    with open(cand_path, "w", encoding="utf-8") as f:
        json.dump(team, f, indent=2)

    raw_data = {
        "github_profiles": raw_gh,
        "linkedin_profiles": raw_li,
        "instagram_profiles": raw_ig,
        "twitter_profiles": raw_tw
    }

    raw_path = os.path.join(dataset_dir, "raw_profiles.json")
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(raw_data, f, indent=2)

    print(f"Successfully generated {len(team)} candidate profiles!")
    print(f"Candidates Dataset: {cand_path}")
    print(f"Raw Profiles Dataset: {raw_path}")

if __name__ == "__main__":
    generate_50_user_dataset()
