# [CSS] CSS Setup and Selectors

Created: Apr 07, 2020 8:17 PM
Property: Ka Yoon Kim
Tags: CSS, HTML

# 1. Intro to CSS

- CSS (Cascading Style Sheets) 은 웹페이지에 HTML 문서들을 **꾸미기 위한** 언어
- If you’re interested in modifying colors, font types, font sizes, shadows, images, element positioning, and more, CSS is the tool for the job! = STYLING LANGUAGE!

# 2. Inline Styles

- 꾸미기 위해선 opening tag에 `style` 써주고, 선언뒤에는 `;` **semicolon**을 잊지말 것!

    <p style="color: red;">I'm learning to code!</p>

- Inline styles는 직접적으로 빠르게 html 요소들을 꾸며주는 방법이다.

# 3. The `<style>` Tag

- lnline style의 단점을 보완한 tag
- `<head>`안에 위치해야 한다.

    <head>
    <style>
      p {
        font-family: Arial;
      } #이로써 모든 p에 같은 폰트 적용! 일일히 안써줘도 됨.
      <title>Vacation World</title>
    </style>
    </head>

# 4. The .css file

- CSS 확장자를 통해 따로 파일을 만들어 html 파일 코드와의 혼선을 막아준다.

# 5.  Linking the CSS File

- 구별한 css file은 html file과 연결해야 스타일링이 적용된다. 이 때 `<link>`를 이용한다.
    - `<link>`
    - self closing tag, 3 attributes
        1. `href` — like the anchor element(`<a>`), **the value of this attribute must be the address, or path**, to the CSS file. 저번에 배웠던 하이퍼링크
        2. `type` — this attribute describes **the type of document** that you are linking to (in this case, a CSS file). The value of this attribute should be set to `text/css`.
        3. `rel` — this attribute describes **the relationship between the HTML file and the CSS file.** Because you are linking to a stylesheet, the value should be set to `stylesheet`. stylesheet도 url!
- 만약 css file이 html file과 동일한 폴더에 있으면 `href = ""./style(파일명).css""` 으로 선언

# 6. Tag Name

- Note that the **CSS selector matches the HTML tag for that element**, but without the angle brackets. ({} css 파일에 추가해야)
- ex. p, h1 etc

# 7. `<class>`

- class 선언 후, 그 class에 해당하는 style로 바꿀 수 있음 (기억할 때: class로 붕어빵틀 모양을 만들어놨다고 생각하고 그것을 선언하면 붕어빵이 그 모양으로 바뀐다는 느낌=MODULE)

    <p class="brand">Sole Shoe Company</p>
    .
    .
    .
    
    .brand {
    
    
    } 

- **Multiple Classes**

    .title { 
     color: teal;
    }
    
    .uppercase {
      text-transform: uppercase;
    }

# 8. ID Name

- **If an HTML element needs to be styled uniquely** (no matter what classes are applied to the element), we can add an ID to the element.

    /*in css file*/
    #large-scale{
    
    }
    
    /*in html file*/
    <p id="large-scale">...</p>

# 9. Chaining Selectors

- For instance, if there was a `.special` class for `h1` elements, the CSS would look like:

    h1.special {
    
    }

The code above would select **only the `h1` elements** that have a class of `special`. If a `p` element also had a class of `special`, the rule in the example would not style the paragraph.