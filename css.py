
import os

def clear_terminal():
    # Terminalni tozalash
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    groups = {
        1: "Matn va Shrifts (Text & Font)",
        2: "Ranglar va Orqa fon (Colors & Background)",
        3: "Qutini boshqarish (Box Model)",
        4: "Joylashuv (Positioning)",
        5: "Layoutlar (Flexbox va Grid)",
        6: "Animatsiyalar va O‘tishlar (Animations & Transitions)",
        7: "Jadval elementlari (Table Properties)",
        8: "Foydalanuvchi bilan muloqot elementlari (User Interaction)",
        9: "Media Queries va Responsiv Dizayn"
    }

    while True:
        print("\nGuruhlar ro'yxati:")
        for key, value in groups.items():
            print(f"{key}. {value}")

        choice = input("1 dan 9 gacha raqam kiriting (0 - chiqish): ")
        
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                print("Dasturdan chiqyapsiz...")
                break
            elif 1 <= choice <= 9:
                display_group_info(choice)
                input("Davom etish uchun Enter tugmasini bosing...")
                clear_terminal()  # Enter bosilganda terminalni tozalash
            else:
                print("Iltimos, 1 dan 9 gacha raqam kiriting.")
        else:
            print("Iltimos, raqam kiriting.")

def display_group_info(group_number):
    info = {
        1: """
        Matn va Shrifts (Text & Font):
        1. color: Matn rangini belgilaydi (masalan, color: red;).
        2. text-align: Matnni gorizontal joylashtirish (left, right, center, justify).
        3. text-decoration: Matnga chiziq qo‘shadi yoki olib tashlaydi (none, underline, line-through, overline).
        4. text-decoration-line: Chiziq turini belgilaydi (xuddi text-decoration kabi).
        5. text-decoration-color: Matn chizig‘i uchun rangni belgilaydi.
        6. text-decoration-style: Chiziq uslubini belgilaydi (solid, dotted, dashed, double, wavy).
        7. text-underline-position: Ost chiziqning joylashuvini sozlaydi (auto, under, left, right).
        8. text-indent: Birinchi qatorni chekinishini aniqlaydi (masalan, text-indent: 20px;).
        9. text-transform: Matnni katta, kichik yoki bosh harflarga aylantiradi (capitalize, uppercase, lowercase, none).
        10. letter-spacing: Harflar orasidagi masofani belgilaydi (masalan, letter-spacing: 2px;).
        11. word-spacing: So‘zlar orasidagi masofani belgilaydi (masalan, word-spacing: 5px;).
        12. line-height: Qatorlar orasidagi masofani aniqlaydi (masalan, line-height: 1.5;).
        13. direction: Matn yo‘nalishini belgilaydi (ltr yoki rtl).
        14. white-space: Bo‘sh joylarni boshqaradi (normal, nowrap, pre, pre-wrap, pre-line).
        15. overflow-wrap: So‘zlarning kesilish usulini belgilaydi (normal, break-word).
        16. text-shadow: Matnga soya qo‘shadi (masalan, text-shadow: 1px 1px 2px black;).

        Font Properties:
        1. font-family: Shrift turini belgilaydi (masalan, font-family: Arial, sans-serif;).
        2. font-size: Shrift o‘lchamini aniqlaydi (masalan, font-size: 16px;).
        3. font-size-adjust: Shrift balandligini boshqaradi.
        4. font-stretch: Shriftni kengaytirish yoki toraytirishni belgilaydi (normal, condensed, expanded).
        5. font-style: Shrift uslubini aniqlaydi (normal, italic, oblique).
        6. font-variant: Shriftning maxsus variantini belgilaydi (normal, small-caps).
        7. font-variant-caps: Bosh harflar formatini belgilaydi (normal, all-small-caps, petite-caps).
        8. font-weight: Matnning qalinligini belgilaydi (normal, bold, 100–900 oralig‘ida).
        9. font-kerning: Harflar orasidagi masofani avtomatik boshqaradi (auto, normal, none).
        10. font-feature-settings: Maxsus shrift xususiyatlarini sozlaydi.
        11. font: Shrift xususiyatlarini birlashtiruvchi qisqa yozuv (masalan, font: italic bold 16px Arial;).
        """,
        
        2: """
        Ranglar va Orqa fon (Colors & Background):
        Color Properties:
        1. color: Matn rangini belgilaydi (masalan, color: blue;).
        2. opacity: Elementning shaffoflik darajasini aniqlaydi (masalan, opacity: 0.5;).

        Background Properties:
        1. background: Orqa fon xususiyatlarini birlashtiruvchi qisqa yozuv (masalan, background: red;).
        2. background-color: Orqa fon rangini belgilaydi (masalan, background-color: #f0f0f0;).
        3. background-image: Orqa fonga tasvir qo‘shadi (masalan, background-image: url('image.jpg');).
        4. background-position: Tasvirning joylashuvini belgilaydi (masalan, background-position: center;).
        5. background-size: Tasvirning o‘lchamini aniqlaydi (masalan, background-size: cover;).
        6. background-repeat: Tasvirning takrorlanishini belgilaydi (masalan, background-repeat: no-repeat;).
        7. background-clip: Orqa fonni qaysi qismga chegaralashni belgilaydi (masalan, background-clip: content-box;).
        8. background-origin: Orqa fonning boshlanish nuqtasini belgilaydi.
        9. background-attachment: Orqa fon tasvirining skrollanish xususiyatini belgilaydi (masalan, background-attachment: fixed;).
        10. background-blend-mode: Fon ranglari va tasvirlarning bir-biriga qanday ta’sir qilishini aniqlaydi (masalan, background-blend-mode: multiply;).

        Gradientlar:
        1. linear-gradient(): Chiziqli gradient yaratadi (masalan, background: linear-gradient(to right, red, blue);).
        2. radial-gradient(): Aylana gradient yaratadi.
        3. conic-gradient(): Konus shaklidagi gradient yaratadi.
        4. repeating-linear-gradient(): Takrorlanuvchi chiziqli gradient hosil qiladi.
        5. repeating-radial-gradient(): Takrorlanuvchi aylana gradient hosil qiladi.
        """,
        
        3: """
        Qutini boshqarish (Box Model):
        Margin va Padding:
        1. margin: Element atrofidagi tashqi bo‘shliqni belgilaydi (masalan, margin: 10px;).
        2. margin-top: Har bir tomonga alohida bo‘shliq belgilaydi (masalan, margin-top: 20px;).
        3. margin-right: ...
        4. margin-bottom: ...
        5. margin-left: ...
        6. padding: Element ichki bo‘shlig‘ini belgilaydi (masalan, padding: 10px;).
        7. padding-top: ...
        8. padding-right: ...
        9. padding-bottom: ...
        10. padding-left: ...

        O‘lcham va Qutini chegarasi:
        1. width: Elementning kengligini belgilaydi (masalan, width: 100px;).
        2. min-width: Minimal kenglikni aniqlaydi (masalan, min-width: 50px;).
        3. max-width: Maksimal kenglikni aniqlaydi (masalan, max-width: 200px;).
        4. height: Elementning balandligini belgilaydi (masalan, height: 100px;).
        5. min-height: ...
        6. max-height: ...
        7. box-sizing: Elementning o‘lchamini hisoblash usulini belgilaydi (masalan, box-sizing: border-box;).

        Chegaralar (Borders):
        1. border: Element chegarasi uchun qisqa yozuv (masalan, border: 1px solid black;).
        2. border-width: Chegaraning kengligini belgilaydi.
        3. border-style: ...
        4. border-color: ...
        5. border-radius: Element chekkalarini yumaloqlash (masalan, border-radius: 5px;).
        6. border-image: Chegaralarda rasm ishlatish imkoniyati.
        7. outline: Chegaradan tashqaridagi chiziqni belgilaydi.
        8. box-shadow: Qutiga soya qo‘shadi (masalan, box-shadow: 2px 2px 5px gray;).
        """,
        
        4: """
        Joylashuv (Positioning):
        Position va Display:
        1. position: Elementning joylashuvini belgilaydi (masalan, position: relative;).
        2. top: Joylashuvni belgilash uchun koordinatalar (masalan, top: 10px;).
        3. right: ...
        4. bottom: ...
        5. left: ...
        6. z-index: Elementlarning qavatini belgilaydi (masalan, z-index: 1;).
        7. display: Element ko‘rinishini boshqaradi (masalan, display: block;).
        8. visibility: Element ko‘rinishini boshqaradi (masalan, visibility: visible;).
        9. overflow: Element chegarasidan tashqarida joylashgan qismini boshqaradi (masalan, overflow: hidden;).
        10. overflow-x: ...
        11. overflow-y: ...
        12. clip: Elementni kesish maydonini aniqlaydi.
        13. clip-path: Elementni murakkab shaklda kesish uchun ishlatiladi.
        """,
        
        5: """
        Layoutlar (Flexbox va Grid):
        Flexbox:
        1. display: flex: Flex konteyner yaratadi.
        2. flex-direction: Elementlarning asosiy o‘qi bo‘ylab yo‘nalishini belgilaydi (masalan, flex-direction: row;).
        3. flex-wrap: Elementlarni o‘rab olishni boshqaradi (masalan, flex-wrap: wrap;).
        4. justify-content: Asosiy o‘q bo‘ylab hizalash (masalan, justify-content: center;).
        5. align-items: O‘zaro perpendikulyar o‘q bo‘ylab hizalash (masalan, align-items: stretch;).
        6. align-content: Bir nechta qatorlarning hizalanishi (masalan, align-content: space-between;).
        7. flex: Har bir elementning egallagan joyini belgilash uchun qisqa yozuv (masalan, flex: 1;).
        8. flex-grow: Elementning ortiqcha joyni qancha egallashini belgilaydi (masalan, flex-grow: 2;).
        9. flex-shrink: Element siqilganda qancha qisqarishi kerakligini belgilaydi (masalan, flex-shrink: 1;).
        10. flex-basis: Elementning asosiy o‘lchamini belgilaydi (masalan, flex-basis: 100px;).

        Grid:
        1. display: grid: Grid konteyner yaratadi.
        2. grid-template-columns: Ustunlarning tuzilmasini belgilaydi (masalan, grid-template-columns: 1fr 2fr;).
        3. grid-template-rows: Qatorlarning tuzilmasini belgilaydi.
        4. grid-template-areas: Grid ichidagi sohalarni belgilaydi.
        5. gap: Qatorlar va ustunlar orasidagi bo‘shliqni aniqlaydi (masalan, gap: 10px;).
        6. grid-column: Elementning qator va ustun oralig‘ini belgilaydi (masalan, grid-column: 1 / 3;).
        7. grid-row: ...
        8. place-items: Elementlarni hizalash uchun qisqa yozuv (masalan, place-items: center;).
        9. auto-rows: Yangi qatorlarning avtomatik o‘lchamini belgilaydi.
        10. auto-columns: Yangi ustunlarning avtomatik o‘lchamini belgilaydi.
        """,
        
        6: """
        Animatsiyalar va O‘tishlar (Animations & Transitions):
        Transitions:
        1. transition: O‘tish effektini boshqarish uchun qisqa yozuv (masalan, transition: all 0.3s ease;).
        2. transition-property: O‘tish amal qiladigan xususiyatni belgilaydi (masalan, transition-property: width;).
        3. transition-duration: O‘tish davomiyligini belgilaydi (masalan, transition-duration: 0.5s;).
        4. transition-timing-function: O‘tish tezligini boshqaradi (masalan, transition-timing-function: linear;).
        5. transition-delay: O‘tishni boshlash kechikishini belgilaydi (masalan, transition-delay: 0.2s;).

        Animations:
        1. @keyframes: Animatsiyaning qadamlarini belgilaydi (masalan, @keyframes example { ... }).
        2. animation: Animatsiya uchun qisqa yozuv (masalan, animation: move 2s infinite;).
        3. animation-name: @keyframes orqali yaratilgan animatsiya nomi (masalan, animation-name: slide;).
        4. animation-duration: Animatsiya davomiyligi (masalan, animation-duration: 1s;).
        5. animation-timing-function: Animatsiyaning tezlik egri chizig‘i (masalan, animation-timing-function: ease-in-out;).
        6. animation-delay: Animatsiyani boshlash vaqtini kechiktirish (masalan, animation-delay: 0.5s;).
        7. animation-iteration-count: Takrorlanish soni (masalan, animation-iteration-count: infinite;).
        8. animation-direction: Yo‘nalishni boshqaradi (masalan, animation-direction: alternate;).
        9. animation-fill-mode: Animatsiya tugaganidan keyin holatini belgilaydi (masalan, animation-fill-mode: forwards;).
        10. animation-play-state: Animatsiyani to‘xtatish yoki davom ettirish (masalan, animation-play-state: running;).
        """,
        
        7: """
        Jadval elementlari (Table Properties):
        1. border-collapse: Jadval chegaralari birlashishini boshqaradi (masalan, border-collapse: collapse;).
        2. border-spacing: Hujayralar orasidagi bo‘shliqni aniqlaydi (masalan, border-spacing: 5px;).
        3. caption-side: Jadval sarlavhasining joylashuvini belgilaydi (masalan, caption-side: top;).
        4. empty-cells: Bo‘sh hujayralar ko‘rinishini boshqaradi (masalan, empty-cells: hide;).
        5. table-layout: Jadval tartibini aniqlaydi (masalan, table-layout: fixed;).
        """,
        
        8: """
        Foydalanuvchi bilan muloqot elementlari (User Interaction):
        1. cursor: Sichqoncha kursorining ko‘rinishini belgilaydi (masalan, cursor: pointer;).
        2. pointer-events: Element bilan interaktiv harakatni boshqaradi (masalan, pointer-events: auto;).
        3. resize: Foydalanuvchi elementni kattalashtirish imkonini belgilaydi (masalan, resize: both;).

        User Select:
        1. user-select: Matnni tanlash imkoniyatini boshqaradi (masalan, user-select: none;).
        """,
        
        9: """
        Media Queries va Responsiv Dizayn:
        1. @media: Ekran o‘lchamlariga moslashuvni belgilaydi (masalan, @media (max-width: 600px) { ... }).
        2. @supports: CSS xususiyatini qo‘llab-quvvatlanishini tekshiradi (masalan, @supports (display: grid) { ... }).
        3. @container: Konteynerga asoslangan dizayn qoidalari.

        Media Queries shartlari:
        1. min-width: Ekran minimal kengligini tekshiradi (masalan, @media (min-width: 768px) { ... }).
        2. max-width: ...
        3. min-height: ...
        4. max-height: ...
        5. aspect-ratio: Ekran tomonlari nisbatini aniqlaydi (masalan, aspect-ratio: 16/9;).
        6. hover: Sichqoncha mavjudligini tekshiradi.
        7. pointer: Sichqoncha aniqligini belgilaydi (masalan, pointer: coarse;).

        Responsiv O‘lchamlar:
        1. %, em, rem: Dinamik o‘lcham birliklari (masalan, width: 50%;).
        2. vw, vh: Ko‘rish oynasining kengligi va balandligini foizda belgilaydi (masalan, width: 50vw;).
        3. vmin, vmax: Ko‘rish oynasining minimal yoki maksimal o‘lchamiga mos ravishda belgilaydi.
        4. calc(): Dinamik hisoblash formulalaridan foydalanish (masalan, width: calc(100% - 20px);).
        """
    }
    
    print(f"\n{info[group_number]}")

if __name__ == "__main__":
    main()
