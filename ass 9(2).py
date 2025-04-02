HTML:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>US COLLEGE</title>
    <link rel="stylesheet" href="college.css">
</head>
<body>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzdOyMZ2wr3fSIFeUhETfxzJxgexP4V2-S8Q&s">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5dVUfAuSBb9pyZfAI6WeQL1bCtLWxWDF60Q&s"height="225">
    <header>
        <h1>US COLLEGE</h1>
        <nav>
            <ul>
                <li><a href="https://www.svnit.ac.in/web/about-us.php">About</a></li>
                <li><a href="https://www.shiksha.com/college/sardar-vallabhbhai-national-institute-of-technology-surat-24414/courses">Courses</a></li>
                <li><a href="https://svnit.ac.in/web/gallery.php">Gallery</a></li>
                <li><a href="https://mis.svnit.ac.in/mispay/formContact.aspx">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <section id="about">
        <h3>WELCOME</h3>
    </section>
    
    <section id="courses">
        <h2>Our Courses</h2>
        <ul>
            <li>Graphic Design</li>
            <li>Interior Design</li>
            <li>Fashion Design</li>
            <li>Web Design</li>
        </ul>
    </section>
    
    <section id="gallery">
        <h2>Gallery</h2>
        <div class="gallery">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSP6xjdjC70zbbcKdWiTFTtaf7VGTOp7TE1Fg&s" alt="NCC">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcfVsc6UZR0kwou_fQHrAONR0o4kFWDY-NbQ&s"height="200" alt="Sports">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9wptYx3f4kWdy4RVOsmHbxzrTeFouWzenZQ&s" alt="CLUBS">
        </div>
    </section>
    
    <section id="contact">
        <h2>Contact Us</h2>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            
            <button type="submit">Send</button>
        </form>
    </section>
    
    <footer>
        <p>Thankyou</p>
    </footer>
</body>
</html>



CSS:
body{
    background:linear-gradient(grey,white) ;
img{
    float:right;
}
}
