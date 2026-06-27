import re

def rewrite_vault_as_cards():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Extract the vault section
    vault_match = re.search(r'(## 📂 The 120\+ Project Vault\n.*?\n<details>\n)(.*)(---.*## 📈 Analytics & GitHub Activity)', content, re.DOTALL)
    if not vault_match:
        print("Vault not found")
        return

    vault_header = vault_match.group(1)
    vault_body = vault_match.group(2)
    after_vault = vault_match.group(3)

    # Find all categories
    categories = re.findall(r'<summary><b>(.*?)</b></summary>\n<br>\n\n(.*?)</details>', vault_body, re.DOTALL)
    
    new_vault_body = ""
    
    for category_name, category_content in categories:
        new_vault_body += f"<details>\n<summary><b>{category_name}</b></summary>\n<br>\n\n<table>\n"
        
        # Find all projects in this category
        projects = re.findall(r'### 🏢 (.*?)\n\[!\[GitHub Repo.*?\]\((.*?)\)\]\n\n\*\*(.*?)\*\*\n\n(.*?)\n\n\*\*Features:\*\*\n(.*?)\n\*\*Impact:\*\* (.*?)\n\n---', category_content, re.DOTALL)
        
        for i, project in enumerate(projects):
            name, repo_link, sub_cat, badges, features_block, impact = project
            
            # Start row
            if i % 3 == 0:
                new_vault_body += "  <tr>\n"
                
            # Parse features
            features_html = ""
            for line in features_block.strip().split('\n'):
                line = line.replace('- ', '', 1).strip()
                features_html += f"        <li>{line}</li>\n"
                
            td = f"""    <td valign="top" width="33%">
      <h3>🏢 {name}</h3>
      <a href="{repo_link}"><img src="https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github" alt="GitHub Repo"></a><br><br>
      <b>{sub_cat}</b><br><br>
      {badges}<br><br>
      <b>Features:</b>
      <ul>
{features_html}      </ul>
      <b>Impact:</b> {impact}
    </td>\n"""
            
            new_vault_body += td
            
            # End row
            if i % 3 == 2 or i == len(projects) - 1:
                new_vault_body += "  </tr>\n"
                
        new_vault_body += "</table>\n\n</details>\n\n"
        
    # Replace in content
    new_content = content[:vault_match.start(2)] + new_vault_body + after_vault
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print("Vault updated as 3-column cards!")

if __name__ == "__main__":
    rewrite_vault_as_cards()
