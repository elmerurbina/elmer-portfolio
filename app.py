from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/elmer')
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
                    color: #DFF5FF;
                    font-family: Arial, sans-serif;
                    line-height: 2.0;
                }

                .section {
                    padding: 20px;
                    margin: 20px;
                    border-radius: 10px;
                    max-width: 50%;
                    transition: max-width 0.5s;
                    align-items: center;
                    display: flex;
                    flex-direction: column;
                    margin: 0 auto;
                    margin-top: 100px;
                }

                .section:hover {
                    max-width: 75%;
                }

                .about-me-section {
                    background-color: #0F3057;
                }
                
                .skills-discipline-section {
                    background-color: #195EBA; 
                    padding: 30px;
                  
                }

                .skills-discipline-section h2 {
                    color: #F9F07A; /* Yellow */
                    margin-bottom: 20px;
                }

                .skills-discipline-section p {
                    margin: 0 auto;
                    max-width: 60%;
                    line-height: 1.5;
                }

                .projects-section {
                    background-color: #1D4E8F;
                }

                .contact-section {
                    background-color: #2A6ABE;
                }
                
                 .footer {
                    text-align: center;
                    margin-top: 50px;
                    color: #FFF;
                }

                h1 {
                    color: #FFF455;
                    margin-top: 20px;
                }
                h2, h3 {
                    color: #F9F07A;
                    margin-top: 20px;
                    text-align: center;
                }
                p {
                    margin-left: 25%;
                    margin-right: 25%;
                    line-height: 1.5;
                }
                a {
                    color: #16FF00;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                    text-align: left;
                }
                li {
                    margin-bottom: 20px;
                    margin-left: 25%;
                    margin-right: 25%;
                }
                .contact-section {
                    margin-top: 40px;
                    text-align: center;
                }
                .icon {
                    margin-right: 10px;
                }

                /* Media query for small screens */
                @media only screen and (max-width: 600px) {
                    .section {
                        max-width: 90%;
                    }
                }
            </style>
        </head>
        <body>

        <h1>Elmer Urbina Meneses</h1>
        <div class="section about-me-section">
            <h2>About Me</h2>
            <p>I am Elmer Urbina Meneses, a passionate programmer currently studying at the <a href="https://uni.edu.ni/#/">National University of Engineering in Nicaragua.</a> My interest in programming stems from the desire to contribute to societal development and bring my ideas to life. I am focused on learning Python and aspiring to become a Python software engineer.</p>
        </div>

        <div class="section skills-discipline-section">
            <h2>Skills and Discipline</h2>
            <p>I possess intermediate skills in Python, and basic knowledge in Java, HTML, CSS, and JavaScript. Additionally, I have intermediate proficiency in Flask and basic understanding of Django. I am dedicated to continuously improving my programming skills and strive to excel in every project I undertake. My disciplined approach to work ensures that I meet deadlines and deliver high-quality results consistently.</p>
        </div>

        <div class="section projects-section">
            <h2>Projects</h2>
            <ul>
                <li>
                    <strong>Freud IA:</strong> A psychologist project consisting of a general system for providing psychological attention to anyone around the world. <a href="https://elmerurbina.github.io/freud.ia">Visit our Website to learn more</a><br>
                    <img src="{{ url_for('static', filename='logo.jpg') }}" alt="Freud IA Logo" style="display: block; margin: 0 auto;" width="200" height="200">
                    <p style="text-align: center;">Freud IA Logo</p>
                    
                    <img src="{{ url_for('static', filename='chat.png') }}" alt="Freud IA chat interface" style="display: block; margin: 0 auto;" width="400" height="200">
                    <p style="text-align: center;">As part of the system we have a chatbot which is trained to act as a human psychologist.</p>
                </li>
                <li>
                    <strong>FarmTech:</strong> A mobile app with a Django server for ganaderos (livestock farmers) where they can manage inventories, cow registrations, production, cost structures, production plans, etc.
                </li>
            </ul>
        </div>

        <div class="section contact-section">
            <h2>Contact Me</h2>
            <ul>
                <li><span class="icon">🔗</span><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/elmer-urbina-meneses-290a3b208?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Elmer Urbina Meneses</a></li>
                <li><span class="icon">✉️</span><strong>Email:</strong> <a href="mailto:elmerurbina570@gmail.com">Lets get in touch on Email</a></li>
                <li><span class="icon">🐙</span><strong>GitHub:</strong> <a href="https://github.com/elmerurbina">lets contact on GitHub</a></li>
            </ul>
        </div>
        
         <div class="footer">
          <p>Second Place Winner in the Web Pages category at Feria Nacional de Ciencia y Tecnologia UNI. Our project is featured as image number 6 in the post. <a href="https://www.facebook.com/share/p/GUBJwDLNdAYXGtab/?mibextid=xfxF2i">See the post</a>. Collaborated with two other team members.</p>

        </div>
        
        </body>
        </html>
    """)


if __name__ == '__main__':
    app.run(debug=True)
