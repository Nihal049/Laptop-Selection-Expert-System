BUDGET_OPTIONS = [
    "Below ₹40,000",
    "₹40,000 - ₹60,000",
    "₹60,000 - ₹80,000",
    "₹80,000 - ₹1,00,000",
    "Above ₹1,00,000"
]

USAGE_OPTIONS = [
    "Basic / Office Work",
    "Programming / Development",
    "Gaming",
    "Video Editing",
    "Student / Multitasking"
]

RAM_OPTIONS = [
    "8 GB",
    "16 GB",
    "32 GB"
]

STORAGE_OPTIONS = [
    "256 GB SSD",
    "512 GB SSD",
    "1 TB SSD"
]

GRAPHICS_OPTIONS = [
    "Integrated Graphics",
    "Dedicated Graphics"
]

RULES = [
    {
        "id": "RULE 1",
        "conditions": {
            "usage": "Basic / Office Work",
            "budget": "Below ₹40,000"
        },
        "recommendation": "Basic Student / Office Laptop",
        "rationale": "For everyday office documents, web browsing, and budget constraints, an entry-level laptop with integrated graphics provides dependable performance and great power efficiency."
    },
    {
        "id": "RULE 2",
        "conditions": {
            "usage": "Programming / Development",
            "ram": "16 GB",
            "storage": "512 GB SSD",
            "budget": "₹40,000 - ₹60,000"
        },
        "recommendation": "Programming / Mid-Range Laptop",
        "rationale": "A balanced developer machine offering 16 GB RAM for multitasking across IDEs, local servers, and browser tabs, paired with fast SSD storage."
    },
    {
        "id": "RULE 3",
        "conditions": {
            "usage": "Programming / Development",
            "ram": ["16 GB", "32 GB"],
            "budget": "₹60,000 - ₹80,000"
        },
        "recommendation": "High Performance Developer Laptop",
        "rationale": "Higher tier processing cores and ample RAM ensure smooth compilation times, containerization support, and responsive developer environments."
    },
    {
        "id": "RULE 4",
        "conditions": {
            "usage": "Gaming",
            "graphics": "Dedicated Graphics",
            "budget": "₹60,000 - ₹80,000"
        },
        "recommendation": "Mid-Range Gaming Laptop",
        "rationale": "Equipped with a dedicated GPU and high-refresh cooling to run modern games smoothly at 1080p medium-to-high settings."
    },
    {
        "id": "RULE 5",
        "conditions": {
            "usage": "Gaming",
            "graphics": "Dedicated Graphics",
            "budget": "₹80,000 - ₹1,00,000"
        },
        "recommendation": "High Performance Gaming Laptop",
        "rationale": "Features higher TGP dedicated graphics, high-refresh display, and superior thermal headroom for demanding AAA titles and ray tracing."
    },
    {
        "id": "RULE 6",
        "conditions": {
            "usage": "Video Editing",
            "ram": ["16 GB", "32 GB"],
            "graphics": "Dedicated Graphics",
            "budget": "₹60,000 - ₹80,000"
        },
        "recommendation": "Video Editing / Creator Laptop",
        "rationale": "Dedicated GPU hardware acceleration and at least 16 GB RAM enable smooth timeline scrubbing and fast rendering in Premiere, DaVinci, and After Effects."
    },
    {
        "id": "RULE 7",
        "conditions": {
            "usage": "Video Editing",
            "ram": "32 GB",
            "graphics": "Dedicated Graphics",
            "budget": "Above ₹1,00,000"
        },
        "recommendation": "Professional Creator Laptop",
        "rationale": "Premium studio-grade hardware with 32 GB RAM, color-calibrated display, and heavy GPU compute for seamless 4K/8K RAW footage workflows."
    },
    {
        "id": "RULE 8",
        "conditions": {
            "usage": "Student / Multitasking",
            "ram": "16 GB",
            "storage": "512 GB SSD"
        },
        "recommendation": "Student Productivity Laptop",
        "rationale": "Ideal combination of 16 GB memory and 512 GB SSD to keep multiple academic applications, research PDFs, and browser tabs open without slowdowns."
    },
    {
        "id": "RULE 9",
        "conditions": {
            "usage": "Student / Multitasking",
            "budget": "Below ₹40,000"
        },
        "recommendation": "Budget Student Laptop",
        "rationale": "Optimized for classroom lectures, online research, document editing, and video conferences at an affordable student price."
    },
    {
        "id": "RULE 10",
        "conditions": {
            "usage": "Student / Multitasking",
            "budget": "₹40,000 - ₹60,000"
        },
        "recommendation": "Mainstream Student All-Rounder",
        "rationale": "Offers solid battery endurance, lightweight chassis for portability, and snappy performance for diverse coursework."
    },
    {
        "id": "RULE 11",
        "conditions": {
            "usage": "Student / Multitasking",
            "ram": ["16 GB", "32 GB"],
            "budget": ["₹60,000 - ₹80,000", "₹80,000 - ₹1,00,000", "Above ₹1,00,000"]
        },
        "recommendation": "Premium Student Ultrabook",
        "rationale": "Sleek, lightweight build with all-day battery life, premium screen, and fast responsiveness for rigorous academic workloads."
    },
    {
        "id": "RULE 12",
        "conditions": {
            "usage": "Gaming",
            "graphics": "Dedicated Graphics",
            "ram": "32 GB",
            "budget": "Above ₹1,00,000"
        },
        "recommendation": "Enthusiast / Flagship Gaming Laptop",
        "rationale": "Top-tier dedicated GPU paired with 32 GB RAM, high-refresh display, and advanced vapor chamber cooling for uncompromising AAA gaming and simulation."
    },
    {
        "id": "RULE 13",
        "conditions": {
            "usage": "Gaming",
            "graphics": "Dedicated Graphics",
            "budget": "₹40,000 - ₹60,000"
        },
        "recommendation": "Entry-Level Gaming Laptop",
        "rationale": "An accessible gaming laptop providing an entry-tier dedicated GPU for enjoyable 1080p gameplay in competitive and popular games."
    },
    {
        "id": "RULE 14",
        "conditions": {
            "usage": "Gaming",
            "graphics": "Integrated Graphics"
        },
        "recommendation": "Casual / Light Esports Gaming Laptop",
        "rationale": "Integrated graphics can handle casual and lightweight esports titles, but modern AAA gaming will require a dedicated GPU."
    },
    {
        "id": "RULE 15",
        "conditions": {
            "usage": "Video Editing",
            "ram": ["16 GB", "32 GB"],
            "graphics": "Dedicated Graphics",
            "budget": "₹80,000 - ₹1,00,000"
        },
        "recommendation": "Advanced Studio Creator Laptop",
        "rationale": "High-color accuracy display, multi-core CPU, and strong dedicated GPU performance for 4K video editing and 3D visual effects."
    },
    {
        "id": "RULE 16",
        "conditions": {
            "usage": "Video Editing",
            "graphics": "Dedicated Graphics",
            "budget": "₹40,000 - ₹60,000"
        },
        "recommendation": "Entry-Level Creator Laptop",
        "rationale": "Offers budget dedicated GPU acceleration for 1080p timeline edits, social media video production, and graphic design."
    },
    {
        "id": "RULE 17",
        "conditions": {
            "usage": "Video Editing",
            "graphics": "Integrated Graphics"
        },
        "recommendation": "Basic Video Editing Laptop",
        "rationale": "Integrated graphics are suitable for basic video editing, but dedicated graphics are recommended for heavy video editing, complex timelines, and faster rendering."
    },
    {
        "id": "RULE 18",
        "conditions": {
            "usage": "Programming / Development",
            "budget": "Below ₹40,000"
        },
        "recommendation": "Entry-Level Programming Laptop",
        "rationale": "A starter laptop suited for beginners learning Python, C/C++, web development, and foundational computer science topics."
    },
    {
        "id": "RULE 19",
        "conditions": {
            "usage": "Programming / Development",
            "ram": "32 GB",
            "budget": "Above ₹1,00,000"
        },
        "recommendation": "Flagship Heavy Development Workstation",
        "rationale": "Massive 32 GB memory and top-tier multi-threaded processor designed for virtualization, heavy Docker clusters, and large enterprise codebases."
    },
    {
        "id": "RULE 20",
        "conditions": {
            "usage": "Programming / Development",
            "budget": "₹80,000 - ₹1,00,000"
        },
        "recommendation": "Enterprise Software Engineering Laptop",
        "rationale": "High build quality, ergonomic keyboard, fast compiling speeds, and extended battery life for full-stack engineering."
    },
    {
        "id": "RULE 21",
        "conditions": {
            "usage": "Basic / Office Work",
            "budget": "₹40,000 - ₹60,000"
        },
        "recommendation": "Standard Business & Office Laptop",
        "rationale": "Comfortable keyboard, crisp display, and reliable execution of spreadsheets, presentations, and team communication suites."
    },
    {
        "id": "RULE 22",
        "conditions": {
            "usage": "Basic / Office Work",
            "budget": "₹60,000 - ₹80,000"
        },
        "recommendation": "Premium Executive Office Laptop",
        "rationale": "Sleek aluminum chassis, quiet operation, and long battery life engineered for executive multitasking and presentations."
    },
    {
        "id": "RULE 23",
        "conditions": {
            "usage": "Basic / Office Work",
            "budget": ["₹80,000 - ₹1,00,000", "Above ₹1,00,000"]
        },
        "recommendation": "Executive Enterprise Ultrabook",
        "rationale": "Ultra-lightweight premium laptop with military-grade durability, enterprise biometric security, and all-day endurance."
    },
    {
        "id": "RULE 24",
        "conditions": {
            "usage": "Programming / Development",
            "graphics": "Dedicated Graphics",
            "ram": ["16 GB", "32 GB"],
            "budget": ["₹80,000 - ₹1,00,000", "Above ₹1,00,000"]
        },
        "recommendation": "Full-Stack & AI/ML Development Laptop",
        "rationale": "Combines a high-performance dedicated GPU for CUDA acceleration, local LLMs, and game engines with high memory for complex development."
    },
    {
        "id": "RULE 25",
        "conditions": {
            "usage": "Gaming",
            "graphics": "Dedicated Graphics",
            "ram": "16 GB",
            "budget": "Above ₹1,00,000"
        },
        "recommendation": "High Performance Gaming Laptop",
        "rationale": "A powerful gaming configuration featuring a top-tier dedicated GPU and 16 GB RAM, offering smooth high-refresh gameplay for demanding modern titles."
    },
    {
        "id": "RULE 26",
        "conditions": {
            "usage": "Gaming",
            "graphics": "Dedicated Graphics",
            "ram": "8 GB",
            "budget": "Above ₹1,00,000"
        },
        "recommendation": "Gaming Laptop - RAM Upgrade Recommended",
        "rationale": "The budget and dedicated graphics support a high-performance gaming configuration, but 8 GB RAM may limit performance and 16 GB or higher RAM is recommended."
    },
    {
        "id": "RULE 27",
        "conditions": {
            "usage": "Gaming",
            "budget": "Below ₹40,000",
            "ram": "32 GB",
            "storage": "1 TB SSD",
            "graphics": "Dedicated Graphics"
        },
        "recommendation": "Budget Insufficient for Selected Gaming Requirements",
        "rationale": "The selected gaming requirements include 32 GB RAM, 1 TB SSD and dedicated graphics, while the selected budget is below ₹40,000. Based on the expert-system rules, this combination requires a higher budget. Consider increasing the budget or reducing the RAM or storage requirements."
    },
    {
        "id": "RULE 28",
        "conditions": {
            "usage": "Gaming",
            "budget": "Below ₹40,000",
            "ram": "32 GB",
            "graphics": "Dedicated Graphics"
        },
        "recommendation": "Budget Insufficient / Reduce RAM Requirement",
        "rationale": "Pairing 32 GB RAM with dedicated graphics for gaming requires a higher budget tier than below ₹40,000. Consider increasing your budget or selecting 8 GB or 16 GB RAM."
    },
    {
        "id": "RULE 29",
        "conditions": {
            "usage": "Gaming",
            "budget": "Below ₹40,000",
            "storage": "1 TB SSD",
            "graphics": "Dedicated Graphics"
        },
        "recommendation": "Budget Insufficient / Review Storage Requirement",
        "rationale": "Dedicated graphics paired with a 1 TB SSD for gaming typically exceeds the below ₹40,000 budget bracket. Consider increasing your budget or opting for 256 GB or 512 GB SSD storage."
    }
]


def format_rule(rule):
    lines = [rule["id"]]
    first = True
    order = ["usage", "graphics", "ram", "storage", "budget"]
    sorted_keys = sorted(
        rule["conditions"].keys(),
        key=lambda k: order.index(k) if k in order else 99
    )
    for key in sorted_keys:
        value = rule["conditions"][key]
        field_name = "RAM" if key == "ram" else key.capitalize()
        val_str = " or ".join(value) if isinstance(value, (list, tuple)) else str(value)
        prefix = "IF" if first else "AND"
        lines.append(f"{prefix} {field_name} = {val_str}")
        first = False
    lines.append(f"THEN Recommendation = {rule['recommendation']}")
    return "\n".join(lines)


def get_all_rules_text():
    divider = "\n\n" + ("-" * 50) + "\n\n"
    return divider.join(format_rule(r) for r in RULES)

