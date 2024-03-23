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
                    padding: 20px;
                   
                  
                }
                h2, h3 {
                    color: #F9F07A;
                    margin-top: 20px;
                    text-align: center;
                }
                h1 {
                    color: #FFF455;
                    margin-top: 20px;
                }
                
                p {
                    margin-left: 25%;
                    margin-right: 25%;
                    
                }
                
                a {
                    color: #000000;
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
                    margin-bottom: 10px;
                    margin-left: 25%;
                    margin-right: 25%;
                }
                .contact-section {
                    margin-top: 40px;
                }
            </style>
        </head>
        <body>
            <h1>Elmer Urbina Meneses</h1>

            <h2>About Me</h2>
            <p>I am Elmer Urbina Meneses, a passionate programmer currently studying at the <a href="https://uni.edu.ni/#/"> National University of Engineering in Nicaragua.</a> My interest in programming stems from the desire to contribute to societal development and bring my ideas to life. I am focused on learning Python and aspiring to become a Python software engineer.</p>

            <h2>Projects</h2>
            <ul>
                <li><strong>Freud IA:</strong> A psychologist project consisting of a general system for providing psychological attention to anyone around the world. <a href="https://elmerurbina.github.io/freud.ia">Visit our Website to learn more</a>
                <br>
                 <img src="/logo.jpg" alt="Freud IA Logo" style="display: block; margin: 0 auto;">
                    <p style="text-align: center;">Freud IA Logo</p>
                </li>
                <li><strong>FarmTech:</strong> A mobile app with a Django server for ganaderos (livestock farmers) where they can manage inventories, cow registrations, production, cost structures, production plans, etc.</li>
               
            </ul>

            <div class="contact-section">
                <h2>Contact Me</h2>
                <ul>
                    <li><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/elmer-urbina-meneses-290a3b208?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Elmer Urbina Meneses</a></li>
                    <li><strong>Telegram:</strong> <a href="https://t.me/elmerurbina">elmerurbina</a></li>
                    <li><strong>Email:</strong> <a href="mailto:elmerurbina570@gmail.com">Lets get in touch on Email</a></li>
                    <li><strong>GitHub:</strong> <a href="https://github.com/elmerurbina">lets contact on GitHub</a></li>
                </ul>
            </div>
        </body>
        </html>
    """)


if __name__ == '__main__':
    app.run(debug=True)
