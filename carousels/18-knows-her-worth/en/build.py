src = open('../../15-podcast-quote-6/carousel.html', encoding='utf-8').read()
head = src[:src.index('<section')]
# smaller text like the reference, wider lines so long lines don't climb onto the face
head = head.replace('</style>', '.t{font-size:46px!important;max-width:980px!important;line-height:1.4!important}</style>')
S = [("e", "f", "A woman who knows her worth", "doesn&rsquo;t wait to be chosen."),
     ("a", "b", "Not by a man. Not by a company.", "Not by a manager who decides when she deserves a raise."),
     ("c", "d", "But most of us were raised the opposite way.", "Be good. Be quiet. Wait your turn."),
     ("f", "a", "So you stay in the job that underpays you.", "You keep your dream in your notes app. And you call it being realistic."),
     ("b", "e", "It&rsquo;s not being realistic.", "It&rsquo;s fear with a nice name."),
     ("d", "c", "Security isn&rsquo;t a salary.", "Security is knowing you can make money on your own."),
     ("a", "e", "Most women already have something people would pay for. Their skills. Their story. Their experience.", "They just don&rsquo;t know how to turn it into income."),
     ("f", "b", "That&rsquo;s exactly what I help women do in 90 days.", "Comment &ldquo;BRAND&rdquo; and I&rsquo;ll send you how.")]
pos = {'a': 'center 40%', 'b': 'center 40%', 'c': 'center 40%', 'd': 'center 40%', 'e': 'center 35%', 'f': 'center 35%'}
body = ''.join(f'''<section class="slide">
<div class="half" style="background-image:url(photos/{p}.jpg);background-position:{pos[p]}"><p class="t">{t1}</p></div>
<div class="half" style="background-image:url(photos/{q}.jpg);background-position:{pos[q]}"><p class="t">{t2}</p></div>
</section>''' for p, q, t1, t2 in S)
open('carousel.html', 'w', encoding='utf-8').write(head + body + '</body></html>')
