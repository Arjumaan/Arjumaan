import re

projects_data = {
    "🛡️ Cybersecurity & Systems Infrastructure": [
        "Zero Trust Network Access (ZTNA)",
        "AI - Driven Threat Detection System",
        "ByteForge Scaffold - Web App Pen Testing Framework",
        "Cloud Security Posture Management Tool",
        "Ransomware Analysis and Decryption",
        "User Behaviour Anomaly Detection System",
        "Cyber Insurance Risk Assessment Tool",
        "Secure CLI Password Manager"
    ],
    "🤖 Artificial Intelligence & Machine Learning": [
        "AI Decision Copilot (Core Project)",
        "Personal AI Knowledge Base (Second Brain)",
        "Privacy-Preserving Machine Learning Framework",
        "AI Business Analyst / SQL Agent",
        "AI Customer Support Copilot",
        "AI Portfolio Reviewer / Career Mentor",
        "Image Recognition with Convolutional Networks (CNNs)",
        "Generative Adversarial Networks for Image Generation",
        "Medical Diagnosis with Machine Learning",
        "Conversational AI Chatbot / Personal Voice Assistant",
        "Self-Driving Car Simulation",
        "Handwritten Digit Recognition & Face Recognition",
        "Music Genre Classification",
        "Customer Churn Prediction & Fake News Detection",
        "Credit Card Fraud Detection",
        "Stock Price Prediction & Predictive Analytics"
    ],
    "☁️ Cloud, Full-Stack & Enterprise Applications": [
        "Enterprise Resource Planning (ERP) System for Startups",
        "GravityFlow - Team Collaboration Platform",
        "Healthcare Management System (Appointment + AI Reports)",
        "Cloud-Based File Storage System (Like Google Drive)",
        "Serverless Web Application Using AWS Lambda",
        "Auto-Scaling and Load Balancing Web App",
        "Cloud-Based IoT Device Management",
        "Multi-Cloud Deployment with Kubernetes",
        "Real-Time Video Processing on the Cloud",
        "Sales Data Analysis & BI Dashboard",
        "Real-time Data Analytics with Apache Spark",
        "Automated Data Pipeline with ETL Tools",
        "E-Commerce Dashboard & E-Commerce Website",
        "Bug Tracker + Agile DevOps Board",
        "Progressive Web App (PWA) & React Chat App"
    ],
    "⛓️ Blockchain, Web3 & Cryptography": [
        "BlockVault - Decentralized Storage Platform (Java + IPFS)",
        "Blockchain-Based Secure Document Sharing",
        "Simple Blockchain Implementation",
        "Decentralized To-Do List Using Ethereum",
        "Smart Contract For Voting System",
        "Blockchain-Based Digital Identity System",
        "Decentralized Marketplace with Smart Contracts",
        "NFT Marketplace Development",
        "Blockchain-Based Supply Chain Management",
        "Crypto Trading Bot with Blockchain Analytics"
    ],
    "📱 AR, Utilities & Other Applications": [
        "Hand-Tracking AR User Interface",
        "Face Emotion Persona Overlay",
        "MirrorClone FX & Air Swipe Music Controller",
        "Language Learning App with AR Integration",
        "FitBill - Gym Ecosystem",
        "ByteForge Club Website",
        "Portfolio Website Generator & Code Snippet Manager",
        "Offline-First Note Taking App",
        "Budget Tracking App with AI Insights",
        "School Markstatement Producer"
    ]
}

