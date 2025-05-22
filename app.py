from flask import Flask

app = Flask(__name__)

@app.route("/")
def love_story():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Our Love Story</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
        body {
          font-family: 'Montserrat', serif;
          margin: 0;
          background-color: black;
          color: gray;
          font-size: 16px;
          line-height: 1.7;
          word-break: break-word;
          padding-bottom: 60px;
        }

        nav {
          background-color: gray;
          overflow: hidden;
          display: flex;
          flex-wrap: wrap;
          justify-content: center;
        }

        nav a {
          color: black;
          padding: 14px 16px;
          text-decoration: none;
          font-weight: bold;
          display: block;
          text-align: center;
          flex-grow: 1;
          transition: background-color 0.3s;
        }

        nav a:hover {
          background-color: paleturquoise;
          color: black;
        }

        .page {
          display: none;
          padding: 40px 20px;
          max-width: 800px;
          margin: auto;
          animation: fadeIn 0.5s ease-in-out;
        }

        .active {
          display: block;
        }

        img, video, iframe {
          max-width: 100%;
          border-radius: 10px;
          margin-top: 20px;
        }

        h2 {
          text-align: center;
          font-size: 28px;
          margin-bottom: 20px;
        }

        p {
          margin-bottom: 20px;
          text-align: left;
        }

        @keyframes fadeIn {
          from {opacity: 0;}
          to {opacity: 1;}
        }

        @media (max-width: 600px) {
          nav {
            flex-direction: column;
            align-items: center;
          }

          nav a {
            width: 100%;
            padding: 12px 0;
            font-size: 15px;
          }

          .page {
            padding: 20px 15px;
          }

          h2 {
            font-size: 22px;
          }

          iframe {
            height: 120px;
          }
        }
      </style>
      <script>
        document.addEventListener("DOMContentLoaded", function () {
          const entered = sessionStorage.getItem("entered");
          const correctPassword = "pooks";

          if (!entered) {
            const attempt = prompt("Enter the password to view the page:");
            if (attempt !== correctPassword) {
              document.body.innerHTML = "<h2 style='text-align:center; padding:40px; color:white;'>Wrong password</h2>";
            } else {
              sessionStorage.setItem("entered", "true");
            }
          }
        });

        function showPage(pageId) {
          var pages = document.getElementsByClassName('page');
          for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
          }
          document.getElementById(pageId).classList.add('active');
        }
      </script>
    </head>
    <body>
      <nav>
        <a href="#" onclick="showPage('start')">Where it started</a>
        <a href="#" onclick="showPage('fell')">How we fell in love</a>
        <a href="#" onclick="showPage('outcome')">The outcome</a>
        <a href="#" onclick="showPage('now')">Where we are now</a>
        <a href="#" onclick="showPage('future')">What I hope the future brings us</a>
      </nav>

      <div id="start" class="page active">
        <h2>Where it started</h2>
        <p>
          We met under the most unexpected circumstances... and yet it felt like the universe conspired for us to find each other.<br><br>

          We met an August morning. August 7th of 2023 morning to be exact. As you know, I didn't have a big first impression of you, but I had a big second impression of you. When I saw you going through my front door that August 13th night I was amazed by your height and by your beauty. I started liking you that night. It was an immediate feeling, an immediate attraction.<br><br>

          When you told me to accompany you and Lia to the sociales party I was over the Moon. Fuck, I was going to a party with you. I was hoping something would happen, but it didn't and I'm so happy it turned out to be that way because our relationship wouldn't be what it is today if that had happened. Still, I had a great night and my feelings and attraction for you only grew stronger. Seeing you dance, seeing you owning that dance floor was a magical feeling I had never ever experienced before with someone I liked.
        </p>

        <img src="{{ url_for('static', filename='img_0473.jpeg') }}" alt="You and Lia at the Sociales Party">

        <p>
          Two days after, we went to the viewpoint together and that same night we went to a rave, my first rave ever! At the viewpoint, I realized how nice you were. Until that point, my impression of you was that you were a player and that you didn't have a lot of feelings. That day I noticed that you had a lot of feelings. You felt love, pain, sadness, happiness and many other things. I believe it was a bonding moment for us and I really enjoyed that time with you. After, we went to the rave. I fucking hated it, but I was happy to be there, because you were there.
        </p>

        <img src="{{ url_for('static', filename='img_0539.jpeg') }}" alt="Candid of you at the viewpoint">
        <img src="{{ url_for('static', filename='img_0551.jpeg') }}" alt="Lia handling that shot like a champ and well... you looking scared">

        <p>
          A few weeks later, we went through a little car crash together (I'm sorry!) and afterwards, we went to drink to the park. It was a magical night for me. We were just talking about everything and nothing at the same time. We were so high and laughing so much and I think it's one of the best memories I have with you here in Santiago.
        </p>

        <img src="{{ url_for('static', filename='img_0848.jpeg') }}" alt="You smoking your joint with a silly beach towel on your shoulders because we were SO cold">
        <img src="{{ url_for('static', filename='img_0835.jpeg') }}" alt="Beautiful afternoon">

        <p>
          One day we went to Sala Gente with Josefa. You know what happened there and that's the first time I saw you cry. It broke my heart into a million pieces. But seeing you being so vulnerable in front of me made me feel so, so honored. It made me feel special. It made me feel like I had won something in life.
        </p>

        <img src="{{ url_for('static', filename='burgir.png') }}" alt="You eating a McFlurry at McDonalds after Sala Gente">

        <p>
          Maitencillo... What a beautiful day. I remember I asked you a lot of questions. I wanted to know everything about you. Still, we didn't speak that much, but it was nice. Beautiful day, beautiful view and beautiful company.
        </p>

        <img src="{{ url_for('static', filename='img_1379.jpeg') }}" alt="Us at the beach looking happy and silly">
      </div>

      <div id="fell" class="page">
        <h2>How we fell in love</h2>

        <p>
          A month went by and I started noticing that you were... starting to have feelings for me? We met in San Pedro de Atacama and I realized that you were acting a tad different. It was almost noticeable, but I did notice. After, Christi invited us to her birthday party. That night, on our way back to your house, you hugged me in the car. You hugged me so, so tightly that I almost cried. I didn't know what to do. I was driving, I couldn't hug you with both of my arms, because we would crash. So I rested my head on your shoulder (we also could've crashed, but thankfully, we didn't).
        </p>

        <img src="{{ url_for('static', filename='christi.jpg') }}" alt="Christi's birthday">

        <p>
          The next day you texted me telling me that you were not feeling so good. I ran to your house and we went to Tobalaba. You had a joint, we stared at the cars and the traffic lights and we hugged. My feelings for you were so strong by then. I loved you so much already.
        </p>

        <img src="{{ url_for('static', filename='img_2652.jpeg') }}" alt="I asked the traffic lights if it'll be all right they said I don't know">

        <p>
          This is crazy, because Scott Street just came on while I was writing this... Anyway don't be a stranger.
        </p>

        <img src="{{ url_for('static', filename='img_2724.jpg') }}" alt="Don't be a stranger, okay?">

        <p>
          — I love you. No, I'm sorry, I shouldn't have said that.<br>
          — You can say it.<br>
          — Okay, I love you. Bye.<br>
          — Bye.
        </p>

        <div style="margin-top: 20px; margin-bottom: 20px;">
          <iframe style="border-radius:12px"
            src="https://open.spotify.com/embed/track/21uFPefbgeR3QLVJWATlrr"
            width="100%" height="152" frameborder="0" allowfullscreen=""
            allow="clipboard-write; encrypted-media; fullscreen; picture-in-picture"
            loading="lazy">
          </iframe>
        </div>

        <p>
          Then Mendoza came... It was actually out of a movie. The drama with my friends, the lying, the being trapped for almost one week outside of Santiago, the fighting with my mom in the car, everything. But you know what? It was fucking worth it. SO. WORTH. IT. I would do it all over again, 100 times if it's necessary, if it means that I'll be with you.
        </p>

        <p>
          Our first kiss was magical. Time stopped for a second, at least for me. I had been waiting months for it and it was finally happening. I was so, so, so into you. As cliche as it sounds, and I'm so sorry for how cringe this will sound, I felt fireworks the moment my lips touched yours. The conversation we had after that, the Lia situation, everything was out of a movie.
        </p>

        <img src="{{ url_for('static', filename='besito.jpg') }}" alt="Our first photo after our first kiss">

        <p>
          I told you that I loved you pretty early on our relationship, huh? Hahaha. I remember, it was in the second Airbnb. We were in bed and I told you "I don't care if you don't say it back, but I love you." I said it because I felt it and I really couldn't hold it back. My feelings for you were so strong right from the start (they still are).
        </p>

        <img src="{{ url_for('static', filename='camita.jpg') }}" alt="Us laying in bed in the second Airbnb">

        <p>
          When we got back to Santiago, we "hid" our relationship. We went on a silly little hike together. Hated the hike, loved the company and the river. I actually look back and I absolutely loved and hated this time. I loved the fact that I was with you, basically living my dream, but I hated the fact that I had to hide the fact that I was head over heels for you because of the Lia factor. Everyone knew though, because it was visible from 1000 kilometers away, but still. I wanted to scream it. But well, you were going to leave in 1 month and our relationship was going to end, so what was the point anyway? We were not going to be together.
        </p>

        <img src="{{ url_for('static', filename='img_3859.jpg') }}" alt="Our hike together">
        <img src="{{ url_for('static', filename='img_4598.jpeg') }}" alt="Silly, silly, silly girls">
      </div>

      <div id="outcome" class="page">
      <h2>The outcome</h2>

      <p>
        Even though you left, we became something real and rare. Something that, no matter what happens, no matter if we break up now, in 1 year or in 10 more years, will leave a mark, a huge mark that won't fade, at least for me.
      </p>

      <p>
        First of all, we went to Costa Rica together. I always wonder what people thought about us. If you think about it, it was actually CRAZY. We hadn't been together for more than 3 months and we were traveling to Central America together. CRAZY.
      </p>

      <img src="{{ url_for('static', filename='img_5022.jpeg') }}" alt="Costa Rica 1">
      <img src="{{ url_for('static', filename='img_4993.jpeg') }}" alt="Costa Rica 2">
      <img src="{{ url_for('static', filename='img_4953.jpeg') }}" alt="Costa Rica 3">

      <p>
        Then you returned to The Netherlands. I suffered a lot. I missed you and I thought that our relationship was ending. I did some stupid things I deeply regret because they hurt me and you. And then, one day, you asked me to be your girlfriend. I was so, so happy. I was your girlfriend. I felt so honored to be your girlfriend. Knowing that you had gone through a lot of horrible situations in your life, you choosing me as your partner meant that you trusted me a lot and that means so much to me. It makes me want to cry just thinking about it.
      </p>

      <p>A lot of smoking sessions came after that.</p>
      <img src="{{ url_for('static', filename='img_8946.jpg') }}" alt="Smoking sesh">

      <p>Some crying sessions too...</p>
      <img src="{{ url_for('static', filename='img_7678.jpg') }}" alt="Crying sesh">

      <p>And, finally... our first reunion :)</p>
      <img src="{{ url_for('static', filename='maas.jpg') }}" alt="You look so peaceful in this one">
      <img src="{{ url_for('static', filename='fujifilm.jpg') }}" alt="Pretty girl">

      <p>
        I was so happy to see you. I was with my <em>*clears throat*</em> GIRLFRIEND after 6 years of being apart. I would've never thought we would've stayed together more than 2 months (wupsies), but we did, and I couldn't be happier. I got to travel to Barcelona, I got to meet your friends and I felt so accepted by them and I loved that. I felt at home.
      </p>

      <p>
        But it was time to say goodbye, again... lots of crying at the airport, lots of crying on the plane. I didn't know if I was going to see you again. Was our relationship going to survive? But it did survive and after 5 months, we saw each other again. You picked me up at the airport with a heart balloon.
      </p>

      <img src="{{ url_for('static', filename='img_5179.jpeg') }}" alt="YOU WITH A HEART BALLON!">

      <p>
        And I'd never felt more in love in my whole life. I fucking love you Izzy, so much. My heart feels like it's about to explode every single time I'm near you or even talking to you over the phone.
      </p>

      <img src="{{ url_for('static', filename='img_5224.jpeg') }}" alt="Lesbians...">
      <img src="{{ url_for('static', filename='img_5348.jpg') }}" alt="We look so happy">
      <img src="{{ url_for('static', filename='img_2227.jpeg') }}" alt="Mistery baggy">

      <p>
        Just two weeks until I went back to Santiago and you received the news of your mom. We cried together and I didn't want to leave you. I wanted to stay with you. I wanted to drop uni, I wanted to make you company during this horrible time for you. But, sadly, I couldn't. As much as I wanted to, I couldn't because the fear of disappointing my parents and, also, the fear of having lost 5 years of my life was too big. So I came back to Santiago.
      </p>

      <img src="{{ url_for('static', filename='img_6614.jpeg') }}" alt="Airport">

    </div>


    <div id="now" class="page">

      <h2>Where we are now</h2>

      <img src="{{ url_for('static', filename='img_7712.png') }}" alt="Distance">

      <p>
        My heart aches every time I think about you. My heart aches when I think about you crying alone in your apartment, and I feel so useless 12,000 kilometers away from you... I wish I were there. I wish I could make your life easier by just doing your dishes every morning. But I can't, and it breaks me.
      </p>

      <p>
        You're struggling so much more than we thought, and I can't begin to imagine how horrendous that must be. I just want you to know that I notice you. I see you and I can see your pain. I see that you're struggling. You are noticed, at least by me.
      </p>

      <p>
        I'm sorry for the times you've felt unseen by me. I'm sorry for the times I've noticed you're upset and I haven't said anything.
      </p>

      <p>
        We've grown through so much together. We're stronger, wiser, and still connected in the most beautiful ways possible. And I'll always be deeply grateful for that with you.
      </p>

      <p>
        Just know that I've never loved anyone the way that I love you. You're the one I love and the one I want to love for the rest of my life. I don't want to hate you and that's why, if loving you for the rest of my life means that I have to lose you, I'm willing to accept that.
      </p>
    </div>
     
    <div id="future" class="page">
      <h2>What I hope the future brings us</h2>

      <p>
        I really don't know what the future will bring us, so I don't know what my hopes are... I just hope love, for both of us. Love and happiness. You deserve that — and me too.
      </p>

      <p>
        Learn to forgive, to forget. To live, even if it's fucking hard sometimes.
      </p>

      <p>
        Just know that I will always love you.
      </p>

      <p>
        <em>That's what I hope the future will bring you. That you know that I'll always love you.</em>
      </p>

      <img src="{{ url_for('static', filename='img_6479.jpeg') }}" alt="What I hope for us">

      <p style="margin-top: 30px;">
        With love,<br>
        <strong>Catalina Paz Muga Vaccarella</strong>
      </p>
    </div>

      <script>
        function showPage(pageId) {
          var pages = document.getElementsByClassName('page');
          for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
          }
          document.getElementById(pageId).classList.add('active');
        }

        function submitMessage() {
          var message = document.getElementById("messageInput").value;
          if (message.trim() === "") {
            alert("Please write something first!");
            return;
          }
          document.getElementById("submitted-message").innerHTML = "<strong>Your message:</strong><br>" + message;
          document.getElementById("messageInput").value = "";
        }
      </script>

    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(debug=True)
