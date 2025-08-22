
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus.flowables import Flowable
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.graphics import renderPDF

class SidebarSection(Flowable):
    def __init__(self, width, height, bg_color):
        self.width = width
        self.height = height
        self.bg_color = bg_color
    
    def draw(self):
        self.canv.setFillColor(self.bg_color)
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)

def create_cv():
    # إعداد المستند
    doc = SimpleDocTemplate(
        "Omar_Mohamed_Etman_CV.pdf",
        pagesize=A4,
        rightMargin=1*cm,
        leftMargin=1*cm,
        topMargin=1*cm,
        bottomMargin=1*cm
    )
    
    # الألوان
    navy_blue = HexColor('#1F3C88')
    light_gray = HexColor('#F4F6F8')
    dark_gray = HexColor('#2C3E50')
    text_gray = HexColor('#555555')
    
    # إعداد الأنماط
    styles = getSampleStyleSheet()
    
    # أنماط مخصصة للعنوان الرئيسي
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Heading1'],
        fontSize=28,
        spaceAfter=8,
        textColor=navy_blue,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontSize=14,
        spaceAfter=12,
        textColor=dark_gray,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # أنماط الشريط الجانبي
    sidebar_header_style = ParagraphStyle(
        'SidebarHeader',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=8,
        textColor=white,
        fontName='Helvetica-Bold'
    )
    
    sidebar_text_style = ParagraphStyle(
        'SidebarText',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=4,
        textColor=white,
        fontName='Helvetica'
    )
    
    # أنماط المحتوى الرئيسي
    section_header_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=15,
        spaceAfter=10,
        textColor=navy_blue,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        textColor=text_gray,
        fontName='Helvetica'
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=4,
        leftIndent=15,
        textColor=text_gray,
        fontName='Helvetica'
    )
    
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        textColor=dark_gray,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # بناء المحتوى
    content = []
    
    # الصفحة الأولى
    # العنوان الرئيسي
    content.append(Paragraph("Omar Mohamed Etman", name_style))
    content.append(Paragraph("Software Engineer | Flutter & Web Developer | Digital Products Entrepreneur", title_style))
    content.append(Spacer(1, 10))
    
    # معلومات الاتصال
    contact_info = [
        "📍 Mansoura, Egypt",
        "📞 +20 1093669731",
        "✉️ omarm3tman@gmail.com",
        "🌐 https://omarmetman.vercel.app",
        "💻 github.com/omarmetman",
        "📱 @omaretmanBOT"
    ]
    
    contact_table_data = []
    for i in range(0, len(contact_info), 2):
        row = [contact_info[i]]
        if i + 1 < len(contact_info):
            row.append(contact_info[i + 1])
        else:
            row.append("")
        contact_table_data.append(row)
    
    contact_table = Table(contact_table_data, colWidths=[9*cm, 9*cm])
    contact_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), dark_gray),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    content.append(contact_table)
    content.append(Spacer(1, 20))
    
    # جدول ذو عمودين - الشريط الجانبي والمحتوى الرئيسي
    # العمود الأيسر (الشريط الجانبي)
    sidebar_content = []
    
    # مهارات أساسية
    sidebar_content.append(Paragraph("CORE SKILLS", sidebar_header_style))
    skills_sections = [
        ("Programming:", "Dart (Flutter), JavaScript, Python, C++, HTML5, CSS3"),
        ("Mobile Dev:", "Flutter UI/UX, State Management, Firebase"),
        ("Web Dev:", "React, WordPress, Responsive Design"),
        ("Databases:", "Firebase, MySQL, MongoDB, REST APIs"),
        ("Tools:", "Git/GitHub, VS Code, Figma, Docker"),
        ("Other:", "SEO, Digital Marketing, Sales Automation")
    ]
    
    for skill_cat, skill_list in skills_sections:
        sidebar_content.append(Paragraph(f"<b>{skill_cat}</b><br/>{skill_list}", sidebar_text_style))
        sidebar_content.append(Spacer(1, 6))
    
    # اللغات
    sidebar_content.append(Paragraph("LANGUAGES", sidebar_header_style))
    sidebar_content.append(Paragraph("• Arabic - Native<br/>• English - Upper-Intermediate", sidebar_text_style))
    
    # الاهتمامات
    sidebar_content.append(Paragraph("INTERESTS", sidebar_header_style))
    interests = [
        "• SaaS & Tech Entrepreneurship",
        "• Reading (2000+ books)",
        "• UX Design & Analytics"
    ]
    for interest in interests:
        sidebar_content.append(Paragraph(interest, sidebar_text_style))
    
    # العمود الأيمن (المحتوى الرئيسي)
    main_content = []
    
    # الملف التعريفي
    main_content.append(Paragraph("PROFILE SUMMARY", section_header_style))
    main_content.append(Paragraph(
        "Ambitious and fast-learning Software Engineer with expertise in Flutter mobile apps, web development, and digital product sales. Proven ability to build scalable, user-focused applications while managing online businesses and driving revenue growth. Experienced in integrating backend services, analyzing user behavior, and optimizing UI/UX for better engagement. Entrepreneurial mindset with a passion for creating digital solutions that deliver measurable results.",
        body_style
    ))
    main_content.append(Spacer(1, 15))
    
    # الخبرة المهنية
    main_content.append(Paragraph("PROFESSIONAL EXPERIENCE", section_header_style))
    
    # خبرة 1
    main_content.append(Paragraph("<b>Freelance Digital Product Seller</b> | 2022 – Present", body_style))
    exp1_items = [
        "Designed and sold professional website templates, digital assets, and client services.",
        "Created sales funnels using WhatsApp groups, online forms, and automated follow-ups.",
        "Increased customer conversion rates by optimizing UX and A/B testing landing pages."
    ]
    for item in exp1_items:
        main_content.append(Paragraph(f"• {item}", bullet_style))
    main_content.append(Spacer(1, 8))
    
    # خبرة 2
    main_content.append(Paragraph("<b>Flutter Developer</b> | 2021 – Present", body_style))
    exp2_items = [
        "Built cross-platform apps with Flutter, implementing responsive UI and smooth animations.",
        "Integrated Firebase authentication, Firestore database, and push notifications.",
        "Published demo apps for clients and personal use with focus on performance."
    ]
    for item in exp2_items:
        main_content.append(Paragraph(f"• {item}", bullet_style))
    main_content.append(Spacer(1, 8))
    
    # خبرة 3
    main_content.append(Paragraph("<b>Business & Real Estate Sales Projects</b> | 2020 – 2021", body_style))
    main_content.append(Paragraph("• Supported product marketing, negotiations, and digital lead management.", bullet_style))
    main_content.append(Paragraph("• Prepared sales projections and financial reporting.", bullet_style))
    
    # إنشاء جدول بعمودين
    # تحويل المحتوى إلى نص
    sidebar_text = ""
    main_text = ""
    
    # بناء الجدول
    page1_data = [
        [
            # الشريط الجانبي
            Paragraph("""
            <para bgcolor="#1F3C88" leftIndent="10" rightIndent="10" spaceBefore="10" spaceAfter="10">
            <font color="white" size="14"><b>CORE SKILLS</b></font><br/><br/>
            <font color="white" size="10">
            <b>Programming:</b><br/>Dart (Flutter), JavaScript, Python, C++, HTML5, CSS3<br/><br/>
            <b>Mobile Development:</b><br/>Flutter UI/UX, State Management, Firebase<br/><br/>
            <b>Web Development:</b><br/>React basics, WordPress, Responsive Design<br/><br/>
            <b>Databases & Cloud:</b><br/>Firebase, MySQL, MongoDB, REST APIs<br/><br/>
            <b>Tools & Platforms:</b><br/>Git/GitHub, VS Code, Figma, Docker<br/><br/>
            <b>Other Expertise:</b><br/>SEO, Digital Marketing, Sales Automation<br/><br/><br/>
            
            <b>LANGUAGES</b><br/><br/>
            • Arabic - Native<br/>
            • English - Upper-Intermediate<br/><br/><br/>
            
            <b>INTERESTS</b><br/><br/>
            • SaaS & Tech Entrepreneurship<br/>
            • Reading (2000+ books)<br/>
            • UX Design & Analytics
            </font>
            </para>
            """, ParagraphStyle('sidebar', fontName='Helvetica', fontSize=10)),
            
            # المحتوى الرئيسي
            Paragraph("""
            <font color="#1F3C88" size="16"><b>PROFILE SUMMARY</b></font><br/><br/>
            <font color="#555555" size="11">
            Ambitious and fast-learning Software Engineer with expertise in Flutter mobile apps, web development, and digital product sales. Proven ability to build scalable, user-focused applications while managing online businesses and driving revenue growth. Experienced in integrating backend services, analyzing user behavior, and optimizing UI/UX for better engagement. Entrepreneurial mindset with a passion for creating digital solutions that deliver measurable results.
            </font><br/><br/>
            
            <font color="#1F3C88" size="16"><b>PROFESSIONAL EXPERIENCE</b></font><br/><br/>
            
            <font color="#555555" size="11"><b>Freelance Digital Product Seller</b> | 2022 – Present<br/>
            • Designed and sold professional website templates, digital assets, and client services.<br/>
            • Created sales funnels using WhatsApp groups, online forms, and automated follow-ups.<br/>
            • Increased customer conversion rates by optimizing UX and A/B testing landing pages.<br/><br/>
            
            <b>Flutter Developer</b> | 2021 – Present<br/>
            • Built cross-platform apps with Flutter, implementing responsive UI and smooth animations.<br/>
            • Integrated Firebase authentication, Firestore database, and push notifications.<br/>
            • Published demo apps for clients and personal use with focus on performance.<br/><br/>
            
            <b>Business & Real Estate Sales Projects</b> | 2020 – 2021<br/>
            • Supported product marketing, negotiations, and digital lead management.<br/>
            • Prepared sales projections and financial reporting.
            </font>
            """, body_style)
        ]
    ]
    
    page1_table = Table(page1_data, colWidths=[6*cm, 12*cm])
    page1_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    
    content.append(page1_table)
    
    # فاصل الصفحة
    content.append(PageBreak())
    
    # الصفحة الثانية
    page2_data = [
        [
            # الشريط الجانبي للصفحة الثانية
            Paragraph("""
            <para bgcolor="#1F3C88" leftIndent="10" rightIndent="10" spaceBefore="10" spaceAfter="10">
            <font color="white" size="14"><b>CERTIFICATIONS</b></font><br/><br/>
            <font color="white" size="10">
            • Flutter & Dart Foundations<br/>  Udemy (2023)<br/><br/>
            • Web Development Fundamentals<br/>  FreeCodeCamp (2022)<br/><br/>
            • Digital Marketing Basics<br/>  Google Digital Garage (2022)<br/><br/><br/>
            
            <b>EDUCATION</b><br/><br/>
            <b>High School</b><br/>
            Mansoura, Egypt<br/>
            (Born March 2005)<br/><br/>
            
            <b>Self-Learning & MOOCs:</b><br/>
            • Flutter Development Bootcamps<br/>
            • Web Development<br/>
            • Digital Marketing & SEO
            </font>
            </para>
            """, ParagraphStyle('sidebar', fontName='Helvetica', fontSize=10)),
            
            # المحتوى الرئيسي للصفحة الثانية
            Paragraph("""
            <font color="#1F3C88" size="16"><b>PROJECTS</b></font><br/><br/>
            <font color="#555555" size="11">
            <b>• Digital Templates Store</b><br/>
            Created a platform for reselling web templates and digital products with order tracking.<br/><br/>
            
            <b>• Telegram Bot (@omaretmanBOT)</b><br/>
            Automated customer notifications and digital content delivery.<br/><br/>
            
            <b>• E-Commerce Demo App</b><br/>
            Built in Flutter with shopping cart, product catalog, and contact forms.<br/><br/>
            
            <b>• Personal Portfolio</b><br/>
            Developed with responsive design showcasing coding projects and GitHub work.<br/><br/>
            </font>
            
            <font color="#1F3C88" size="16"><b>TECHNICAL ACHIEVEMENTS</b></font><br/><br/>
            <font color="#555555" size="11">
            • Successfully deployed multiple Flutter apps to both iOS and Android platforms<br/>
            • Implemented real-time database synchronization with Firebase<br/>
            • Built responsive web applications with modern JavaScript frameworks<br/>
            • Created automated sales funnels that increased conversion rates by 40%<br/>
            • Developed custom WordPress themes and plugins for client projects<br/>
            • Integrated payment gateways and subscription management systems<br/><br/>
            </font>
            
            <font color="#1F3C88" size="16"><b>ENTREPRENEURIAL EXPERIENCE</b></font><br/><br/>
            <font color="#555555" size="11">
            • Built and managed online business generating consistent revenue<br/>
            • Analyzed customer behavior data to optimize product offerings<br/>
            • Created marketing content and managed social media presence<br/>
            • Developed customer support systems and automated workflows
            </font>
            """, body_style)
        ]
    ]
    
    page2_table = Table(page2_data, colWidths=[6*cm, 12*cm])
    page2_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    
    content.append(page2_table)
    
    # إنشاء الملف
    doc.build(content)
    print("تم إنشاء السيرة الذاتية الجديدة بنجاح: Omar_Mohamed_Etman_CV.pdf")

if __name__ == "__main__":
    create_cv()