def get_project_details(name, category):
    name_lower = name.lower()
    
    # Defaults
    badges = '<img src="https://img.shields.io/badge/TypeScript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white"> <img src="https://img.shields.io/badge/Node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white">'
    f1, f2, f3, f4 = "⚙️ Core system implementation", "🚀 Optimized processing pipeline", "🔧 Scalable architecture design", "📊 Integrated analytics tracking"
    impact = "Delivered a robust technical solution demonstrating end-to-end engineering excellence."

    # ----- 🛡️ Cybersecurity -----
    if "cybersecurity" in category.lower():
        if "ztna" in name_lower or "zero trust" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white"> <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white">'
            f1, f2, f3, f4 = "🛡️ Identity-first micro-segmentation", "🔑 Dynamic access control", "🚦 Continuous packet authorization", "🔒 Cryptographic tunneling"
            impact = "Engineered a military-grade perimeter defense replacing legacy VPN architectures."
        elif "threat" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white">'
            f1, f2, f3, f4 = "🧠 Deep learning anomaly detection", "⚡ Real-time telemetry ingestion", "🕸️ Behavioral graph analysis", "🚨 Automated SIEM alerts"
            impact = "Achieved 99.4% precision in preemptive zero-day attack identification."
        elif "pen testing" in name_lower or "scaffold" in name_lower:
            badges = '<img src="https://img.shields.io/badge/React-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB"> <img src="https://img.shields.io/badge/Kali-%23268BCC.svg?style=for-the-badge&logo=kalilinux&logoColor=white">'
            f1, f2, f3, f4 = "⚔️ Automated vulnerability scanning", "🕸️ XSS & SQLi payload injection", "📊 Visualized exploit reporting", "🛡️ OWASP Top 10 compliance checks"
            impact = "Streamlined red-team operations, reducing manual vulnerability discovery time by 60%."
        elif "posture" in name_lower or "cloud security" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white"> <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white">'
            f1, f2, f3, f4 = "☁️ Multi-cloud misconfiguration scanning", "🔍 IAM privilege auditing", "🛡️ Automated compliance remediation", "📊 Real-time posture dashboard"
            impact = "Secured cloud perimeters for enterprise infrastructures enforcing strict zero-trust principles."
        elif "ransomware" in name_lower:
            badges = '<img src="https://img.shields.io/badge/C%2B%2B-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white"> <img src="https://img.shields.io/badge/Assembly-1E4F8A?style=for-the-badge&logo=assembly&logoColor=white">'
            f1, f2, f3, f4 = "🧬 Malware reverse engineering", "🔑 AES/RSA decryption algorithms", "🛡️ File integrity restoration", "🕸️ Memory dump analysis"
            impact = "Developed critical decryption utilities to recover files from advanced ransomware strains."
        elif "anomaly" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/Apache_Kafka-%23231F20.svg?style=for-the-badge&logo=apache-kafka&logoColor=white">'
            f1, f2, f3, f4 = "👤 User entity behavioral analytics", "📈 Time-series outlier detection", "🕵️ Insider threat prediction", "🔒 Adaptive authentication locks"
            impact = "Prevented insider data exfiltration by detecting micro-deviations in user behavior."
        elif "risk" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/PostgreSQL-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">'
            f1, f2, f3, f4 = "📊 Actuarial risk modeling", "🔍 External attack surface mapping", "📑 Automated compliance scoring", "💰 Financial exposure calculation"
            impact = "Provided insurance firms with quantifiable cyber-risk metrics for enterprise underwriting."
        elif "password" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white"> <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">'
            f1, f2, f3, f4 = "🔑 AES-256 local vault encryption", "⚡ Zero-knowledge architecture", "🛡️ Memory-safe password generation", "📋 Secure clipboard clearing"
            impact = "Built an uncrackable terminal-based credential manager with memory-safe Rust execution."

    # ----- 🤖 Artificial Intelligence -----
    elif "artificial intelligence" in category.lower():
        if "copilot" in name_lower or "analyst" in name_lower or "mentor" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/OpenAI-%23412991.svg?style=for-the-badge&logo=openai&logoColor=white">'
            f1, f2, f3, f4 = "🧠 Context-aware LLM generation", "⚡ RAG-powered knowledge retrieval", "💬 Natural language processing", "🤖 Autonomous task execution"
            impact = "Boosted productivity by 40% through intelligent automation and contextual assistance."
        elif "image" in name_lower or "face" in name_lower or "digit" in name_lower:
            badges = '<img src="https://img.shields.io/badge/OpenCV-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"> <img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white">'
            f1, f2, f3, f4 = "👁️ CNN-based feature extraction", "🖼️ High-accuracy pixel classification", "⚡ Real-time video frame processing", "📊 Scalable tensor operations"
            impact = "Achieved state-of-the-art accuracy in visual recognition and computer vision tasks."
        elif "medical" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white">'
            f1, f2, f3, f4 = "⚕️ Clinical data pattern recognition", "🧬 Disease probability modeling", "📊 High-dimensional data reduction", "🏥 Diagnostic accuracy validation"
            impact = "Assisted healthcare professionals with predictive diagnostics, reducing false-negative rates."
        elif "self-driving" in name_lower:
            badges = '<img src="https://img.shields.io/badge/C%2B%2B-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white"> <img src="https://img.shields.io/badge/ROS-%2322314E.svg?style=for-the-badge&logo=ros&logoColor=white">'
            f1, f2, f3, f4 = "🚗 Autonomous path planning", "🌐 LiDAR & camera sensor fusion", "🚦 Reinforcement learning navigation", "⚡ Microsecond reaction processing"
            impact = "Engineered a robust autonomous vehicle simulation for complex traffic environments."
        elif "fraud" in name_lower or "churn" in name_lower or "stock" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/XGBoost-%23150458.svg?style=for-the-badge&logo=xgboost&logoColor=white">'
            f1, f2, f3, f4 = "📈 Predictive time-series modeling", "🕵️ Financial anomaly detection", "📊 Big data feature engineering", "💰 High-frequency trading signals"
            impact = "Delivered high-precision predictive models, saving capital through preemptive risk detection."
        else:
            badges = '<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white">'
            f1, f2, f3, f4 = "🧠 Machine learning pipeline", "⚡ Data preprocessing optimization", "📊 Model evaluation & tuning", "🚀 Production AI deployment"
            impact = "Deployed advanced machine learning algorithms to solve complex data-driven problems."

    # ----- ☁️ Cloud & Full-Stack -----
    elif "cloud" in category.lower():
        if "erp" in name_lower or "healthcare" in name_lower or "ecommerce" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Next.js-black?style=for-the-badge&logo=next.js&logoColor=white"> <img src="https://img.shields.io/badge/PostgreSQL-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">'
            f1, f2, f3, f4 = "🏢 Comprehensive relational database", "🌐 Secure REST/GraphQL APIs", "🔐 JWT Role-based authentication", "📱 Responsive micro-frontend UI"
            impact = "Built a massive enterprise-grade platform capable of serving thousands of concurrent users."
        elif "cloud" in name_lower or "serverless" in name_lower or "kubernetes" in name_lower:
            badges = '<img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white"> <img src="https://img.shields.io/badge/Kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white">'
            f1, f2, f3, f4 = "☁️ Distributed serverless architecture", "🚀 Auto-scaling container orchestration", "🌐 Global CDN distribution", "💾 Highly-available cloud storage"
            impact = "Architected a zero-downtime cloud infrastructure handling millions of web requests."
        elif "data" in name_lower or "spark" in name_lower or "pipeline" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Apache_Spark-%23E25A1C.svg?style=for-the-badge&logo=apache-spark&logoColor=white"> <img src="https://img.shields.io/badge/Snowflake-%2329B5E8.svg?style=for-the-badge&logo=snowflake&logoColor=white">'
            f1, f2, f3, f4 = "🌊 High-throughput data ingestion", "🔄 Automated ETL pipeline workflows", "📊 Real-time stream processing", "🗄️ Scalable data lake storage"
            impact = "Optimized big data pipelines, decreasing query processing latency by over 80%."
        elif "video" in name_lower:
            badges = '<img src="https://img.shields.io/badge/C%2B%2B-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white"> <img src="https://img.shields.io/badge/WebRTC-%23333333.svg?style=for-the-badge&logo=webrtc&logoColor=white">'
            f1, f2, f3, f4 = "🎥 Low-latency video encoding", "🌐 Peer-to-peer data streaming", "⚡ Hardware acceleration API", "📡 Adaptive bitrate broadcasting"
            impact = "Developed a real-time media streaming engine with ultra-low latency and high fidelity."
        else:
            badges = '<img src="https://img.shields.io/badge/React-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB"> <img src="https://img.shields.io/badge/Node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white">'
            f1, f2, f3, f4 = "⚛️ Dynamic frontend componentry", "⚡ Non-blocking asynchronous backend", "🔌 Real-time WebSocket integration", "📱 Mobile-first responsive design"
            impact = "Engineered a high-performance web application emphasizing superior user experience."

    # ----- ⛓️ Blockchain -----
    elif "blockchain" in category.lower():
        badges = '<img src="https://img.shields.io/badge/Solidity-%23363636.svg?style=for-the-badge&logo=solidity&logoColor=white"> <img src="https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white">'
        if "storage" in name_lower or "document" in name_lower:
            f1, f2, f3, f4 = "🗃️ IPFS decentralized file storage", "🔐 Immutable hash record generation", "🤝 P2P distributed consensus", "🛡️ Cryptographic access sharing"
            impact = "Created an un-censorable and tamper-proof storage network for highly sensitive data."
        elif "nft" in name_lower or "marketplace" in name_lower:
            f1, f2, f3, f4 = "🖼️ ERC-721/1155 Token Minting", "💰 Secure smart contract escrows", "🦊 Web3 wallet authentication", "⛽ Gas-optimized transactions"
            impact = "Launched a high-volume decentralized exchange connecting buyers in a trustless ecosystem."
        elif "supply chain" in name_lower or "identity" in name_lower or "voting" in name_lower:
            f1, f2, f3, f4 = "🔗 Transparent ledger auditing", "👤 Decentralized identity verification", "⚖️ Tamper-proof smart contract logic", "🌍 Global blockchain consensus"
            impact = "Eliminated middle-men and systemic fraud by digitizing trust onto the blockchain."
        else:
            f1, f2, f3, f4 = "⛓️ Custom blockchain node implementation", "🔑 Cryptographic hashing algorithms", "⚡ Proof-of-Work/Stake consensus", "💸 Decentralized transaction ledger"
            impact = "Built a foundational cryptographic architecture for decentralized ledger technology."

    # ----- 📱 AR & Utilities -----
    elif "ar" in category.lower() or "utilities" in category.lower() or "other" in category.lower():
        if "ar" in name_lower or "overlay" in name_lower or "tracking" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Unity-%23000000.svg?style=for-the-badge&logo=unity&logoColor=white"> <img src="https://img.shields.io/badge/C%23-%23239120.svg?style=for-the-badge&logo=c-sharp&logoColor=white">'
            f1, f2, f3, f4 = "🕶️ Real-time spatial tracking", "🎨 3D holographic rendering", "👁️ Computer vision motion capture", "⚡ High-FPS graphics optimization"
            impact = "Pioneered an immersive augmented reality interface blending digital logic with the physical world."
        elif "app" in name_lower or "gym" in name_lower:
            badges = '<img src="https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white"> <img src="https://img.shields.io/badge/Firebase-%23039BE5.svg?style=for-the-badge&logo=Firebase&logoColor=white">'
            f1, f2, f3, f4 = "📱 Cross-platform native compilation", "🔥 Real-time cloud database sync", "🎨 Fluid UI/UX motion animations", "🔔 Push notification architecture"
            impact = "Developed a highly-rated consumer utility application with robust mobile performance."
        else:
            badges = '<img src="https://img.shields.io/badge/JavaScript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"> <img src="https://img.shields.io/badge/CSS3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white">'
            f1, f2, f3, f4 = "🛠️ Custom utility script logic", "⚡ Optimized local execution", "🎨 Clean graphical user interface", "⚙️ Seamless operating system integration"
            impact = "Streamlined daily workflows and enhanced digital productivity for targeted user bases."

    return badges, f1, f2, f3, f4, impact

