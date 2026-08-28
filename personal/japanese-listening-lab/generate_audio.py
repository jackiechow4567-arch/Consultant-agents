#!/usr/bin/env python3
"""Generate Japanese neural TTS clips and lessons.js for the listening lab."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent
AUDIO = ROOT / "audio"
VOICE = {
    "nanami": "ja-JP-NanamiNeural",
    "keita": "ja-JP-KeitaNeural",
}


def ruby(kanji: str, kana: str) -> str:
    return f"<ruby>{kanji}<rt>{kana}</rt></ruby>"


# Original learner clips (not copied from textbooks or news).
LESSONS: list[dict] = [
    # --- N5 daily ---
    {
        "id": "n5-01",
        "track": "n5",
        "title": "Morning",
        "voice": "nanami",
        "jp": "おはようございます。今日はいい天気ですね。",
        "kana": "おはようございます。きょうはいいてんきですね。",
        "ruby": f"おはようございます。{ruby('今日', 'きょう')}はいい{ruby('天気', 'てんき')}ですね。",
        "en": "Good morning. The weather is nice today.",
        "quiz": {
            "q": "What is the speaker commenting on?",
            "choices": ["The weather", "The train", "Lunch", "A meeting"],
            "answer": 0,
        },
    },
    {
        "id": "n5-02",
        "track": "n5",
        "title": "Where is the station?",
        "voice": "keita",
        "jp": "すみません、駅はどこですか。",
        "kana": "すみません、えきはどこですか。",
        "ruby": f"すみません、{ruby('駅', 'えき')}はどこですか。",
        "en": "Excuse me, where is the station?",
        "quiz": {
            "q": "What is the speaker looking for?",
            "choices": ["A hotel", "The station", "A bank", "A hospital"],
            "answer": 1,
        },
    },
    {
        "id": "n5-03",
        "track": "n5",
        "title": "How much?",
        "voice": "nanami",
        "jp": "このパンはいくらですか。三百円です。",
        "kana": "このぱんはいくらですか。さんびゃくえんです。",
        "ruby": f"このパンはいくらですか。{ruby('三百円', 'さんびゃくえん')}です。",
        "en": "How much is this bread? It is 300 yen.",
        "quiz": {
            "q": "How much is the bread?",
            "choices": ["100 yen", "200 yen", "300 yen", "500 yen"],
            "answer": 2,
        },
    },
    {
        "id": "n5-04",
        "track": "n5",
        "title": "Water please",
        "voice": "keita",
        "jp": "水を一杯ください。",
        "kana": "みずをいっぱいください。",
        "ruby": f"{ruby('水', 'みず')}を{ruby('一杯', 'いっぱい')}ください。",
        "en": "One glass of water, please.",
        "quiz": {
            "q": "What does the speaker want?",
            "choices": ["Tea", "Coffee", "Water", "Juice"],
            "answer": 2,
        },
    },
    {
        "id": "n5-05",
        "track": "n5",
        "title": "What time?",
        "voice": "nanami",
        "jp": "今、何時ですか。三時半です。",
        "kana": "いま、なんじですか。さんじはんです。",
        "ruby": f"{ruby('今', 'いま')}、{ruby('何時', 'なんじ')}ですか。{ruby('三時半', 'さんじはん')}です。",
        "en": "What time is it now? It is 3:30.",
        "quiz": {
            "q": "What time is it?",
            "choices": ["2:00", "3:00", "3:30", "4:30"],
            "answer": 2,
        },
    },
    {
        "id": "n5-06",
        "track": "n5",
        "title": "Work tomorrow",
        "voice": "keita",
        "jp": "明日は仕事があります。",
        "kana": "あしたはしごとがあります。",
        "ruby": f"{ruby('明日', 'あした')}は{ruby('仕事', 'しごと')}があります。",
        "en": "I have work tomorrow.",
        "quiz": {
            "q": "When does the speaker have work?",
            "choices": ["Today", "Tomorrow", "Next week", "Tonight"],
            "answer": 1,
        },
    },
    {
        "id": "n5-07",
        "track": "n5",
        "title": "Train delay",
        "voice": "nanami",
        "jp": "電車が遅れています。",
        "kana": "でんしゃがおくれています。",
        "ruby": f"{ruby('電車', 'でんしゃ')}が{ruby('遅', 'おく')}れています。",
        "en": "The train is running late.",
        "quiz": {
            "q": "What is happening?",
            "choices": ["The train is early", "The train is late", "The bus is full", "The shop is closed"],
            "answer": 1,
        },
    },
    {
        "id": "n5-08",
        "track": "n5",
        "title": "This is delicious",
        "voice": "keita",
        "jp": "これはおいしいです。何という料理ですか。",
        "kana": "これはおいしいです。なんというりょうりですか。",
        "ruby": f"これはおいしいです。{ruby('何', 'なん')}という{ruby('料理', 'りょうり')}ですか。",
        "en": "This is delicious. What dish is this called?",
        "quiz": {
            "q": "What is the speaker asking about?",
            "choices": ["The price", "The name of the dish", "The wait time", "The ingredients only"],
            "answer": 1,
        },
    },
    {
        "id": "n5-09",
        "track": "n5",
        "title": "Nice to meet you",
        "voice": "nanami",
        "jp": "名前は田中です。よろしくお願いします。",
        "kana": "なまえはたなかです。よろしくおねがいします。",
        "ruby": f"{ruby('名前', 'なまえ')}は{ruby('田中', 'たなか')}です。よろしく{ruby('願', 'ねが')}いします。",
        "en": "My name is Tanaka. Nice to meet you.",
        "quiz": {
            "q": "What is the speaker's name?",
            "choices": ["Sato", "Tanaka", "Suzuki", "Yamamoto"],
            "answer": 1,
        },
    },
    {
        "id": "n5-10",
        "track": "n5",
        "title": "Tired today",
        "voice": "keita",
        "jp": "今日は疲れました。早く寝ます。",
        "kana": "きょうはつかれました。はやくねます。",
        "ruby": f"{ruby('今日', 'きょう')}は{ruby('疲', 'つか')}れました。{ruby('早', 'はや')}く{ruby('寝', 'ね')}ます。",
        "en": "I got tired today. I will go to bed early.",
        "quiz": {
            "q": "What will the speaker do?",
            "choices": ["Work late", "Go out", "Go to bed early", "Cook dinner"],
            "answer": 2,
        },
    },
    # --- N4 daily ---
    {
        "id": "n4-01",
        "track": "n4",
        "title": "Are you free?",
        "voice": "nanami",
        "jp": "来週の火曜日、空いていますか。",
        "kana": "らいしゅうのかようび、あいていますか。",
        "ruby": f"{ruby('来週', 'らいしゅう')}の{ruby('火曜日', 'かようび')}、{ruby('空', 'あ')}いていますか。",
        "en": "Are you free next Tuesday?",
        "quiz": {
            "q": "Which day is being asked about?",
            "choices": ["This Tuesday", "Next Tuesday", "Next Thursday", "Next Sunday"],
            "answer": 1,
        },
    },
    {
        "id": "n4-02",
        "track": "n4",
        "title": "Directions",
        "voice": "keita",
        "jp": "この道をまっすぐ行って、二つ目の信号を右に曲がってください。",
        "kana": "このみちをまっすぐいって、ふたつめのしんごうをみぎにまがってください。",
        "ruby": f"この{ruby('道', 'みち')}をまっすぐ{ruby('行', 'い')}って、{ruby('二つ目', 'ふたつめ')}の{ruby('信号', 'しんごう')}を{ruby('右', 'みぎ')}に{ruby('曲', 'ま')}がってください。",
        "en": "Go straight on this road, then turn right at the second traffic light.",
        "quiz": {
            "q": "Where should you turn right?",
            "choices": ["The first light", "The second light", "The station", "The corner shop"],
            "answer": 1,
        },
    },
    {
        "id": "n4-03",
        "track": "n4",
        "title": "Restaurant booking",
        "voice": "nanami",
        "jp": "予約をしたいのですが、六時から四人でお願いします。",
        "kana": "よやくをしたいのですが、ろくじからよにんでおねがいします。",
        "ruby": f"{ruby('予約', 'よやく')}をしたいのですが、{ruby('六時', 'ろくじ')}から{ruby('四人', 'よにん')}でお{ruby('願', 'ねが')}いします。",
        "en": "I would like to make a reservation for four people from 6 o'clock.",
        "quiz": {
            "q": "How many people is the booking for?",
            "choices": ["Two", "Three", "Four", "Six"],
            "answer": 2,
        },
    },
    {
        "id": "n4-04",
        "track": "n4",
        "title": "Phone number",
        "voice": "keita",
        "jp": "電話番号を教えていただけますか。",
        "kana": "でんわばんごうをおしえていただけますか。",
        "ruby": f"{ruby('電話番号', 'でんわばんごう')}を{ruby('教', 'おし')}えていただけますか。",
        "en": "Could you tell me your phone number?",
        "quiz": {
            "q": "What is the speaker asking for?",
            "choices": ["An address", "A phone number", "An email", "A name card"],
            "answer": 1,
        },
    },
    {
        "id": "n4-05",
        "track": "n4",
        "title": "Movie with a friend",
        "voice": "nanami",
        "jp": "昨日、友達と映画を見に行きました。とても面白かったです。",
        "kana": "きのう、ともだちとえいがをみにいきました。とてもおもしろかったです。",
        "ruby": f"{ruby('昨日', 'きのう')}、{ruby('友達', 'ともだち')}と{ruby('映画', 'えいが')}を{ruby('見', 'み')}に{ruby('行', 'い')}きました。とても{ruby('面白', 'おもしろ')}かったです。",
        "en": "Yesterday I went to see a movie with a friend. It was very interesting.",
        "quiz": {
            "q": "What did the speaker do yesterday?",
            "choices": ["Cooked at home", "Saw a movie", "Went to work late", "Took a train trip"],
            "answer": 1,
        },
    },
    {
        "id": "n4-06",
        "track": "n4",
        "title": "Heavy luggage",
        "voice": "keita",
        "jp": "荷物が重くて、一人では持てません。",
        "kana": "にもつがおもくて、ひとりではもてません。",
        "ruby": f"{ruby('荷物', 'にもつ')}が{ruby('重', 'おも')}くて、{ruby('一人', 'ひとり')}では{ruby('持', 'も')}てません。",
        "en": "The luggage is heavy, so I cannot carry it by myself.",
        "quiz": {
            "q": "Why is there a problem?",
            "choices": ["The bag is lost", "The luggage is heavy", "The train is late", "The shop is closed"],
            "answer": 1,
        },
    },
    {
        "id": "n4-07",
        "track": "n4",
        "title": "Wrong train",
        "voice": "nanami",
        "jp": "電車を乗り間違えて、一駅行き過ぎてしまいました。",
        "kana": "でんしゃをのりまちがえて、ひとえきいきすぎてしまいました。",
        "ruby": f"{ruby('電車', 'でんしゃ')}を{ruby('乗', 'の')}り{ruby('間違', 'まちが')}えて、{ruby('一駅', 'ひとえき')}{ruby('行', 'い')}き{ruby('過', 'す')}ぎてしまいました。",
        "en": "I took the wrong train and went one station too far.",
        "quiz": {
            "q": "What happened?",
            "choices": ["Missed the last train", "Went one stop too far", "Lost a ticket", "The train stopped"],
            "answer": 1,
        },
    },
    {
        "id": "n4-08",
        "track": "n4",
        "title": "Fever, taking a day off",
        "voice": "keita",
        "jp": "熱があるので、今日は休みます。",
        "kana": "ねつがあるので、きょうはやすみます。",
        "ruby": f"{ruby('熱', 'ねつ')}があるので、{ruby('今日', 'きょう')}は{ruby('休', 'やす')}みます。",
        "en": "I have a fever, so I will take today off.",
        "quiz": {
            "q": "Why is the speaker taking the day off?",
            "choices": ["A meeting was cancelled", "A fever", "A trip", "Overtime yesterday"],
            "answer": 1,
        },
    },
    {
        "id": "n4-09",
        "track": "n4",
        "title": "Coffee or tea",
        "voice": "nanami",
        "jp": "コーヒーと紅茶、どちらがいいですか。コーヒーをお願いします。",
        "kana": "コーヒーとこうちゃ、どちらがいいですか。コーヒーをおねがいします。",
        "ruby": f"コーヒーと{ruby('紅茶', 'こうちゃ')}、どちらがいいですか。コーヒーをお{ruby('願', 'ねが')}いします。",
        "en": "Would you like coffee or tea? Coffee, please.",
        "quiz": {
            "q": "What did the person choose?",
            "choices": ["Tea", "Water", "Coffee", "Juice"],
            "answer": 2,
        },
    },
    {
        "id": "n4-10",
        "track": "n4",
        "title": "Weekend in Kyoto",
        "voice": "keita",
        "jp": "週末は京都へ行くつもりです。お寺を回りたいです。",
        "kana": "しゅうまつはきょうとへいくつもりです。おてらをまわりたいです。",
        "ruby": f"{ruby('週末', 'しゅうまつ')}は{ruby('京都', 'きょうと')}へ{ruby('行', 'い')}くつもりです。お{ruby('寺', 'てら')}を{ruby('回', 'まわ')}りたいです。",
        "en": "I plan to go to Kyoto this weekend. I want to visit temples.",
        "quiz": {
            "q": "What does the speaker want to do in Kyoto?",
            "choices": ["Shop for clothes", "Visit temples", "Watch baseball", "Work in an office"],
            "answer": 1,
        },
    },
    # --- N3 work ---
    {
        "id": "n3-01",
        "track": "n3",
        "title": "Online meeting",
        "voice": "nanami",
        "jp": "本日の会議は三時から、オンラインで行います。資料は事前に共有します。",
        "kana": "ほんじつのかいぎはさんじから、オンラインでおこないます。しりょうはじぜんにきょうゆうします。",
        "ruby": f"{ruby('本日', 'ほんじつ')}の{ruby('会議', 'かいぎ')}は{ruby('三時', 'さんじ')}から、オンラインで{ruby('行', 'おこな')}います。{ruby('資料', 'しりょう')}は{ruby('事前', 'じぜん')}に{ruby('共有', 'きょうゆう')}します。",
        "en": "Today's meeting starts at 3:00 online. I will share the materials in advance.",
        "quiz": {
            "q": "How will the meeting be held?",
            "choices": ["In person only", "Online", "By phone only", "It was cancelled"],
            "answer": 1,
        },
    },
    {
        "id": "n3-02",
        "track": "n3",
        "title": "Did you check the email?",
        "voice": "keita",
        "jp": "先日お送りしたメール、ご確認いただけましたでしょうか。",
        "kana": "せんじつおおくりしたメール、ごかくにんいただけましたでしょうか。",
        "ruby": f"{ruby('先日', 'せんじつ')}お{ruby('送', 'おく')}りしたメール、ご{ruby('確認', 'かくにん')}いただけましたでしょうか。",
        "en": "Were you able to review the email I sent the other day?",
        "quiz": {
            "q": "What is the speaker following up on?",
            "choices": ["A phone call", "An email", "A contract signing", "A flight"],
            "answer": 1,
        },
    },
    {
        "id": "n3-03",
        "track": "n3",
        "title": "Two-city trip",
        "voice": "nanami",
        "jp": "来月の出張は、東京と大阪の二都市です。日程を調整しましょう。",
        "kana": "らいげつのしゅっちょうは、とうきょうとおおさかのにとしです。にっていをちょうせいしましょう。",
        "ruby": f"{ruby('来月', 'らいげつ')}の{ruby('出張', 'しゅっちょう')}は、{ruby('東京', 'とうきょう')}と{ruby('大阪', 'おおさか')}の{ruby('二都市', 'にとし')}です。{ruby('日程', 'にってい')}を{ruby('調整', 'ちょうせい')}しましょう。",
        "en": "Next month's business trip covers two cities, Tokyo and Osaka. Let's align the schedule.",
        "quiz": {
            "q": "Which cities are in the trip?",
            "choices": ["Tokyo and Kyoto", "Osaka and Nagoya", "Tokyo and Osaka", "Sapporo and Tokyo"],
            "answer": 2,
        },
    },
    {
        "id": "n3-04",
        "track": "n3",
        "title": "Decide by next week",
        "voice": "keita",
        "jp": "本件については、来週までに方針を決めたいと思います。",
        "kana": "ほんけんについては、らいしゅうまでにほうしんをきめたいとおもいます。",
        "ruby": f"{ruby('本件', 'ほんけん')}については、{ruby('来週', 'らいしゅう')}までに{ruby('方針', 'ほうしん')}を{ruby('決', 'き')}めたいと{ruby('思', 'おも')}います。",
        "en": "For this matter, I would like to decide the direction by next week.",
        "quiz": {
            "q": "When does the speaker want a decision?",
            "choices": ["Today", "By next week", "Next month", "After the holiday"],
            "answer": 1,
        },
    },
    {
        "id": "n3-05",
        "track": "n3",
        "title": "Polite follow-up",
        "voice": "nanami",
        "jp": "ご多忙のところ恐れ入りますが、ご返信をお願いできますでしょうか。",
        "kana": "ごたぼうのところおそれいりますが、ごへんしんをおねがいできますでしょうか。",
        "ruby": f"ご{ruby('多忙', 'たぼう')}のところ{ruby('恐', 'おそ')}れ{ruby('入', 'い')}りますが、ご{ruby('返信', 'へんしん')}をお{ruby('願', 'ねが')}いできますでしょうか。",
        "en": "Sorry to bother you when you are busy, but could I ask for a reply?",
        "quiz": {
            "q": "What is being requested?",
            "choices": ["A meeting room", "A reply", "A discount", "A signature stamp"],
            "answer": 1,
        },
    },
    {
        "id": "n3-06",
        "track": "n3",
        "title": "Numbers later",
        "voice": "keita",
        "jp": "数字の説明は後ほどいたします。まずは全体の流れをご覧ください。",
        "kana": "すうじのせつめいはのちほどいたします。まずはぜんたいのながれをごらんください。",
        "ruby": f"{ruby('数字', 'すうじ')}の{ruby('説明', 'せつめい')}は{ruby('後', 'のち')}ほどいたします。まずは{ruby('全体', 'ぜんたい')}の{ruby('流', 'なが')}れをご{ruby('覧', 'らん')}ください。",
        "en": "I will explain the numbers later. Please look at the overall flow first.",
        "quiz": {
            "q": "What should the listener look at first?",
            "choices": ["The numbers", "The overall flow", "The appendix", "The invoice"],
            "answer": 1,
        },
    },
    {
        "id": "n3-07",
        "track": "n3",
        "title": "Meeting moved",
        "voice": "nanami",
        "jp": "先方の都合がつかないため、打ち合わせを金曜日に変更しました。",
        "kana": "せんぽうのつごうがつかないため、うちあわせをきんようびにへんこうしました。",
        "ruby": f"{ruby('先方', 'せんぽう')}の{ruby('都合', 'つごう')}がつかないため、{ruby('打', 'う')}ち{ruby('合', 'あ')}わせを{ruby('金曜日', 'きんようび')}に{ruby('変更', 'へんこう')}しました。",
        "en": "The other side was not available, so I moved the meeting to Friday.",
        "quiz": {
            "q": "When is the meeting now?",
            "choices": ["Monday", "Wednesday", "Friday", "Sunday"],
            "answer": 2,
        },
    },
    {
        "id": "n3-08",
        "track": "n3",
        "title": "Thank you for your time",
        "voice": "keita",
        "jp": "本日はお時間をいただき、ありがとうございました。引き続きよろしくお願いいたします。",
        "kana": "ほんじつはおじかんをいただき、ありがとうございました。ひきつづきよろしくおねがいいたします。",
        "ruby": f"{ruby('本日', 'ほんじつ')}はお{ruby('時間', 'じかん')}をいただき、ありがとうございました。{ruby('引', 'ひ')}き{ruby('続', 'つづ')}きよろしくお{ruby('願', 'ねが')}いいたします。",
        "en": "Thank you for your time today. I look forward to continuing to work together.",
        "quiz": {
            "q": "What is the tone of this line?",
            "choices": ["A complaint", "A closing thanks", "A price negotiation", "A cancellation"],
            "answer": 1,
        },
    },
    # --- Healthcare / clinic Japanese (generic, no real names or products) ---
    {
        "id": "med-01",
        "track": "med",
        "title": "Explain how to use",
        "voice": "nanami",
        "jp": "先生、本日はお薬の使い方について、簡単にご説明いたします。",
        "kana": "せんせい、ほんじつはおくすりのつかいかたについて、かんたんにごせつめいいたします。",
        "ruby": f"{ruby('先生', 'せんせい')}、{ruby('本日', 'ほんじつ')}はお{ruby('薬', 'くすり')}の{ruby('使', 'つか')}い{ruby('方', 'かた')}について、{ruby('簡単', 'かんたん')}にご{ruby('説明', 'せつめい')}いたします。",
        "en": "Doctor, today I will briefly explain how to use the medicine.",
        "quiz": {
            "q": "What will be explained?",
            "choices": ["Hospital visiting hours", "How to use the medicine", "Insurance only", "A surgery date"],
            "answer": 1,
        },
    },
    {
        "id": "med-02",
        "track": "med",
        "title": "Used in blood diseases",
        "voice": "keita",
        "jp": "このお薬は、血液の病気の治療に使われることがあります。",
        "kana": "このおくすりは、けつえきのびょうきのちりょうにつかわれることがあります。",
        "ruby": f"このお{ruby('薬', 'くすり')}は、{ruby('血液', 'けつえき')}の{ruby('病気', 'びょうき')}の{ruby('治療', 'ちりょう')}に{ruby('使', 'つか')}われることがあります。",
        "en": "This medicine is sometimes used in the treatment of blood diseases.",
        "quiz": {
            "q": "What kind of illness is mentioned?",
            "choices": ["A cold", "Blood diseases", "A broken bone", "Skin allergy only"],
            "answer": 1,
        },
    },
    {
        "id": "med-03",
        "track": "med",
        "title": "Main side effects",
        "voice": "nanami",
        "jp": "主な副作用として、発熱やだるさが出ることがあります。",
        "kana": "おもなふくさようとして、はつねつやだるさがでることがあります。",
        "ruby": f"{ruby('主', 'おも')}な{ruby('副作用', 'ふくさよう')}として、{ruby('発熱', 'はつねつ')}やだるさが{ruby('出', 'で')}ることがあります。",
        "en": "The main side effects can include fever and fatigue.",
        "quiz": {
            "q": "Which side effects are named?",
            "choices": ["Cough and rash", "Fever and fatigue", "Hair loss only", "No side effects"],
            "answer": 1,
        },
    },
    {
        "id": "med-04",
        "track": "med",
        "title": "Rest after injection",
        "voice": "keita",
        "jp": "注射のあと、しばらく安静にしてください。",
        "kana": "ちゅうしゃのあと、しばらくあんせいにしてください。",
        "ruby": f"{ruby('注射', 'ちゅうしゃ')}のあと、しばらく{ruby('安静', 'あんせい')}にしてください。",
        "en": "After the injection, please rest for a while.",
        "quiz": {
            "q": "What should the listener do after the injection?",
            "choices": ["Go running", "Rest for a while", "Eat a large meal immediately", "Drive at once"],
            "answer": 1,
        },
    },
    {
        "id": "med-05",
        "track": "med",
        "title": "Next visit in two weeks",
        "voice": "nanami",
        "jp": "次回の診察は二週間後になります。ご都合はいかがですか。",
        "kana": "じかいのしんさつはにしゅうかんごになります。ごつごうはいかがですか。",
        "ruby": f"{ruby('次回', 'じかい')}の{ruby('診察', 'しんさつ')}は{ruby('二週間後', 'にしゅうかんご')}になります。ご{ruby('都合', 'つごう')}はいかがですか。",
        "en": "The next consultation will be in two weeks. How is your schedule?",
        "quiz": {
            "q": "When is the next visit?",
            "choices": ["Tomorrow", "In two days", "In two weeks", "In two months"],
            "answer": 2,
        },
    },
    {
        "id": "med-06",
        "track": "med",
        "title": "Results next week",
        "voice": "keita",
        "jp": "検査の結果は、来週改めてご説明します。",
        "kana": "けんさのけっかは、らいしゅうあらためてごせつめいします。",
        "ruby": f"{ruby('検査', 'けんさ')}の{ruby('結果', 'けっか')}は、{ruby('来週', 'らいしゅう')}{ruby('改', 'あらた')}めてご{ruby('説明', 'せつめい')}します。",
        "en": "I will explain the test results again next week.",
        "quiz": {
            "q": "When will the results be explained?",
            "choices": ["Today", "Tomorrow morning", "Next week", "Next year"],
            "answer": 2,
        },
    },
    {
        "id": "med-07",
        "track": "med",
        "title": "Please ask anytime",
        "voice": "nanami",
        "jp": "ご不明な点がございましたら、いつでもご質問ください。",
        "kana": "ごふめいなてんがございましたら、いつでもごしつもんください。",
        "ruby": f"ご{ruby('不明', 'ふめい')}な{ruby('点', 'てん')}がございましたら、いつでもご{ruby('質問', 'しつもん')}ください。",
        "en": "If anything is unclear, please ask a question at any time.",
        "quiz": {
            "q": "What is the listener invited to do?",
            "choices": ["Leave immediately", "Ask questions", "Sign a form", "Pay now"],
            "answer": 1,
        },
    },
    {
        "id": "med-08",
        "track": "med",
        "title": "Contact if symptoms appear",
        "voice": "keita",
        "jp": "安全が第一です。気になる症状があれば、すぐにご連絡ください。",
        "kana": "あんぜんがだいいちです。きになるしょうじょうがあれば、すぐにごれんらくください。",
        "ruby": f"{ruby('安全', 'あんぜん')}が{ruby('第一', 'だいいち')}です。{ruby('気', 'き')}になる{ruby('症状', 'しょうじょう')}があれば、すぐにご{ruby('連絡', 'れんらく')}ください。",
        "en": "Safety comes first. If any symptoms concern you, please contact us right away.",
        "quiz": {
            "q": "What should you do if symptoms are worrying?",
            "choices": ["Wait a month", "Search online only", "Contact them right away", "Stop all daily activity"],
            "answer": 2,
        },
    },
]


def export_payload(lessons: list[dict]) -> list[dict]:
    out = []
    for item in lessons:
        out.append(
            {
                "id": item["id"],
                "track": item["track"],
                "title": item["title"],
                "jp": item["jp"],
                "kana": item["kana"],
                "ruby": item["ruby"],
                "en": item["en"],
                "audio": f"audio/{item['id']}.mp3",
                "quiz": item["quiz"],
            }
        )
    return out


async def synth_one(item: dict, sem: asyncio.Semaphore) -> None:
    dest = AUDIO / f"{item['id']}.mp3"
    async with sem:
        communicate = edge_tts.Communicate(
            item["jp"],
            VOICE[item["voice"]],
            rate="-10%",
        )
        await communicate.save(str(dest))
        print(f"wrote {dest.name}")


async def main() -> None:
    AUDIO.mkdir(parents=True, exist_ok=True)
    sem = asyncio.Semaphore(4)
    await asyncio.gather(*(synth_one(item, sem) for item in LESSONS))
    payload = export_payload(LESSONS)
    js = ROOT / "lessons.js"
    js.write_text(
        "window.LESSONS = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )
    print(f"wrote {js.name} ({len(payload)} clips)")


if __name__ == "__main__":
    asyncio.run(main())
