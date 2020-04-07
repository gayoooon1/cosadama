# [HTML] HTML Document Standards

Created: Apr 07, 2020 8:17 PM
Property: Ka Yoon Kim
Tags: HTML

# 🐣 HTML Document Standards

---

## 1. Preparing for HTML

- `!<DOCTYPE html>`은 html 문서의 가장 첫 번째로 와야하는 문장. 문서로 쓰인다는 뜻이며, 마지막에 html 확장자로 파일에 저장된다. 브라우저에게 두 가지 정보 제공 : 나는 문서고, html이야~ 하지만 구조나 내용을 포함하진 않는다.
- `html` tag는 앞 태그 선언한 뒤에 선언하며, opening & closing 필수, 안의 내용은 html code. html tag가 없으면 내가 쓴 코드들을 제대로 인식할 수 없다.

    <!DOCTYPE html>
    <html>
    
    </html>
    

## 2. The Head

Now, let’s also give the browser some information about the page itself. We can do this by adding a 

- `<head>` element : 브라우저에게 페이지 정보를 넘겨준다.
- `<body>` element 위에 선언
- `<head>` 웹 페이지의 메타 데이터(웹페이지에 나와있지 않은 정보들)를 포함, 페이지 자체를 위한 정보를 가지고 있다.

## 3. The Page Titles

- Web Page's Title `<title>`
- 브라우저 새 탭 윗부분에 보이는 제목이다!

    <!DOCTYPE html>
    <html>
      <head>
        <title>My Coding Journal</title>
      </head>
    </html>
    

## 4. Linking to ~

### 1. Other Web Pages

- `<a>` 를 통해 다른 웹 페이지를 연결할 수 있다. opening, closing MANDATORY
- `href` = *hyperlink*, *URLs*

    <a href="https://www.wikipedia.org/">This Is A Link To Wikipedia</a>
    

### 2. Opening Links in a New Window

- Use `<target>="_blank"`

### 3. Linking to Relative Pages

- If the files are stored in the same folder, we can link web pages together using a relative path.
- `./` 현재 폴더에 있다는 것을 말한다.
- Relative path 추가할 때 : `<a href ="./aboutme.html>About Me</a>`

### 4. Linking At Will

- HTML은 이미지를 링크로 변환할 수 있다.
- How? By simply wrapping the `<img>` element with an `<a>` element.

    <a href="https://en.wikipedia.org/wiki/Opuntia" target="_blank"><img src="https://www.Prickly_Pear_Closeup.jpg" alt="A red prickly pear fruit"/></a>
    

In the example above, an image of a prickly pear has been turned into a link by wrapping the outside of the `<img>` element with an `<a>` element.

### 5. Linking to Same Page

- 내용이 너무 많다! 다른 부분에서 이 창을 열게 하고 싶다. → `<target>`
- Target in link → id 사용해야 잘 알아볼 수 있음!
- The target link is a string containing the # character and the target element’s id.
- 내가 설정해놓은 div의 id와 같아야 그 링크가 만들어지고 같은 페이지 내에서 이동할 수 있는듯

> The rest of following contents will focus on some tools developers use to make code easier to interpret.

## 6. Whitespace & Indentation

## 7. Comments

- Comments are written in HTML using the following syntax: `<!-- comment -->`

## 8. Codes

    <!DOCTYPE html>
    <html>
    
    <head>
      <title>Brown Bears</title>
    </head>
    
    <body>
      <a href="./index.html">Brown Bear</a>
      <a href="./aboutme.html">About Me</a>
      <h1>The Brown Bear</h1>
      <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#habitat">Habitat</a></li>
        <li><a href="#media">Media</a></li>
      </ul>
      <div id="introduction">
        <h2>About Brown Bears</h2>
        <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern</strong>.<br /><br /> There are many subspecies within the brown bear species, including the
          Atlas bear and the Himalayan brown bear.</p>
        <a href="https://en.wikipedia.org/wiki/Brown_bear" target="_blank">Learn More</a>
        <h3>Species</h3>
        <ul>
          <li>Arctos</li>
          <li>Collarus</li>
          <li>Horribilis</li>
          <li>Nelsoni (extinct)</li>
        </ul>
        <h3>Features</h3>
        <p>Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe.</p>
      </div>
      <div id="habitat">
        <h2>Habitat</h2>
        <h3>Countries with Large Brown Bear Populations</h3>
        <ol>
          <li>Russia</li>
          <li>United States</li>
          <li>Canada</li>
        </ol>
        <h3>Countries with Small Brown Bear Populations</h3>
        <p>Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.</p>
      </div>
      <div id="media">
        <h2>Media</h2>
        <a href="https://en.wikipedia.org/wiki/Brown_bear" target="_blank"><img src="https://s3.amazonaws.com/codecademy-content/courses/web-101/web101-image_brownbear.jpg"/></a>
        <video src="https://s3.amazonaws.com/codecademy-content/courses/freelance-1/unit-1/lesson-2/htmlcss1-vid_brown-bear.mp4" height="240" width="320" controls>Video not supported</video>
      </div>
    </body>
    
    </html>