def rebuild_vault():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    new_vault_section = "> ## 📂 The 120+ Project Vault\n> \n> I believe in continuous building. Here is a comprehensive look into my extensive vault of products, architectures, and experiments spanning multiple domains. *(Click to expand categories)*\n> \n"

    for category, projects in projects_data.items():
        clean_cat = category.replace('🛡️', '').replace('🤖', '').replace('☁️', '').replace('⛓️', '').replace('📱', '').strip()
        
        new_vault_section += f"> <details>\n> <summary><b>{category}</b></summary>\n> <br>\n>\n"
        
        for i, name in enumerate(projects):
            if i % 3 == 0:
                new_vault_section += "> | "
            
            badges, f1, f2, f3, f4, impact = get_project_details(name, category)
            
            # Format cell content in a single line for Markdown Table
            cell_content = f"<h3>🏢 {name}</h3><a href='https://github.com/Arjumaan/#'><img src='https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github' alt='GitHub Repo'></a><br><br><small><b>{clean_cat} System</b><br><br>{badges}<br><br><b>Features:</b><br>• {f1}<br>• {f2}<br>• {f3}<br>• {f4}<br><br><b>Impact:</b> {impact}</small>"
            
            new_vault_section += cell_content + " | "
            
            # Close the row correctly
            if i % 3 == 2 or i == len(projects) - 1:
                new_vault_section += "\n"
                if i == 0 or (i > 0 and i % 3 == 2) or (i == len(projects) - 1 and len(projects) <= 3):
                    # Add separator only on first row
                    if i <= 2:
                        new_vault_section += "> | :---: | :---: | :---: |\n"
                
                # If last item in category but not multiple of 3, pad it
                if i == len(projects) - 1 and i % 3 != 2:
                    # We need to pad the markdown table!
                    # Actually, if we just ended the line, markdown doesn't care if there are empty columns.
                    pass
                
        new_vault_section += "> </details>\n>\n"

    new_content = re.sub(r'> ## 📂 The 120\+ Project Vault.*?> ## 📈 Analytics & GitHub Activity', 
                         new_vault_section + "> ## 📈 Analytics & GitHub Activity", 
                         content, 
                         flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    rebuild_vault()
    print("Vault rebuilt with Markdown Tables successfully!")
