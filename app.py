from flask import Flask, render_template_string

app = Flask(__name__)

# Skill levels
skills = {
    'Python': 60,
    'Java': 40,
    'HTML': 88,
    'CSS': 80,
    'JavaScript': 30,
    'Flask': 70,
    'Django': 40,
    'Discipline': 90
}

# Project information
projects = [
    {
        'name': 'Freud IA',
        'description': 'A psychologist project consisting of a general system for providing psychological attention to anyone around the world.',
        'link': 'https://elmerurbina.github.io/freud.ia',
        'image': 'logo.jpg',
        'alt': 'Freud IA Logo'
    },
    {
        'name': 'FarmTech',
        'description': 'A mobile app with a Django server for ganaderos (livestock farmers) where they can manage inventories, cow registrations, production, cost structures, production plans, etc.',
        'link': 'https:github.com/farmtech24/farmtech',
        'image': None,  # Add image if available
        'alt': None  # Add alt text if available
    }
]

# Footer content
footer_content = """
Second Place Winner in the Web Pages category at Feria Nacional de Ciencia y Tecnologia UNI. Our project is featured as image number 6 in the post. <a href="https://www.facebook.com/share/p/GUBJwDLNdAYXGtab/?mibextid=xfxF2i">See the post</a>. Collaborated with two other team members. <a href="https://github.com/elmerurbina/automator">See the project on GitHub</a>.
"""


@app.route('/elmerurbina')
def home():
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>My Portfolio</title>
            <style>
                body {
                    background-color: #378CE7;
                    color: #FFF;
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                }

                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }

                h1, h2, h3 {
                    color: #F9F07A;
                }

                p {
                    margin-bottom: 20px;
                }

                .skill {
                    margin-bottom: 20px;
                }

                .progress {
                    background-color: #1A1A1D;
                    border-radius: 5px;
                    overflow: hidden;
                    height: 20px;
                }

                .progress-bar {
                    background-color: #2CEEF0;
                    width: 0;
                    height: 100%;
                    line-height: 20px;
                    text-align: center;
                    transition: width 1s ease-in-out;
                }

                .project {
                    background-color: #1D4E8F;
                    padding: 20px;
                    border-radius: 5px;
                    margin-bottom: 20px;
                }

                .project h3 {
                    margin-top: 0;
                }

                .footer {
                    text-align: center;
                    margin-top: 50px;
                }

                a {
                    color: #16FF00;
                    text-decoration: none;
                }

                a:hover {
                    text-decoration: underline;
                }
                
                .menu {
                    float: right;
                    margin-right: 50px;
                }

                .menu a {
                    color: white;
                    text-decoration: none;
                    margin-left: 20px;
                    display: inline-block; /* Display menu items horizontally */
                }

                .dropdown {
                    float: right;
                    position: relative;
                    display: inline-block;
                }

                .dropdown button {
                    background-color: transparent;
                    border: none;
                    cursor: pointer;
                    font-size: 20px;
                    color: white;
                }
                .dropdown #servicesDropdownContent,
                .dropdown #contactDropdownContent,
                .dropdown #languagesDropdownContent {
                    display: none;
                    position: absolute;
                    background-color: #1D4E8F;
                    min-width: 160px;
                    z-index: 1;
                    right: 0;
                    margin-top: 40px;
                }

                .dropdown #servicesDropdownContent a,
                .dropdown #contactDropdownContent a,
                .dropdown #languagesDropdownContent a {
                    color: white;
                    padding: 12px 16px;
                    text-decoration: none;
                    display: block;
                }

                .dropdown #servicesDropdownContent a:hover,
                .dropdown #contactDropdownContent a:hover,
                .dropdown #languagesDropdownContent a:hover {
                    background-color: #378CE7;
                }

                .show {
                    display: block;
                }
                
                .tooltip {
                        display: none;
                        position: absolute;
                        background-color: #333;
                        color: white;
                        padding: 5px;
                        border-radius: 5px;
                        z-index: 1;
                }


              a:hover + .tooltip {
              display: block;
               }

                
               
                 @media only screen and (max-width: 600px) {
        .project img[src*='chat.png'] {
            width: 100px;  
                }
                }
                
            </style>
        </head>
        <body>
            <div class="menu">
     <div class="dropdown">
        <button onclick="toggleServices()">Services ^</button>
        <div id="servicesDropdownContent">
            <a href="#" onmouseover="showTooltip('webDevelopmentTooltip')" onmouseout="hideTooltip('webDevelopmentTooltip')">Web Development</a>
            <span id="webDevelopmentTooltip" class="tooltip">Server Flask / Django | Backend Python</span>
            <a href="#">Automation Process with Python</a>
        </div>
    </div>
    <div class="dropdown">
        <button onclick="toggleContact()">Contact ^</button>
        <div id="contactDropdownContent">
            <a href="https://www.linkedin.com/in/elmer-urbina-meneses-290a3b208?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">LinkedIn</a>
            <a href="mailto:elmerurbina570@gmail.com">Email</a>
            <a href="https://github.com/elmerurbina">GitHub</a>
            <a href="https://t.me/elmerurbina">Telegram</a>
        </div>
    </div>
    <div class="dropdown">
        <button onclick="toggleLanguages()">Languages ^</button>
        <div id="languagesDropdownContent">
            <a href="https://learn.saylor.org/pluginfile.php/1/tool_certificate/issues/1675029197/0045648404EU.pdf">English</a>
            <a href="#" onmouseover="showTooltip('nativeLanguageTooltip')" onmouseout="hideTooltip('nativeLanguageTooltip')">Spanish</a>
            <span id="nativeLanguageTooltip" class="tooltip">Native Language</span>
        </div>
    </div>
