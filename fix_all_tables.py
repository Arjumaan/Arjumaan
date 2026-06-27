import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Revert Professional Experience to Markdown table
prof_exp_html = r"""> <table border="10" width="100%">
>   <thead>
>     <tr>
>       <th align="left">Role & Organization</th>
>       <th align="left">Duration</th>
>       <th align="left">Impact & Responsibilities</th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td><b>CCTV & Network Infrastructure Intern</b> <br> <i>iFix Tech Solutions Pvt. Ltd.</i></td>
>       <td>2024 – 2026</td>
>       <td>Deployed and maintained IP-based CCTV network infrastructures. Handled complex router, switch, and endpoint configuration. Troubleshot device communication issues and contributed to the structured design of office network deployments.</td>
>     </tr>
>     <tr>
>       <td><b>SEO Analyst Intern</b> <br> <i>RankuHigher</i></td>
>       <td>2024 \(3 Mos\)</td>
>       <td>Optimized multiple client websites through targeted keyword research and on-page audits. Executed comprehensive competitor analysis. Successfully <b>ranked 14 websites from Not-Listed to #1 rank.</b></td>
>     </tr>
>     <tr>
>       <td><b>Freelance Network Engineer</b> <br> <i>Office Network Setup Project</i></td>
>       <td>Freelance</td>
>       <td>Architected and deployed a secure routing infrastructure featuring 3-tier departmental network segmentation. Configured strict inter-departmental endpoint deployments to ensure operational isolation.</td>
>     </tr>
>     <tr>
>       <td><b>Virtual Network Infrastructure Designer</b> <br> <i>Simulated Enterprise Project</i></td>
>       <td>Academic</td>
>       <td>Architected a production-grade enterprise network simulation. Designed comprehensive routing protocols, VLAN segmentation, IP addressing schemas, and secure access architectures.</td>
>     </tr>
>   </tbody>
> </table>"""

prof_exp_md = """> | Role & Organization | Duration | Impact & Responsibilities |
> | :--- | :--- | :--- |
> | **CCTV & Network Infrastructure Intern** <br> *iFix Tech Solutions Pvt. Ltd.* | 2024 – 2026 | Deployed and maintained IP-based CCTV network infrastructures. Handled complex router, switch, and endpoint configuration. Troubleshot device communication issues and contributed to the structured design of office network deployments. |
> | **SEO Analyst Intern** <br> *RankuHigher* | 2024 (3 Mos) | Optimized multiple client websites through targeted keyword research and on-page audits. Executed comprehensive competitor analysis. Successfully **ranked 14 websites from Not-Listed to #1 rank.** |
> | **Freelance Network Engineer** <br> *Office Network Setup Project* | Freelance | Architected and deployed a secure routing infrastructure featuring 3-tier departmental network segmentation. Configured strict inter-departmental endpoint deployments to ensure operational isolation. |
> | **Virtual Network Infrastructure Designer** <br> *Simulated Enterprise Project* | Academic | Architected a production-grade enterprise network simulation. Designed comprehensive routing protocols, VLAN segmentation, IP addressing schemas, and secure access architectures. |"""

content = re.sub(prof_exp_html, prof_exp_md, content)

# 2. Convert Startup Flagship Products to Markdown table
flagship_html = r"""> <table border="10">
>   <tr>
>     <td align="center" width="33%">
>       <h3>🛡️ AEGIS \(SOC\)</h3>
>       <p>A defense-grade Security Operations Center \(SOC\) project under SentraSec AI Systems, built to provide real-time threat detection, anomalous behavioral analysis, and enterprise-level incident response.</p>
>     </td>
>     <td align="center" width="33%">
>       <h3>🧠 Forge AI</h3>
>       <p>An advanced AI platform offering cutting-edge intelligence, automation pipelines, and agentic workflows designed to accelerate business intelligence and productivity.</p>
>     </td>
>     <td align="center" width="33%">
>       <h3>📚 CT Upskilling</h3>
>       <p>A premier EdTech platform revolutionizing how individuals learn, offering immersive tech upskilling and bridging the gap between academic knowledge and industry-grade engineering.</p>
>     </td>
>   </tr>
> </table>"""

flagship_md = """> | 🛡️ AEGIS (SOC) | 🧠 Forge AI | 📚 CT Upskilling |
> | :---: | :---: | :---: |
> | A defense-grade Security Operations Center (SOC) project under SentraSec AI Systems, built to provide real-time threat detection, anomalous behavioral analysis, and enterprise-level incident response. | An advanced AI platform offering cutting-edge intelligence, automation pipelines, and agentic workflows designed to accelerate business intelligence and productivity. | A premier EdTech platform revolutionizing how individuals learn, offering immersive tech upskilling and bridging the gap between academic knowledge and industry-grade engineering. |"""

content = re.sub(flagship_html, flagship_md, content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Tables converted to Markdown successfully!")
