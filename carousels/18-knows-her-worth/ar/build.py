src = open('../../15-podcast-quote-6/carousel.html', encoding='utf-8').read()
head = src[:src.index('<section')].replace('lang="en" dir="ltr"', 'lang="ar" dir="rtl"')
head = head.replace('</style>', '.t{font-size:48px!important;max-width:980px!important;line-height:1.5!important}</style>')
S = [("e", "f", "البنت اللي عندها دخلها الخاص", "ما حدا بيقدر يتحكم فيها."),
     ("a", "b", "لا شخص معين.", "ولا مدير بيقرر إمتى بتستاهل زيادة بالراتب."),
     ("c", "d", "بس أغلبنا تربينا على العكس.", "كوني لطيفة، كوني هادية، واستني دورك."),
     ("f", "a", "فبتضلي بشغل ما بيعطيكي حقك.", "وحلمك بيبقى كلام على ورق."),
     ("d", "c", "الأمان مو راتب بينزل كل شهر.", "الأمان إنك تعرفي تعملي دخلك بنفسك."),
     ("a", "e", "أغلب البنات عندهن أصلا شي الناس مستعدة تدفع مقابله: مهاراتهن، قصتهن، خبرتهن.", "بس ما بيعرفوا كيف يحولوه لدخل."),
     ("f", "b", "إذا عندك مهارة، خبرة، وجاهزة إنك تحوليها لدخل خلال ٩٠ يوم", "علقي بكلمة &laquo;براند&raquo;")]
pos = {k: 'center 40%' for k in 'abcd'} | {'e': 'center 35%', 'f': 'center 35%'}
body = ''.join(f'''<section class="slide">
<div class="half" style="background-image:url(../en/photos/{p}.jpg);background-position:{pos[p]}"><p class="t">{t1}</p></div>
<div class="half" style="background-image:url(../en/photos/{q}.jpg);background-position:{pos[q]}"><p class="t">{t2}</p></div>
</section>''' for p, q, t1, t2 in S)
open('carousel.html', 'w', encoding='utf-8').write(head + body + '</body></html>')
