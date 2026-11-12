#!/usr/bin/env python3
"""North Live page generator — builds route pages, signal pages, sitemap.xml
and robots.txt from data.json + the SIGNALS table below. No dependencies."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://live.gbadventure.vip"
LASTMOD = "2026-11-12"
WA = "https://wa.me/923555101279?text=North%20Live%20report%3A%20"
GB = "https://gbadventure.vip"

# carrier rows: [name, bars 0-4, note]
SIGNALS = {
    "karimabad": {
        "place": "Hunza (Karimabad)", "short": "Hunza",
        "page": "which-sim-works-in-hunza.html",
        "quick": "SCOM is the most reliable network in Hunza — and Zong and Jazz both give strong 4G in Karimabad and the main KKH towns.",
        "carriers": [["SCOM", 4, "Best data"], ["Zong", 4, "Strong 4G"], ["Jazz", 4, "Strong 4G"],
                     ["Telenor", 2, "Slow"], ["Ufone", 1, "Weak"]],
        "intro": "Hunza sits on the Karakoram Highway, and its main towns are better connected than most of Gilgit-Baltistan. The gaps appear in the side valleys — Batura, Chapursan, Shimshal — and on the climb to Khunjerab, where every network fades.",
        "routes": ["kkh-gilgit-khunjerab", "babusar"],
        "faqs": [
            ["Does Zong work in Hunza?",
             "Yes. Zong has strong 4G in Karimabad and along the Karakoram Highway towns of Hunza. It thins out in the side valleys and on the climb towards Khunjerab."],
            ["Which SIM is best for Hunza?",
             "SCOM is the most reliable all-round choice for Hunza — it keeps working in Upper Hunza and smaller villages where national networks drop. Pair it with Zong or Jazz for the fastest 4G in Karimabad."],
            ["Is there 4G in Hunza?",
             "Yes — Karimabad and the main KKH towns have 4G on SCOM, Zong and Jazz. Speeds fall in the evenings and disappear entirely in remote spots such as Chapursan and the upper Batura area."],
            ["Which SIM is best for Gilgit-Baltistan overall?",
             "SCOM, the regional network built for Gilgit-Baltistan and AJK, has the widest mountain coverage. Most travellers carry SCOM as their main SIM and a Zong or Jazz SIM for fast data in the bigger towns."],
        ],
    },
    "skardu": {
        "place": "Skardu", "short": "Skardu",
        "page": "which-sim-works-in-skardu.html",
        "quick": "SCOM leads in Skardu; Zong and Jazz give good 4G in the city but thin out fast towards the valleys of Baltistan.",
        "carriers": [["SCOM", 4, "Best data"], ["Zong", 3, "Good 4G"], ["Jazz", 3, "Good 4G"],
                     ["Telenor", 2, "Slow"], ["Ufone", 1, "Weak"]],
        "intro": "Skardu city is well covered, but Baltistan's valleys are SCOM country. If your trip includes Shigar, Kharmang, Hushe or Deosai, plan around SCOM — and around dead zones with no signal at all.",
        "routes": ["skardu-road", "deosai"],
        "faqs": [
            ["Is there 4G in Skardu?",
             "Yes. Skardu city has 4G on SCOM, Zong and Jazz. Coverage is a city-and-highway thing — it fades quickly once you leave for the valleys."],
            ["Does Zong work in Skardu?",
             "Yes, Zong gives good 4G in Skardu city and along parts of the Skardu Road. For trips beyond the city — Shigar, Kharmang, Deosai — SCOM is the safer main SIM."],
            ["Which SIM should I carry for Deosai and the Baltistan valleys?",
             "SCOM. It is the only network with meaningful reach into the Baltistan valleys, and even SCOM has no reliable signal inside the Deosai Plains — download offline maps before you go."],
            ["Does Jazz work in Skardu?",
             "Yes, Jazz works in Skardu city with usable 4G. Outside the city its coverage is thinner than SCOM's."],
        ],
    },
    "gilgit": {
        "place": "Gilgit", "short": "Gilgit",
        "page": "which-sim-works-in-gilgit.html",
        "quick": "Every network works in Gilgit city — SCOM, Zong and Jazz all run strong 4G here. It is the best-connected city in Gilgit-Baltistan.",
        "carriers": [["SCOM", 4, "Best data"], ["Zong", 4, "Strong 4G"], ["Jazz", 4, "Strong 4G"],
                     ["Telenor", 3, "Good"], ["Ufone", 2, "Slow"]],
        "intro": "Gilgit is where travellers stock up on connectivity: every network runs here, SCO outlets sell SCOM SIMs in the bazaar, and it is the last place with fast data before the valleys. Sort your SIMs out in Gilgit before you move on.",
        "routes": ["kkh-chilas-gilgit", "gilgit-ghizer"],
        "faqs": [
            ["Which SIM is best in Gilgit city?",
             "Gilgit has the best connectivity in Gilgit-Baltistan: SCOM, Zong and Jazz all provide strong 4G in the city, and Telenor is decent too. Any of them works for a city stay."],
            ["Is there 4G in Gilgit?",
             "Yes — full 4G coverage across Gilgit city on SCOM, Zong and Jazz, with the fastest speeds near the bazaar and airport areas."],
            ["Does Telenor work in Gilgit?",
             "Yes, Telenor works in Gilgit city, though its coverage drops faster than SCOM or Zong once you leave the city towards Hunza or Ghizer."],
            ["Which SIM should I buy in Gilgit for onward travel?",
             "Buy SCOM in Gilgit if you are heading into the valleys — it is sold at SCO outlets in the city and is the network most likely to work in Hunza, Ghizer, Astore and Baltistan."],
        ],
    },
    "naran": {
        "place": "Naran", "short": "Naran",
        "page": "which-sim-works-in-naran.html",
        "quick": "Zong works best in Naran. SCOM is a Gilgit-Baltistan network and is only patchy here in the Kaghan Valley (Khyber Pakhtunkhwa).",
        "carriers": [["Zong", 4, "Best here"], ["Telenor", 3, "Good"], ["Jazz", 3, "Good"],
                     ["SCOM", 1, "Patchy — GB network"], ["Ufone", 2, "Slow"]],
        "intro": "Naran is in Khyber Pakhtunkhwa, not Gilgit-Baltistan — and that changes which SIM you need. The national networks run the Kaghan Valley; SCOM only becomes the essential SIM once you cross into GB at Chilas.",
        "routes": ["babusar", "naran"],
        "faqs": [
            ["Which SIM works best in Naran?",
             "Zong is the strongest network in Naran, with good 4G in the town and bazaar. Telenor and Jazz also work well in town."],
            ["Does SCOM work in Naran?",
             "Only patchily. SCOM is the regional network for Gilgit-Baltistan and Azad Kashmir, while Naran is in Khyber Pakhtunkhwa — travellers crossing into GB often buy an SCOM SIM after Chilas. In Naran itself, rely on Zong, Telenor or Jazz."],
            ["Is there 4G in Naran?",
             "Yes, in Naran town on Zong, Telenor and Jazz. Signal weakens on the road up the valley towards Battakundi and Bassal, and there is no reliable coverage on the Babusar climb."],
            ["Will my SIM work at Babusar Top?",
             "Expect little to no signal at Babusar Top itself on any network. Download offline maps in Naran before you climb — and note that the pass is closed for winter from November."],
        ],
    },
}

# Per-route SEO content: title/H1 question, a context paragraph, optional best
# alternative, nearest signal page key, related route ids, and 4 FAQs.
ROUTE_EXTRA = {
    "babusar": {
        "title": "Is Babusar Top Open Today? Live Road Status — North Live",
        "h1": "Is Babusar Top Open Today?",
        "context": "Babusar Top (about 4,170m) is the seasonal shortcut between Naran in the Kaghan Valley and Chilas on the Karakoram Highway. Because it is high, exposed and avalanche-prone in winter, it is one of the first passes in Pakistan to close and one of the last to reopen. Until it opens again in summer, all Gilgit-Baltistan traffic uses the Karakoram Highway.",
        "alt": "Best alternative while Babusar is closed: the Karakoram Highway via Besham and Chilas — open all year.",
        "sig": "naran", "related": ["naran", "kkh-chilas-gilgit", "deosai"],
        "faqs": [
            ["Is Babusar Top open in November?",
             "No. Babusar Top was closed by Mansehra district police on 11 November 2026 after heavy snowfall, and in a normal year the pass shuts for winter with the first heavy snow in late October or November. It does not reopen until the summer season."],
            ["When does Babusar Top open again?",
             "Babusar Top typically reopens around mid-June, once the National Highway Authority clears the winter snow — in some years it opens in late May or early July depending on snowfall. The normal season runs from about mid-June to mid-October."],
            ["Which route is open to Gilgit in winter?",
             "The Karakoram Highway via Besham and Chilas is the year-round route into Gilgit-Baltistan. It is longer than the Babusar shortcut, but it stays open through winter, apart from short landslide or fog closures."],
            ["Can I still reach Naran if Babusar Top is closed?",
             "Yes. The road up to Naran town remains open and Naran receives snowfall tourists in November. The police closure is beyond Bassal, on the climb towards Babusar Top."],
        ],
    },
    "kkh-chilas-gilgit": {
        "title": "Is the KKH (Chilas–Gilgit) Open Today? Live Road Status — North Live",
        "h1": "Is the KKH from Chilas to Gilgit Open Today?",
        "context": "The Chilas–Gilgit section of the Karakoram Highway follows the Indus gorge through Diamer and is the main supply route for the whole of Gilgit-Baltistan. While Babusar Top is closed for winter, every vehicle heading to Gilgit, Hunza, Ghizer and the Skardu Road junction at Jaglot passes this way.",
        "alt": "",
        "sig": "gilgit", "related": ["kkh-gilgit-khunjerab", "skardu-road", "fairy-meadows"],
        "faqs": [
            ["Is the Karakoram Highway open today?",
             "Yes — the KKH between Chilas and Gilgit is open for all traffic (North Live launch report, 12 November 2026). Conditions on the KKH can change within hours, so check this page again before a long drive."],
            ["Is the Karakoram Highway open in winter?",
             "Yes. The KKH is Gilgit-Baltistan's year-round lifeline and stays open through winter. Short closures do happen — most often for landslides, rockfall or fog — but it is the only all-season road into the region."],
            ["How long does Chilas to Gilgit take?",
             "The section is roughly 230 km and usually takes 5 to 7 hours by car, depending on road works, weather and stops. Start early in winter so you are not driving the gorge sections after dark."],
            ["What is the alternative route when Babusar Top is closed?",
             "This is the alternative: traffic from Islamabad and Mansehra uses the KKH via Besham, Pattan and Dassu to Chilas, then continues to Gilgit. It adds several hours compared with the Babusar shortcut."],
        ],
    },
    "kkh-gilgit-khunjerab": {
        "title": "Is the KKH to Khunjerab Open Today? Live Road Status — North Live",
        "h1": "Is the KKH from Gilgit to Khunjerab Open Today?",
        "context": "From Gilgit the KKH climbs through Hunza — Karimabad, Gulmit and Passu — to Sost and the Khunjerab Pass, the highest paved international border crossing in the world at 4,693m. It is one of the great drives of Pakistan, and in winter its upper section is a serious high-altitude journey.",
        "alt": "",
        "sig": "karimabad", "related": ["kkh-chilas-gilgit", "gilgit-ghizer", "babusar"],
        "faqs": [
            ["Is Khunjerab Pass open today?",
             "The road from Gilgit to Khunjerab is open for traffic (North Live launch report, 12 November 2026). Expect sub-zero temperatures and strong wind at the pass itself, which sits at 4,693m."],
            ["Can tourists cross the Khunjerab border in winter?",
             "Typically not. Under the Pakistan–China agreement the Khunjerab border crossing usually closes to tourists and trade for the winter months (commonly January to March), even though the road up to the pass on the Pakistan side may still be driveable. Always check the current notice before planning a crossing."],
            ["How cold is Khunjerab Pass in November?",
             "Well below freezing. Daytime temperatures at the pass in November are commonly around −10°C or lower, and wind chill makes it feel much colder. Warm layers, gloves and a hat are essential even for a short photo stop."],
            ["Which SIM works at Khunjerab Pass?",
             "Mobile coverage fades after Sost, the last town before the pass. SCOM is usually the last network to drop out on this stretch, and there is no reliable signal at the pass itself. Download offline maps in Gilgit or Karimabad."],
        ],
    },
    "skardu-road": {
        "title": "Skardu Road Status Today — Open or Closed? Live S-1 Update — North Live",
        "h1": "Skardu Road Status Today — Open or Closed?",
        "context": "The S-1 follows the Indus river from Jaglot to Skardu, the gateway to Baltistan, the Deosai Plains and the Karakoram giants. It has been widened and improved in recent years, but it remains a mountain road where conditions — not distance — decide your travel time.",
        "alt": "",
        "sig": "skardu", "related": ["deosai", "kkh-chilas-gilgit", "fairy-meadows"],
        "faqs": [
            ["Is Skardu Road open today?",
             "Yes — the S-1 Skardu Road is open, with a caution advisory for winter rockfall on the stretches near Stak (North Live, 12 November 2026). Travel in daylight where you can."],
            ["How long is the drive from the KKH to Skardu?",
             "The Skardu Road runs about 167 km from its junction with the Karakoram Highway near Jaglot to Skardu city, and normally takes 5 to 7 hours. Allow longer in winter or after rain, when clearing work can hold traffic."],
            ["Is Skardu Road risky in winter?",
             "It has landslide- and rockfall-prone sections carved into the Indus gorge, and winter adds ice and falling rocks. The standard advice is to travel in daylight, avoid the road during heavy rain, and check the latest status before setting off."],
            ["Is there another way to reach Skardu in winter?",
             "By road, no — in winter the S-1 is the only route; the Deosai track from Astore is a summer-only alternative. Skardu also has flights from Islamabad, but they are weather-dependent and are often cancelled in poor visibility."],
        ],
    },
    "deosai": {
        "title": "Is Deosai Open Today? Live Road Status — North Live",
        "h1": "Is Deosai Open Today?",
        "context": "Deosai — the 'Land of Giants' — is one of the world's highest plateaus, averaging over 4,000m, famous for Sheosar Lake, wildflowers in July and Himalayan brown bears. That altitude is exactly why its season is short: for more than half the year it is a snowbound wilderness.",
        "alt": "Want Skardu instead? The S-1 Skardu Road from the KKH stays open in winter — check its live status below.",
        "sig": "skardu", "related": ["skardu-road", "babusar", "fairy-meadows"],
        "faqs": [
            ["Is Deosai open in November?",
             "No. The Deosai Plains are snow covered and closed for the winter season (status: 12 November 2026). Both entry tracks — from Skardu and from Astore — are impassable until the snow melts."],
            ["When does Deosai open for the season?",
             "Deosai typically opens in June, once the tracks are cleared, and stays open until about October, closing with the first heavy snow. In a heavy-snow year the opening can slip to late June or July."],
            ["What vehicle do I need for Deosai?",
             "A high-clearance vehicle is strongly recommended — the tracks are unpaved, with water crossings and rocky sections. In the peak summer season regular cars do cross in good weather, but low clearance and bad weather catch many drivers out."],
            ["Is there mobile signal in Deosai?",
             "There is little to no reliable mobile signal inside the plains on any network. Download offline maps, carry enough fuel, and tell someone your plan before you enter."],
        ],
    },
    "naran": {
        "title": "Is Naran Open Today? Kaghan Valley Road Status — North Live",
        "h1": "Is Naran Open Today?",
        "context": "Naran is the busy hub of the Kaghan Valley — the jumping-off point for Lake Saiful Muluk, Lalazar and the Babusar road. In November the crowds are gone, the first snow has arrived, and the valley splits in two: Naran itself open for snowfall trips, everything above Bassal closed until summer.",
        "alt": "Heading to Gilgit-Baltistan? Use the Karakoram Highway via Besham–Chilas while Babusar Top is closed.",
        "sig": "naran", "related": ["babusar", "kkh-chilas-gilgit", "deosai"],
        "faqs": [
            ["Is Naran open today?",
             "Yes — Naran town is reachable by road and is receiving tourists coming for the early snowfall (District police / The News, 12 November 2026). The closure in the valley is further up, beyond Bassal towards Babusar Top."],
            ["Can I drive from Naran to Babusar Top now?",
             "No. District police closed the road beyond Bassal on 11 November 2026 after heavy snowfall made the climb to Babusar Top dangerous. The pass is expected to stay closed for the winter season."],
            ["Does the road to Naran close in winter?",
             "The road to Naran usually stays open longer than the Babusar section, but heavy snow spells can close it temporarily, and most hotels shut for the deep winter. Check the status here on the day you travel."],
            ["Which SIM works in Naran?",
             "Zong works best in Naran, with good Telenor and Jazz cover in town. SCOM is a Gilgit-Baltistan and AJK network and is only patchy here in the Kaghan Valley (Khyber Pakhtunkhwa), so do not rely on it."],
        ],
    },
    "gilgit-ghizer": {
        "title": "Is the Gilgit–Ghizer Road Open Today? Live Status — North Live",
        "h1": "Is the Gilgit to Ghizer Road Open Today?",
        "context": "The Gilgit–Ghizer road follows the Gilgit River west through Singul and Gahkuch towards Phander's trout streams and, in summer, over Shandur to Chitral. In winter it is a lifeline for Ghizer's villages — open, but demanding respect on icy morning bends.",
        "alt": "",
        "sig": "gilgit", "related": ["kkh-gilgit-khunjerab", "kkh-chilas-gilgit", "fairy-meadows"],
        "faqs": [
            ["Is the Gilgit to Ghizer road open today?",
             "Yes — the road is open, with a winter caution for icy patches after Gahkuch in the early morning (North Live advisory, 12 November 2026). If you can, start after 10am when the sun has softened the ice."],
            ["How far is Gahkuch from Gilgit?",
             "Gahkuch, the main town of Ghizer district, is about 72 km from Gilgit city — roughly 2 to 3 hours by road along the Gilgit River."],
            ["Is Shandur Pass open in winter?",
             "No. Shandur Top (about 3,700m), which connects Ghizer with Chitral, is a seasonal pass that closes with winter snow — typically from around November to May. The lower Gilgit–Ghizer road up to Gahkuch and Phander stays open."],
            ["Any winter driving tips for the Ghizer road?",
             "Watch for black ice on shaded bends before mid-morning, keep speeds low on the river-side sections, and carry chains if you are heading beyond Gahkuch towards Phander or Gupis in a cold spell."],
        ],
    },
    "fairy-meadows": {
        "title": "Is Fairy Meadows Open Today? Raikot Jeep Track Status — North Live",
        "h1": "Is Fairy Meadows Open Today?",
        "context": "Fairy Meadows, at the foot of Nanga Parbat's Raikot face, is reached by one of Pakistan's most dramatic combinations: the KKH, a cliff-edge jeep track, and a forest trek. In winter the meadows are silent and snowbound — beautiful, but only for travellers who come prepared.",
        "alt": "",
        "sig": "gilgit", "related": ["kkh-chilas-gilgit", "skardu-road", "deosai"],
        "faqs": [
            ["Can I visit Fairy Meadows in winter?",
             "It is possible, but it is a different trip from summer. The Raikot–Tattu jeep track only runs in good winter weather, most guesthouses are closed, and the trek from Tattu is on snow. Confirm with local jeep operators at Raikot Bridge before you set out."],
            ["How do I reach Fairy Meadows?",
             "Drive the Karakoram Highway to Raikot Bridge, take a local jeep up the track to Tattu village (about 1 to 1.5 hours), then trek roughly 2 to 3 hours to Fairy Meadows. In winter, allow extra time for both stages."],
            ["Is there mobile signal at Fairy Meadows?",
             "Signal is limited and patchy — SCOM and Zong connect at some points around Tattu and the meadows, but treat Fairy Meadows as mostly off-grid and download what you need at Raikot."],
            ["Do I need a guide for Fairy Meadows in winter?",
             "In winter, yes — hiring a local guide or porter from Tattu is strongly recommended. Snow hides the trail, days are short, and conditions at about 3,300m change fast."],
        ],
    },
}

FA_CSS = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"

CSS = """
:root{
  --g1:#177A44; --g2:#2E9E5B; --deep:#0B3524; --nav:#0C3B2A;
  --ink:#132219; --mut:#6E8272; --bg:#F6FAF7;
  --ok:#16A34A; --okbg:#E6F6EC; --bad:#DC2626; --badbg:#FDECEC; --warn:#B45309; --warnbg:#FCF2DF;
  --gold:#D9A441; --wa:#1FA855; --sh:0 10px 28px rgba(15,80,45,.09);
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:-apple-system,BlinkMacSystemFont,'SF Pro Display','Segoe UI',Poppins,Roboto,sans-serif;color:var(--ink);
  background:linear-gradient(160deg,#DFF3E6 0%,#E9F6EE 45%,#E3F1F6 100%);min-height:100dvh}
a{text-decoration:none;color:inherit}
button{font:inherit;cursor:pointer;border:0;background:none;color:inherit}

/* iPhone frame on larger screens */
.device{position:relative;max-width:430px;margin:0 auto}
.island{display:none}
.phone{max-width:430px;margin:0 auto;background:var(--bg);min-height:100dvh;position:relative;
  box-shadow:0 0 60px rgba(11,53,36,.18);padding:0 20px 110px}
@media(min-width:520px){
  body{padding:30px 0 46px}
  .device{max-width:452px;border:11px solid #101013;border-radius:54px;overflow:hidden;
    box-shadow:0 40px 90px rgba(7,40,26,.35),0 0 0 2px #2a2a2e}
  .island{display:block;position:absolute;top:12px;left:50%;transform:translateX(-50%);
    width:112px;height:30px;border-radius:999px;background:#000;z-index:80}
  .phone{min-height:0;height:min(880px,calc(100dvh - 112px));overflow-y:auto;box-shadow:none}
  .phone::-webkit-scrollbar{width:0}
  .bnav{position:absolute !important}
}

/* header */
.hbar{display:flex;align-items:center;gap:10px;padding:18px 0 4px}
@media(min-width:520px){.hbar{padding-top:34px}}
.logo{display:flex;align-items:center;gap:9px;font-weight:800;font-size:19px;color:var(--deep)}
.logo .tile{width:36px;height:36px;border-radius:12px;background:linear-gradient(145deg,var(--g1),var(--g2));color:#fff;display:grid;place-items:center;font-size:16px;box-shadow:0 6px 14px rgba(23,122,68,.35)}
.logo em{font-style:normal;color:var(--g1)}
.back{width:42px;height:42px;border-radius:50%;background:#fff;box-shadow:var(--sh);display:grid;place-items:center;font-size:15px;color:var(--deep);flex:none}
.hbtn{margin-left:auto;width:42px;height:42px;border-radius:50%;background:#fff;box-shadow:var(--sh);display:grid;place-items:center;font-size:16px;color:var(--deep);position:relative}
.hbtn::after{content:'';position:absolute;top:10px;right:11px;width:8px;height:8px;border-radius:50%;background:var(--bad);border:2px solid #fff}

.crumb{margin-top:14px;font-size:12px;font-weight:600;letter-spacing:.1em;color:var(--mut);text-transform:uppercase}
h1.q{font-size:25px;font-weight:800;line-height:1.25;color:var(--deep);margin-top:5px;letter-spacing:-.01em}
h2.sec{font-size:18.5px;font-weight:700;color:var(--deep);margin:26px 0 12px}

/* status card */
.statuscard{margin-top:16px;background:#fff;border-radius:26px;box-shadow:var(--sh);padding:20px}
.sc-top{display:flex;align-items:center;gap:10px}
.pill{display:inline-block;font-size:11.5px;font-weight:700;letter-spacing:.05em;padding:6px 13px;border-radius:999px}
.pill.open{background:var(--okbg);color:var(--ok)} .pill.closed{background:var(--badbg);color:var(--bad)} .pill.caution{background:var(--warnbg);color:var(--warn)}
.wx{margin-left:auto;font-size:13px;font-weight:600;color:var(--mut);display:inline-flex;align-items:center;gap:6px}
.wx i{color:var(--g1)}
.sc-reason{font-size:19px;font-weight:700;color:var(--deep);margin-top:13px;line-height:1.3}
.sc-detail{font-size:14px;line-height:1.6;color:#33463D;margin-top:7px}
.sc-meta{margin-top:13px;padding-top:11px;border-top:1px dashed #E4EFE7;font-size:12px;color:var(--mut);display:flex;gap:7px;align-items:flex-start;line-height:1.5}
.sc-meta i{color:var(--ok);margin-top:1px}
.ans{font-size:14.5px;line-height:1.65;color:#2A3B31;margin-top:16px}
.altbox{margin-top:16px;background:var(--warnbg);border:1px solid #F0DFBA;border-radius:18px;padding:14px 16px;font-size:13.5px;line-height:1.55;color:#7A4A08;display:flex;gap:10px}
.altbox i{margin-top:2px}
.quickbox{margin-top:16px;background:var(--okbg);border:1px solid #CBEED6;border-radius:18px;padding:15px 16px;font-size:14px;line-height:1.6;color:#14532D}
.quickbox b{display:block;font-size:11.5px;letter-spacing:.1em;margin-bottom:4px}

/* big button */
.bigbtn{margin-top:18px;display:flex;align-items:center;justify-content:center;gap:10px;width:100%;
  background:linear-gradient(145deg,var(--g1),var(--g2));color:#fff;font-weight:700;font-size:15.5px;
  padding:16px;border-radius:999px;box-shadow:0 14px 28px rgba(23,122,68,.4);transition:transform .15s}
.bigbtn:active{transform:scale(.98)}
.bigbtn .fa-whatsapp{font-size:19px}

/* faq */
.fq{background:#fff;border-radius:20px;box-shadow:var(--sh);padding:16px 17px;margin-bottom:11px}
.fq h3{font-size:14.5px;font-weight:700;color:var(--deep);line-height:1.4}
.fq p{font-size:13.5px;line-height:1.6;color:#3C4F44;margin-top:6px}

/* link rows */
.rrow{background:#fff;border-radius:22px;box-shadow:var(--sh);padding:14px 15px;display:flex;align-items:center;gap:12px;margin-bottom:11px;transition:transform .15s}
.rrow:active{transform:scale(.985)}
.tile{width:46px;height:46px;border-radius:15px;display:grid;place-items:center;font-size:19px;flex:none}
.tile.green{background:var(--okbg);color:var(--ok)} .tile.red{background:var(--badbg);color:var(--bad)} .tile.amber{background:var(--warnbg);color:var(--warn)}
.rrow .tt{font-size:14.5px;font-weight:600;line-height:1.3}
.rrow .ts{font-size:12px;color:var(--mut);margin-top:2px;line-height:1.4}
.rrow .rt{margin-left:auto;text-align:right;flex:0 1 auto;max-width:44%}
.rrow .tm{display:block;font-size:11px;color:var(--mut);margin-top:5px;overflow-wrap:break-word}
.siglink{margin-top:14px;background:#fff;border-radius:22px;box-shadow:var(--sh);padding:15px;display:flex;align-items:center;gap:12px;font-size:14px;font-weight:600;color:var(--deep)}
.siglink .tile{background:var(--okbg);color:var(--g1)}
.siglink .chev{margin-left:auto;color:#B9C8BE}

/* signal card */
.sigcard{background:#fff;border-radius:26px;box-shadow:var(--sh);padding:8px 20px 14px;margin-top:16px}
.srow{display:flex;align-items:center;gap:12px;padding:13px 0;border-bottom:1px dashed #E4EFE7}
.srow:last-child{border-bottom:0}
.srow .ct{width:42px;height:42px;border-radius:13px;background:var(--okbg);color:var(--g1);display:grid;place-items:center;font-weight:800;font-size:14px;flex:none}
.srow .nm{font-size:14px;font-weight:600}
.srow .nt{font-size:11.5px;color:var(--mut)}
.srow .br{margin-left:auto;text-align:right}
.bars{display:flex;gap:3px;align-items:flex-end;height:17px;justify-content:flex-end}
.bars i{width:5px;border-radius:2px;background:#E1EDE4;display:block}
.bars i:nth-child(1){height:5px}.bars i:nth-child(2){height:9px}.bars i:nth-child(3){height:13px}.bars i:nth-child(4){height:17px}
.bars i.on{background:var(--g2)}
.br .bt{font-size:11px;font-weight:600;color:var(--g1);margin-top:3px}
.br .bt.no{color:var(--bad)}

/* GB card */
.gbcard{margin-top:22px;border-radius:28px;padding:22px;color:#fff;position:relative;overflow:hidden;
  background:linear-gradient(150deg,#3A2C07 0%,#7A5A14 55%,#B9862F 130%);box-shadow:0 16px 30px rgba(122,90,20,.35)}
.gbcard .mtn{position:absolute;right:16px;top:12px;font-size:56px;opacity:.25}
.gbcard .lbl{font-size:11px;font-weight:600;letter-spacing:.14em;color:#FFE1A1}
.gbcard h3{font-size:20px;font-weight:800;margin-top:6px;line-height:1.25;max-width:250px;position:relative}
.gbcard p{font-size:13px;opacity:.92;margin-top:7px;max-width:270px;line-height:1.55}
.gbcard .cta{margin-top:15px;display:inline-flex;align-items:center;gap:8px;background:var(--gold);color:#241B08;font-weight:700;font-size:13.5px;padding:11px 18px;border-radius:999px;box-shadow:0 8px 18px rgba(0,0,0,.25)}

.foot{margin-top:24px;text-align:center;font-size:11.5px;color:var(--mut);line-height:1.7;padding:0 8px}
.foot b{color:var(--deep)}

/* bottom nav */
.bnav{position:fixed;left:50%;transform:translateX(-50%);bottom:16px;width:min(394px,calc(100% - 28px));
  background:var(--nav);border-radius:999px;display:flex;align-items:center;justify-content:space-around;
  padding:10px 8px;box-shadow:0 18px 36px rgba(7,40,26,.45);z-index:60}
.bnav a{display:flex;flex-direction:column;align-items:center;gap:3px;color:#9DBFA9;font-size:10px;font-weight:500;padding:2px 8px}
.bnav a .ni{font-size:18px;line-height:1}
.bnav a.on{color:#fff}
.bnav .center{width:54px;height:54px;border-radius:50%;background:linear-gradient(145deg,var(--g2),var(--g1));
  display:grid;place-items:center;font-size:21px;color:#fff;margin-top:-30px;border:4px solid var(--bg);
  box-shadow:0 10px 22px rgba(23,122,68,.5);flex:none}

/* RESPONSIVE FIX — no side wobble */
html,body{overflow-x:hidden;overflow-x:clip}
body{width:100%}
img,svg,video{max-width:100%}
.device{max-width:min(452px,calc(100vw - 16px))}
.phone{overflow-x:clip}
.rrow>div,.alertrow>div,.srow>div{min-width:0}
.tt,.ts,.nt,.sc-meta{overflow-wrap:break-word}
.bnav{max-width:calc(100vw - 24px)}
"""


def head(title, desc, canonical, jsonld=""):
    ld = ""
    if jsonld:
        ld = '\n<script type="application/ld+json">' + jsonld + "</script>"
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>""" + title + """</title>
<meta name="description" content=\"""" + desc + """\">
<link rel="canonical" href=\"""" + canonical + """\">
<meta property="og:type" content="website">
<meta property="og:site_name" content="North Live">
<meta property="og:title" content=\"""" + title + """\">
<meta property="og:description" content=\"""" + desc + """\">
<meta property="og:url" content=\"""" + canonical + """\">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href=\"""" + FA_CSS + """\">
<style>""" + CSS + """</style>""" + ld + """
</head>
"""


def shell_open(back=True):
    back_html = '<a class="back" href="index.html" aria-label="Back to home"><i class="fa-solid fa-arrow-left"></i></a>' if back else ""
    return """<body>
<div class="device">
<div class="island"></div>
<div class="phone">
  <div class="hbar">
    """ + back_html + """
    <a class="logo" href="index.html"><span class="tile"><i class="fa-solid fa-mountain"></i></span>North<em>Live</em></a>
    <a class="hbtn" href=\"""" + WA + """\" target="_blank" rel="noopener" aria-label="Report an update"><i class="fa-solid fa-bell"></i></a>
  </div>
"""


NAV = """
<nav class="bnav">
  <a href="index.html"><span class="ni"><i class="fa-solid fa-house"></i></span>Home</a>
  <a href="index.html#routes"><span class="ni"><i class="fa-solid fa-route"></i></span>Routes</a>
  <a class="center" href=\"""" + WA + """\" target="_blank" rel="noopener" aria-label="Report on WhatsApp"><i class="fa-solid fa-plus"></i></a>
  <a href="index.html#signal"><span class="ni"><i class="fa-solid fa-tower-cell"></i></span>Signal</a>
  <a href=\"""" + GB + """\" target="_blank" rel="noopener"><span class="ni"><i class="fa-solid fa-suitcase"></i></span>Tours</a>
</nav>
</div>
</body>
</html>
"""

FOOT = """
  <p class="foot"><b>North Live</b> — a GB Adventure service.<br>Launch data — statuses from public reports &amp; officials, 12 Nov 2026. Report changes on WhatsApp.<br>Statuses are reports, not guarantees — check locally before a high pass in bad weather.</p>
"""

GBCARD = """
  <div class="gbcard">
    <span class="mtn"><i class="fa-solid fa-mountain"></i></span>
    <div class="lbl">GB ADVENTURE</div>
    <h3>Planning to go? Travel with locals.</h3>
    <p>Guided tours across Gilgit-Baltistan with local drivers who know every turn of these roads.</p>
    <a class="cta" href=\"""" + GB + """\" target="_blank" rel="noopener">Book a tour <i class="fa-solid fa-arrow-right"></i></a>
  </div>
"""


def faq_jsonld(faqs):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }, ensure_ascii=False)


def faq_html(faqs):
    out = ['<h2 class="sec">Common questions</h2>']
    for q, a in faqs:
        out.append('<div class="fq"><h3>' + q + "</h3><p>" + a + "</p></div>")
    return "\n".join(out)


def bars_html(n):
    b = ""
    for i in range(1, 5):
        b += '<i class="' + ("on" if i <= n else "") + '"></i>'
    return b


def pill(status):
    return '<span class="pill ' + status + '">' + status.upper() + "</span>"


def status_tile(status, reason):
    if status == "open":
        return '<span class="tile green"><i class="fa-solid fa-route"></i></span>'
    if status == "caution":
        return '<span class="tile amber"><i class="fa-solid fa-triangle-exclamation"></i></span>'
    if "snow" in reason.lower():
        return '<span class="tile red"><i class="fa-solid fa-snowflake"></i></span>'
    return '<span class="tile red"><i class="fa-solid fa-ban"></i></span>'


WXJS = """
function wxIcon(c){if(c===0)return 'fa-sun';if(c<=2)return 'fa-cloud-sun';if(c===3)return 'fa-cloud';if(c===45||c===48)return 'fa-smog';if((c>=71&&c<=77)||c===85||c===86)return 'fa-snowflake';if(c>=95)return 'fa-cloud-bolt';if(c>=51)return 'fa-cloud-rain';return 'fa-cloud';}
function wxLabel(c){if(c===0)return 'Clear sky';if(c===1)return 'Mostly clear';if(c===2)return 'Partly cloudy';if(c===3)return 'Overcast';if(c===45||c===48)return 'Foggy';if((c>=71&&c<=77)||c===85||c===86)return 'Snow';if(c>=95)return 'Thunderstorm';if(c>=80&&c<=82)return 'Rain showers';if(c>=61&&c<=67)return 'Rain';if(c>=51&&c<=57)return 'Drizzle';return 'Cloudy';}
function relTime(iso){var s=(Date.now()-new Date(iso).getTime())/1e3;if(isNaN(s))return '';if(s<3600)return Math.max(1,Math.round(s/60))+' min ago';if(s<86400)return Math.round(s/3600)+'h ago';return Math.round(s/86400)+'d ago';}
"""


def route_script(r):
    js = """<script>
var RID="__RID__";""" + WXJS + """
fetch('data.json').then(function(x){return x.json();}).then(function(d){
  var rt=null,i;for(i=0;i<d.routes.length;i++){if(d.routes[i].id===RID)rt=d.routes[i];}
  if(!rt)return;
  var p=document.getElementById('stPill');p.className='pill '+rt.status;p.textContent=rt.status.toUpperCase();
  document.getElementById('stReason').textContent=rt.reason;
  document.getElementById('stDetail').textContent=rt.detail;
  document.getElementById('stMeta').textContent='Source: '+rt.source+' \\u00B7 updated '+relTime(rt.updatedISO);
}).catch(function(){});
fetch('https://api.open-meteo.com/v1/forecast?latitude=__LAT__&longitude=__LON__&current=temperature_2m,weather_code,wind_speed_10m&timezone=Asia%2FKarachi')
.then(function(x){return x.json();}).then(function(d){var c=d.current;
  document.getElementById('wxNow').innerHTML='<i class="fa-solid '+wxIcon(c.weather_code)+'"></i> '+Math.round(c.temperature_2m)+'\\u00B0C \\u00B7 '+wxLabel(c.weather_code)+' \\u00B7 wind '+Math.round(c.wind_speed_10m)+' km/h';
}).catch(function(){});
</script>"""
    return (js.replace("__RID__", r["id"])
              .replace("__LAT__", str(r["lat"]))
              .replace("__LON__", str(r["lon"])))


def route_row_link(r):
    return ('<a class="rrow" href="' + r["slug"] + '-road-status.html">' + status_tile(r["status"], r["reason"]) +
            '<div><div class="tt">' + r["name"] + '</div><div class="ts">' + r["reason"] + '</div></div>' +
            '<div class="rt">' + pill(r["status"]) + "</div></a>")


def route_page(r, routes_by_id):
    ex = ROUTE_EXTRA[r["id"]]
    fname = r["slug"] + "-road-status.html"
    canonical = BASE + "/" + fname
    desc = (r["name"] + " road update today — open or closed? Live status: " + r["reason"] +
            ". Current weather and answers — North Live, November 2026.")
    meta = "Source: " + r["source"] + ("" if "2026" in r["source"] else " · 12 Nov 2026")
    sig = SIGNALS[ex["sig"]]
    alt = ""
    if ex["alt"]:
        alt = ('\n  <div class="altbox"><i class="fa-solid fa-triangle-exclamation"></i><div>' + ex["alt"] + "</div></div>")
    related = "\n".join(route_row_link(routes_by_id[i]) for i in ex["related"])
    body = shell_open() + """
  <p class="crumb">Live road status · Northern Pakistan</p>
  <h1 class="q">""" + ex["h1"] + """</h1>
  <div class="statuscard">
    <div class="sc-top">""" + pill(r["status"]).replace('class="pill', 'id="stPill" class="pill') + """
      <span class="wx" id="wxNow"><i class="fa-solid fa-temperature-half"></i> Live weather…</span></div>
    <div class="sc-reason" id="stReason">""" + r["reason"] + """</div>
    <p class="sc-detail" id="stDetail">""" + r["detail"] + """</p>
    <p class="sc-meta"><i class="fa-solid fa-circle-check"></i><span id="stMeta">""" + meta + """</span></p>
  </div>
  <p class="ans">""" + r["detail"] + """</p>
  <p class="ans">""" + ex["context"] + """</p>""" + alt + """
  <a class="bigbtn" href=\"""" + WA + """\" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> Report a change on WhatsApp</a>
  """ + faq_html(ex["faqs"]) + """
  <h2 class="sec">Related routes</h2>
  """ + related + """
  <a class="siglink" href=\"""" + sig["page"] + """\"><span class="tile"><i class="fa-solid fa-tower-cell"></i></span>Which SIM works in """ + sig["short"] + """?<span class="chev"><i class="fa-solid fa-arrow-right"></i></span></a>
  """ + GBCARD + FOOT + "</div>" + NAV
    html = head(ex["title"], desc, canonical, faq_jsonld(ex["faqs"])) + body
    return html.replace("</body>", route_script(r) + "\n</body>")


def signal_page(key, s, routes_by_id):
    canonical = BASE + "/" + s["page"]
    title = "Which SIM Works in " + s["short"] + "? SCOM, Zong, Jazz Coverage — North Live"
    desc = ("Which SIM works in " + s["short"] + "? SCOM, Zong, Jazz, Telenor and Ufone coverage in " +
            s["place"] + " compared — 4G availability, the best network and the dead zones. North Live, November 2026.")
    rows = ""
    for name, bars, note in s["carriers"]:
        bt = "No signal" if bars == 0 else str(bars) + "/4 bars"
        rows += ('<div class="srow"><span class="ct">' + name[0] + '</span><div><div class="nm">' + name +
                 '</div><div class="nt">' + note + '</div></div><div class="br"><span class="bars">' +
                 bars_html(bars) + '</span><div class="bt' + (" no" if bars == 0 else "") + '">' + bt + "</div></div></div>")
    rel_routes = "\n".join(route_row_link(routes_by_id[i]) for i in s["routes"])
    others = ""
    for k2, s2 in SIGNALS.items():
        if k2 != key:
            others += ('\n  <a class="siglink" href="' + s2["page"] + '"><span class="tile"><i class="fa-solid fa-tower-cell"></i></span>Which SIM works in ' +
                       s2["short"] + '?<span class="chev"><i class="fa-solid fa-arrow-right"></i></span></a>')
    body = shell_open() + """
  <p class="crumb">Mobile signal guide · Northern Pakistan</p>
  <h1 class="q">Which SIM Works in """ + s["short"] + """?</h1>
  <div class="quickbox"><b>QUICK ANSWER</b>""" + s["quick"] + """</div>
  <p class="ans">""" + s["intro"] + """</p>
  <div class="sigcard">""" + rows + """
  </div>
  <a class="bigbtn" href=\"""" + WA + """\" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> Report signal in """ + s["short"] + """</a>
  """ + faq_html(s["faqs"]) + """
  <h2 class="sec">Road status near """ + s["short"] + """</h2>
  """ + rel_routes + """
  <h2 class="sec">Signal in other places</h2>""" + others + """
  """ + GBCARD + FOOT + "</div>" + NAV
    return head(title, desc, canonical, faq_jsonld(s["faqs"])) + body


def main():
    with open(os.path.join(HERE, "data.json"), encoding="utf-8") as f:
        data = json.load(f)
    routes_by_id = {r["id"]: r for r in data["routes"]}
    made = []
    for r in data["routes"]:
        fn = r["slug"] + "-road-status.html"
        with open(os.path.join(HERE, fn), "w", encoding="utf-8") as f:
            f.write(route_page(r, routes_by_id))
        made.append(fn)
    for key, s in SIGNALS.items():
        with open(os.path.join(HERE, s["page"]), "w", encoding="utf-8") as f:
            f.write(signal_page(key, s, routes_by_id))
        made.append(s["page"])
    urls = [BASE + "/"] + [BASE + "/" + fn for fn in made]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append("<url><loc>" + u + "</loc><lastmod>" + LASTMOD + "</lastmod></url>")
    sm.append("</urlset>")
    with open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm) + "\n")
    with open(os.path.join(HERE, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: " + BASE + "/sitemap.xml\n")
    print("generated:", len(made), "pages + sitemap.xml + robots.txt")
    for fn in made:
        print(" ", fn, os.path.getsize(os.path.join(HERE, fn)), "bytes")


if __name__ == "__main__":
    main()
