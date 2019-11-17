---
title: Password Generator
featured_image: '/images/blog/2019-08-19_password_generator_js/UI.png'
exerpt: A password generator made with javascript
---

This is a simple single-page password generator made with HTML, CSS, and Javascript. 

![](/images/blog/2019-08-19_password_generator_js/all_types.png)

It features an intuitive interface that allows the user to select the length of password generated, as well as if the password is allowed to contain uppercase letters, lowercase letters, numbers, or symbols. Once the user clicks the Generate Password button the password appears in the text box and the user is able to copy it to their clipboard with a single click.


I made this after seeing a video by [Brad Traversy](https://www.youtube.com/channel/UC29ju8bIPH5as8OGnQzwJyA) about one of [Florin Pop](https://www.florin-pop.com)'s 100days100projects projects - a password generator.

In the above versions, you have the following pattern: lowercase, uppercase, number, symbol. My version does not have this pattern, instead, the type of each character is chosen randomly and then a random character of that type is drawn. This means that my version creates a slightly stronger password for the given length.

