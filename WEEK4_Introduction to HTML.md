# 🐣Introduction to HTML

Created: Apr 07, 2020 8:17 PM
Property: Ka Yoon Kim
Tags: HTML

# What is html?

---

1. HTML provides structure to the content appearing on a website, such as images, text, or videos.
2. HTML stands for HyperText Markup Language:
*A markup language = a computer language that defines the structure and presentation of raw text.
*In HTML, the computer can interpret raw text that is wrapped in HTML elements.
*HyperText = text displayed on a computer or device that provides access to other text through links.
*마크업: 텍스트 변환해주는 컴퓨터 언어 하이퍼텍스트: 누르면 링크로 타고 이동 (하이퍼링크!)

# HTML Anatomy

---

1. One opening tag `<p>`
2. The content (“Hello World!” text)
3. A closing tag `</p>`
4. *A tag and the content between it is called an HTML element. (1,2,3 전체)*

# The Body

---

1. Body tags 사이에 있는 내용들만 보인다. 사진, 글 등 유형이 다양하다.
2. Body tags = `<body> <p> </p> </body>`

# HTML Structure

---

## 1. HTML Hierarchy

부모, 자식 간 관계를 잘 파악하고 있어야 한다.

    <body> //Parent Element
      <p>This paragraph is a child of the body</p> //Child Element
    </body>
    
    

## 2. Heading Elements

    <body>
      <h1>The Brown Bear</h1>
      <h2>About Brown Bears</h2>
      <h3>Species</h3>
      <h2>Habitat</h2>
      <h3>Features</h3>
    </body>
    

## 3. Div Elements

Use for **grouping**, `<div>` elements can contain flow content such as headings, paragraphs, links, images, etc.

    <div>
      <h1>A section of grouped elements</h1>
      <p>Here’s some text for the section</p>
    </div>
    <div>
      <h1>Second section of grouped elements</h1>
      <p>Here’s some text</p>
    </div>
    

## 4. HTML Attributes

HTML attributes are values added to the opening tag of an element to configure the element or change the element’s default behavior. Div, body 등의 특성

    <p id="my-paragraph" style="color: green;">Here’s some text for a paragraph that is being altered by HTML attributes</p>
    

## 5. Paragraph Element `<p>`

The `<p>` paragraph element = a block of text.

## 6. Span Element `<span>`

The <span> element is an inline container for text and can be used to to separate pieces of text from a larger body of text, its use should be avoided if a more semantic element is available.

## 7. Emphasis Element `<em>`

The <em> emphasis element emphasizes text and browsers will usually italicize the emphasized text by default.
*글씨가 휘날리게 강조해줍니다*

    ```
    <p>This <em>word</em> will be emphasized in italics.</p>
    ```
    

## 8. Strong Element `<strong>`

**bold**체로 표시해줍니다.

## 9. Line Break Element `<br>`

    A line break haiku.<br>
    Poems are a great use case.<br>
    Oh joy! A line break.
    

## 10. List contained Elements `<ul>, <ol>, <li>`

1. Unordered List Element `<ul>`
2. Ordered List Element `<ol>`
3. List Item Element `<li>` create list items inside: Ordered lists `<ol>`, Unordered lists `<ul>`

    <ol>
      <li>Head east on Prince St</li>
      <li>Turn left on Elizabeth</li>
    </ol>
    

    <ul>
      <li>Cookies</li>
      <li>Milk</li>
    </ul>
    

---

이미지와 비디오 넣기는 코드 참조

    <body>
      <h1>The Brown Bear</h1>
      <div id="introduction">
        <h2>About Brown Bears</h2>
        <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern</strong>.<br /><br /> There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear.</p>
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
        <img src="<https://content.codecademy.com/courses/web-101/web101-image_brownbear.jpg>" alt="A Brown Bear"/>
        <video src="<https://content.codecademy.com/courses/freelance-1/unit-1/lesson-2/htmlcss1-vid_brown-bear.mp4>" width="320", height="240" controls>Video not supported</video>
      </div>
    </body>