</div>

        
            <div class="container">
                <h1>Elmer Urbina Meneses</h1>

                <div class="section about-me-section">
                    <h2>About Me</h2>
                    <p>I am Elmer Urbina Meneses, a passionate programmer currently studying at the <a href="https://uni.edu.ni/#/">National University of Engineering in Nicaragua.</a> My interest in programming stems from the desire to contribute to societal development and bring my ideas to life. I am focused on learning Python and aspiring to become a Python software engineer.</p>
                </div>

                <div class="section skills-discipline-section">
                    <h2>Skills and Discipline</h2>
                    {% for skill, level in skills.items() %}
                    <div class="skill">
                        <p>{{ skill }}</p>
                        <div class="progress">
                            <div class="progress-bar" style="width: {{ level }}%;">{{ level }}%</div>
                        </div>
                    </div>
                    {% endfor %}
                </div>

                <div class="section projects-section">
    <h2>Projects</h2>
{% for project in projects %}
<div class="project">
    <h3>{{ project['name'] }}</h3>
    {% if project['image'] == 'logo.jpg' %}
        <img src="{{ url_for('static', filename=project['image']) }}" alt="{{ project['alt'] }}" style="width: 300px; height: auto; margin-bottom: 20px;">
    {% endif %}
    <p>{{ project['description'] }}</p>
    {% if project['link'] %}
    <a href="{{ project['link'] }}">Visit Website</a>
    {% endif %}
    {% if project['image'] == 'chat.png' %}
    <img src="{{ url_for('static', filename=project['image']) }}" alt="Freud IA chat interface" style="display: block; margin: 0 auto; width: 300px; height: auto;">
    <p style="text-align: center;">As part of the system we have a chatbot which is trained to act as a human psychologist.</p>
    {% endif %}
</div>
{% endfor %}

</div>


                <div class="footer">
                    {{ footer_content | safe }}
                </div>
            </div>
            
            <script src="{{ url_for('static', filename='menu.js') }}"></script>

            
        </body>
        </html>
    """, skills=skills, projects=projects, footer_content=footer_content)


if __name__ == '__main__':
    app.run(debug=True)
