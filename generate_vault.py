import re

def update_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Top Banner
    banner = '<img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,100:003366&height=200&section=header&text=Arjumaan.M&fontSize=50&fontColor=ffffff" alt="header" width="100%"/>\n\n<div align="center">'
    if "capsule-render" not in content:
        content = content.replace('<div align="center">', banner, 1)

    # 2. Insert Education Section
    education_section = """
## 🎓 Education

### Bachelor of Computer Science with Cyber Security
**Rathinam Global University** | Coimbatore, Tamil Nadu, India
*Jul 2024 - Apr 2027*
- **CGPA:** 8.4 / 10

### Higher Secondary HSC +2
**SBOA MAT HR. SEC SCHOOL** | Coimbatore, Tamil Nadu, India
*2023 - 2024*
- **Percentage:** 84%

---
"""
    if "## 🎓 Education" not in content:
        # Insert after Professional Experience
        content = re.sub(r'(## 💻 Core Engineering Arsenal)', f'{education_section}\n\\1', content)

    # 3. Analytics redesign
    analytics_replacement = """## 📈 Analytics & GitHub Activity

<div align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Arjumaan&theme=dracula" width="100%" alt="Profile Summary" />
</div>

<div align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Arjumaan&theme=dracula" width="48%" alt="Top Languages" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=Arjumaan&theme=dracula" width="48%" alt="Commits per hour" />
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Arjumaan&theme=dracula&hide_border=false" width="48%" alt="GitHub Streak" />
  <img src="https://komarev.com/ghpvc/?username=Arjumaan&color=blue&style=flat-square&label=Profile+Views" width="48%" alt="Profile Views" />
</div>

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Arjumaan&theme=dracula" width="100%" alt="Contribution Graph" />
</div>"""

    content = re.sub(r'## 📈 Analytics & GitHub Activity.*', analytics_replacement, content, flags=re.DOTALL)

    # 4. Project Vault Redesign
    # We will use regex to find all <details> blocks in the vault and rewrite them.
    # The structure of a details block is:
    # <details>
    # <summary><b>CATEGORY</b></summary>
    # | Project Name | Repository | ...
    # </details>
    
    def format_project(name, category):
        # Generate some placeholder but logical tech stacks and features based on category/name
        # Badges templates
        badges = []
        if "AI" in name or "Machine" in name or "Detection" in name or "Analytics" in name or "Data" in name:
            badges = ['![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)',
                      '![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)']
        elif "Blockchain" in name or "Decentralized" in name or "Crypto" in name or "NFT" in name:
            badges = ['![Solidity](https://img.shields.io/badge/Solidity-%23363636.svg?style=for-the-badge&logo=solidity&logoColor=white)',
                      '![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)']
        elif "Cloud" in name or "Serverless" in name or "Pipeline" in name:
            badges = ['![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)',
                      '![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)']
        elif "App" in name or "UI" in name or "Platform" in name or "Website" in name or "Dashboard" in name:
            badges = ['![React](https://img.shields.io/badge/React-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)',
                      '![Node.js](https://img.shields.io/badge/Node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)']
        else:
            badges = ['![Java](https://img.shields.io/badge/Java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)',
                      '![C++](https://img.shields.io/badge/C%2B%2B-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)']
            
        features = [
            "🧠 Advanced algorithmic implementation.",
            "⚡ High-performance computing backend.",
            "🔐 Secure and robust architecture.",
            "📊 Comprehensive data processing."
        ]
        
        impact = "Demonstrates cutting-edge engineering capable of scaling to enterprise levels."

        badges_str = " ".join(badges)
        
        return f"""### 🏢 {name}
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github)](https://github.com/Arjumaan/#)

**{category.replace('🛡️', '').replace('🤖', '').replace('☁️', '').replace('⛓️', '').replace('📱', '').strip()} System**

{badges_str}

**Features:**
- {features[0]}
- {features[1]}
- {features[2]}
- {features[3]}

**Impact:** {impact}
"""

    # We need to process the whole vault section
    # Let's extract the vault part
    vault_match = re.search(r'(## 📂 The 120\+ Project Vault\n.*?\n)(---)', content, re.DOTALL)
    if vault_match:
        vault_section = vault_match.group(1)
        
        new_vault_section = "## 📂 The 120+ Project Vault\n\nI believe in continuous building. Here is a comprehensive look into my extensive vault of products, architectures, and experiments spanning multiple domains. *(Click to expand categories)*\n\n"
        
        # Find all details tags
        details_blocks = re.findall(r'<details>\n<summary><b>(.*?)</b></summary>\n\n(.*?)\n</details>', vault_section, re.DOTALL)
        
        for category, block_content in details_blocks:
            new_vault_section += f"<details>\n<summary><b>{category}</b></summary>\n<br>\n\n"
            
            # Find all projects in the table
            projects = re.findall(r'\|\s*\*\*(.*?)\*\*\s*\|\s*\[.*?\]\(.*?\)\s*\|', block_content)
            
            for project in projects:
                new_vault_section += format_project(project, category)
                new_vault_section += "\n---\n\n"
                
            new_vault_section += "</details>\n\n"
            
        content = content.replace(vault_section, new_vault_section)
        
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
        
    print("README updated successfully.")

if __name__ == "__main__":
    update_readme()
