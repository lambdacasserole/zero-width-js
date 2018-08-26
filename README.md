# Zero-Width JS
Proof-of-concept for an 'invisible' JavaScript payload.

## Overview
It's possible to encode JavaScript as zero-width unicode characters and have it execute on page load. This is going to make it much harder to pick out potential malware by eye because most editors don't even show these characters:

| Name                  | Codepoint | Character (between `][`)     |
|-----------------------|-----------|------------------------------|
| ZERO WIDTH SPACE      | U+200B    | \]&#8203;\[                  |
| ZERO WIDTH NON-JOINER | U+200C    | \]&#8204;\[                  |
| ZERO WIDTH JOINER     | U+200D    | \]&#8205;\[                  |

The demo works by using these characters to encode a JavaScript payload in binary (`\u200c` and `\u200d` representing `0` and `1` and `\u200b` separating bytes). When the page loads, a little bit of code decodes this to ASCII and appends it to the page in the `onload` event handler of an `img` element. If you open up the code in most editors, all you will see is an empty string.

## Your Own Payloads
You can generate your own page with your own custom 'invisible' script using the files in `/src/generator`. Pipe the JavaScript you'd like to embed to the `genpage.sh` script like this:

```bash
echo "alert('Its free real estate!')" | bash genpage.sh > mypage.html
```

You'll obtain mypage.html which will show an alert, but try finding the alert code in the source!

## But Why, Though?
I've done a little bit of a write-up [on my blog](https://blog.sauljohnson.com/you-will-pwn-yourself-with-your-own-clipboard) about this to highlight why copying and pasting code from the internet isn't a great idea. If you come across code on the internet, without careful examination it's entirely possible to end up pasting 'invisble' malware into your projects.
