import re

markdown_table = """> | Role & Organization | Duration | Impact & Responsibilities |
> | :--- | :--- | :--- |
> | **CCTV & Network Infrastructure Intern** <br> *iFix Tech Solutions Pvt. Ltd.* | 2024 – 2026 | Deployed and maintained IP-based CCTV network infrastructures. Handled complex router, switch, and endpoint configuration. Troubleshot device communication issues and contributed to the structured design of office network deployments. |
> | **SEO Analyst Intern** <br> *RankuHigher* | 2024 (3 Mos) | Optimized multiple client websites through targeted keyword research and on-page audits. Executed comprehensive competitor analysis. Successfully **ranked 14 websites from Not-Listed to #1 rank.** |
> | **Freelance Network Engineer** <br> *Office Network Setup Project* | Freelance | Architected and deployed a secure routing infrastructure featuring 3-tier departmental network segmentation. Configured strict inter-departmental endpoint deployments to ensure operational isolation. |
> | **Virtual Network Infrastructure Designer** <br> *Simulated Enterprise Project* | Academic | Architected a production-grade enterprise network simulation. Designed comprehensive routing protocols, VLAN segmentation, IP addressing schemas, and secure access architectures. |"""

html_table = """> <table border="10" width="100%">
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
>       <td>2024 (3 Mos)</td>
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

with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace border="3" with border="10"
text = text.replace('border="3"', 'border="10"')

# Replace the markdown table
if markdown_table in text:
    text = text.replace(markdown_table, html_table)
    print("Replaced markdown table successfully.")
else:
    print("Markdown table not found!")

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)
