#!/usr/bin/python
# -*- coding: utf-8 -*-

JOB_WARRIOR = 0
JOB_KNIGHT = 4
JOB_ARCHER = 1
JOB_MAGICIAN = 2
JOB_PRIEST = 3
TYPE_CARD = 0
TYPE_WEAPON_EV = 1
TYPE_WEAPON_RF = 2
TYPE_CHARA_RF = 3

itemList = [  
  {'id': 10, 'name': 'Gold'},
  {'id': 11, 'name': 'AC'},
]

stoneList = [
  {'id': 0, 'name': '精靈石'},
]

gachaList = [
  {'id': 4, 'type': 0, 'job': 0, 'name': '“龍殺し”ヴォルグ', 'lv': 4, 'autosell': 0},
  {'id': 5, 'type': 0, 'job': 4, 'name': '鉄仮面の剣士アルヴェルト', 'lv': 4, 'autosell': 0},
  {'id': 6, 'type': 0, 'job': 4, 'name': '歷戦の女傭兵ロベルタ', 'lv': 1, 'autosell': 1},
  {'id': 7, 'type': 0, 'job': 0, 'name': '黒き鋭刃リュビア', 'lv': 3, 'autosell': 0},
  {'id': 8, 'type': 0, 'job': 0, 'name': '軽足の傭兵カルロ', 'lv': 1, 'autosell': 1},
  {'id': 9, 'type': 0, 'job': 4, 'name': '百戦の勇士スレイ', 'lv': 3, 'autosell': 0},
  {'id': 10, 'type': 0, 'job': 4, 'name': '無敵の守銭奴メリッサ', 'lv': 2, 'autosell': 1},
  {'id': 11, 'type': 0, 'job': 0, 'name': 'みならい戦士エディ', 'lv': 1, 'autosell': 1},
  {'id': 12, 'type': 0, 'job': 0, 'name': '復讐に燃える戦士グレッグ', 'lv': 1, 'autosell': 1},
  {'id': 13, 'type': 0, 'job': 4, 'name': '自称英雄アルベルト', 'lv': 2, 'autosell': 1},
  {'id': 15, 'type': 0, 'job': 0, 'name': '微笑む悪魔アンジェリカ', 'lv': 4, 'autosell': 0},
  {'id': 16, 'type': 0, 'job': 1, 'name': '無垢の暗殺者ニーナ', 'lv': 5, 'autosell': 0},
  {'id': 17, 'type': 0, 'job': 0, 'name': 'お調子者フランツ', 'lv': 3, 'autosell': 0},
  {'id': 18, 'type': 0, 'job': 1, 'name': '無面の暗殺者フェイスレス', 'lv': 3, 'autosell': 0},
  {'id': 19, 'type': 0, 'job': 1, 'name': '森の王者フィリップ', 'lv': 4, 'autosell': 0},
  {'id': 20, 'type': 0, 'job': 0, 'name': '王都の勇士キリエ', 'lv': 3, 'autosell': 0},
  {'id': 21, 'type': 0, 'job': 1, 'name': '魔境の案内人エマ', 'lv': 3, 'autosell': 0},
  {'id': 22, 'type': 0, 'job': 2, 'name': '万象の魔導師アルドラ', 'lv': 5, 'autosell': 0},
  {'id': 23, 'type': 0, 'job': 0, 'name': '破壊魔人ロレッタ', 'lv': 5, 'autosell': 0},
  {'id': 24, 'type': 0, 'job': 0, 'name': '死の商人アイアリス', 'lv': 3, 'autosell': 0},
  {'id': 25, 'type': 0, 'job': 0, 'name': '熱血武器商人ダスティ', 'lv': 2, 'autosell': 1},
  {'id': 26, 'type': 0, 'job': 1, 'name': 'うら若き商才エンヴィ', 'lv': 3, 'autosell': 0},
  {'id': 27, 'type': 0, 'job': 1, 'name': '慈悲の商人パトリシア', 'lv': 2, 'autosell': 1},
  {'id': 29, 'type': 0, 'job': 2, 'name': '法務委員ビルギット', 'lv': 3, 'autosell': 0},
  {'id': 30, 'type': 0, 'job': 1, 'name': '外交委員オットー', 'lv': 1, 'autosell': 1},
  {'id': 31, 'type': 0, 'job': 3, 'name': '秘薬師メルヴィナ', 'lv': 3, 'autosell': 0},
  {'id': 32, 'type': 0, 'job': 1, 'name': '魔法弓士コロナ', 'lv': 3, 'autosell': 0},
  {'id': 33, 'type': 0, 'job': 4, 'name': '軟派騎士ナックル', 'lv': 1, 'autosell': 1},
  {'id': 34, 'type': 0, 'job': 3, 'name': '熱き癒し手マリナ', 'lv': 1, 'autosell': 1},
  {'id': 35, 'type': 0, 'job': 3, 'name': '若き癒し手カトリ', 'lv': 1, 'autosell': 1},
  {'id': 36, 'type': 0, 'job': 3, 'name': '白の癒し手ラティ', 'lv': 2, 'autosell': 1},
  {'id': 37, 'type': 0, 'job': 4, 'name': '俊足の剣士ラビィ', 'lv': 3, 'autosell': 0},
  {'id': 38, 'type': 0, 'job': 0, 'name': '強運の戦士ニンファ', 'lv': 5, 'autosell': 0},
  {'id': 39, 'type': 0, 'job': 3, 'name': '不良治癒術師ヴァネッサ', 'lv': 4, 'autosell': 0},
  {'id': 40, 'type': 0, 'job': 4, 'name': '善良なる傭兵カイン', 'lv': 1, 'autosell': 1},
  {'id': 41, 'type': 0, 'job': 1, 'name': '頼れる弓兵ミシディア', 'lv': 1, 'autosell': 1},
  {'id': 42, 'type': 0, 'job': 0, 'name': '飛天の遊撃手ジグムント', 'lv': 3, 'autosell': 0},
  {'id': 53, 'type': 0, 'job': 2, 'name': '早撃ちの狩人ワーグマン', 'lv': 2, 'autosell': 1},
  {'id': 1002, 'type': 0, 'job': 4, 'name': '聖王女ユリアナ', 'lv': 5, 'autosell': 0},
  {'id': 1004, 'type': 0, 'job': 4, 'name': '聖騎士団長“聖光の向日葵”リフレット', 'lv': 5, 'autosell': 0},
  {'id': 1005, 'type': 0, 'job': 4, 'name': '聖騎士団長“聖戦の呼び声”ダナディ', 'lv': 4, 'autosell': 0},
  {'id': 1006, 'type': 0, 'job': 4, 'name': '聖騎士団長“聖域の護り手”ウェイン', 'lv': 5, 'autosell': 0},
  {'id': 1007, 'type': 0, 'job': 4, 'name': '背徳の聖騎士イルヘルミナ', 'lv': 4, 'autosell': 0},
  {'id': 1008, 'type': 0, 'job': 4, 'name': '白百合の聖騎士ローエンディア', 'lv': 4, 'autosell': 0},
  {'id': 1009, 'type': 0, 'job': 4, 'name': '司祭騎士パーシェル', 'lv': 5, 'autosell': 0},
  {'id': 1010, 'type': 0, 'job': 4, 'name': '旅の聖騎士ライネル', 'lv': 3, 'autosell': 0},
  {'id': 1011, 'type': 0, 'job': 4, 'name': '旅の聖騎士カイ', 'lv': 3, 'autosell': 0},
  {'id': 1013, 'type': 0, 'job': 4, 'name': '“鋼鉄の血”騎士団長バクスト', 'lv': 1, 'autosell': 1},
  {'id': 1014, 'type': 0, 'job': 4, 'name': '“原初の鷹”騎士団長ハーマン', 'lv': 1, 'autosell': 1},
  {'id': 1015, 'type': 0, 'job': 4, 'name': '聖都の宿将セルバンテス', 'lv': 1, 'autosell': 1},
  {'id': 1019, 'type': 0, 'job': 3, 'name': '隠密神官ヨハン', 'lv': 3, 'autosell': 0},
  {'id': 1020, 'type': 0, 'job': 3, 'name': 'トラブルシスターケイト', 'lv': 2, 'autosell': 1},
  {'id': 1021, 'type': 0, 'job': 3, 'name': '聖都の良心アデル', 'lv': 4, 'autosell': 0},
  {'id': 1022, 'type': 0, 'job': 3, 'name': '放浪牧師ロイ', 'lv': 3, 'autosell': 0},
  {'id': 1023, 'type': 0, 'job': 3, 'name': '花の司祭アリエッタ', 'lv': 4, 'autosell': 0},
  {'id': 1024, 'type': 0, 'job': 4, 'name': '若き聖騎士マリス', 'lv': 3, 'autosell': 0},
  {'id': 1026, 'type': 0, 'job': 4, 'name': '“吸血の戦鬼”騎士団長ベアト', 'lv': 1, 'autosell': 1},
  {'id': 1027, 'type': 0, 'job': 4, 'name': '“悠久の丘”騎士団エリーナ', 'lv': 2, 'autosell': 1},
  {'id': 1028, 'type': 0, 'job': 4, 'name': '神託の聖騎士オデット', 'lv': 3, 'autosell': 0},
  {'id': 1029, 'type': 0, 'job': 4, 'name': '自由の騎士ディード', 'lv': 5, 'autosell': 0},
  {'id': 1031, 'type': 0, 'job': 4, 'name': '“清廉の泉”騎士団ルアンナ', 'lv': 2, 'autosell': 1},
  {'id': 2004, 'type': 0, 'job': 2, 'name': '三ツ星教授メラヒム', 'lv': 4, 'autosell': 0},
  {'id': 2005, 'type': 0, 'job': 2, 'name': ' 二ツ星教授イザヤ', 'lv': 4, 'autosell': 0},
  {'id': 2006, 'type': 0, 'job': 2, 'name': '二ツ星教授ヨナ', 'lv': 3, 'autosell': 0},
  {'id': 2007, 'type': 0, 'job': 2, 'name': '平凡なるメイドエレミア', 'lv': 4, 'autosell': 0},
  {'id': 2009, 'type': 0, 'job': 2, 'name': '穴掘り師カルデア', 'lv': 1, 'autosell': 1},
  {'id': 2010, 'type': 0, 'job': 2, 'name': '魔法兵団師団長ヴェルナー', 'lv': 5, 'autosell': 0},
  {'id': 2011, 'type': 0, 'job': 2, 'name': '魔法兵団師団長カティア', 'lv': 5, 'autosell': 0},
  {'id': 2012, 'type': 0, 'job': 2, 'name': '魔法兵団隊長クラウス', 'lv': 3, 'autosell': 0},
  {'id': 2013, 'type': 0, 'job': 2, 'name': '魔法兵団隊長フェブリア', 'lv': 4, 'autosell': 0},
  {'id': 2014, 'type': 0, 'job': 2, 'name': '魔法兵団隊長ユニ', 'lv': 5, 'autosell': 0},
  {'id': 2015, 'type': 0, 'job': 2, 'name': '魔法兵団フィオナ', 'lv': 3, 'autosell': 0},
  {'id': 2016, 'type': 0, 'job': 2, 'name': '魔法使い傭兵チャーノ', 'lv': 1, 'autosell': 1},
  {'id': 2017, 'type': 0, 'job': 2, 'name': '魔導ギルド団員ゲッベルツ', 'lv': 1, 'autosell': 1},
  {'id': 2018, 'type': 0, 'job': 2, 'name': '魔法兵団リーゼロッテ', 'lv': 2, 'autosell': 1},
  {'id': 2020, 'type': 0, 'job': 2, 'name': '魔法学園生徒クリスティン', 'lv': 1, 'autosell': 1},
  {'id': 2023, 'type': 0, 'job': 2, 'name': '双子魔法使いパルナ', 'lv': 2, 'autosell': 1},
  {'id': 2024, 'type': 0, 'job': 2, 'name': '双子魔法使いプルナ', 'lv': 2, 'autosell': 1},
  {'id': 2025, 'type': 0, 'job': 2, 'name': '魔法学園用務員ウーヴィア', 'lv': 3, 'autosell': 0},
  {'id': 2027, 'type': 0, 'job': 2, 'name': '氷の魔導人形イスレムラ', 'lv': 5, 'autosell': 0},
  {'id': 2029, 'type': 0, 'job': 2, 'name': '死出の案内人アイザック', 'lv': 3, 'autosell': 0},
  {'id': 2036, 'type': 0, 'job': 2, 'name': '候補生チアリー', 'lv': 5, 'autosell': 0},
  {'id': 2038, 'type': 0, 'job': 2, 'name': '候補生レベッカ', 'lv': 4, 'autosell': 0},
  {'id': 3003, 'type': 0, 'job': 0, 'name': '土妖精戦士団隊長エルダ', 'lv': 4, 'autosell': 0},
  {'id': 3005, 'type': 0, 'job': 0, 'name': 'お調子者フランツ', 'lv': 3, 'autosell': 0},
  {'id': 3008, 'type': 0, 'job': 0, 'name': '土妖精の商売人アイダ', 'lv': 3, 'autosell': 0},
  {'id': 3009, 'type': 0, 'job': 0, 'name': '土妖精戦士団エイダル', 'lv': 1, 'autosell': 1},
  {'id': 3012, 'type': 0, 'job': 0, 'name': '土妖精戦士団リンダ', 'lv': 2, 'autosell': 1},
  {'id': 3013, 'type': 0, 'job': 0, 'name': '刀匠ヨルデ', 'lv': 5, 'autosell': 0},
  {'id': 3016, 'type': 0, 'job': 2, 'name': '炎の料理人トト', 'lv': 3, 'autosell': 0},
  {'id': 3017, 'type': 0, 'job': 4, 'name': '炎の戦士ファン=ファン', 'lv': 4, 'autosell': 0},
  {'id': 3018, 'type': 0, 'job': 0, 'name': 'ぬるい炎キキ', 'lv': 5, 'autosell': 0},
  {'id': 3019, 'type': 0, 'job': 2, 'name': '小間使いヨッタ＝ヨッタ', 'lv': 1, 'autosell': 1},
  {'id': 3021, 'type': 0, 'job': 0, 'name': '泣き虫火妖精ヨヨ', 'lv': 2, 'autosell': 1},
  {'id': 4009, 'type': 0, 'job': 2, 'name': '人気詩人ナイエル', 'lv': 4, 'autosell': 0},
  {'id': 4010, 'type': 0, 'job': 0, 'name': 'みならい吟遊詩人ハサン', 'lv': 4, 'autosell': 0},
  {'id': 4011, 'type': 0, 'job': 2, 'name': 'みならい吟遊詩人ハキム', 'lv': 2, 'autosell': 1},
  {'id': 4014, 'type': 0, 'job': 2, 'name': '蛇つかいゴルネッサ', 'lv': 3, 'autosell': 0},
  {'id': 4015, 'type': 0, 'job': 1, 'name': '踊り子見習いニキ', 'lv': 3, 'autosell': 0},
  {'id': 4019, 'type': 0, 'job': 2, 'name': '占い師ネルヴァ', 'lv': 3, 'autosell': 0},
  {'id': 4020, 'type': 0, 'job': 4, 'name': '砂漠の鷹ジャファール', 'lv': 5, 'autosell': 0},
  {'id': 4021, 'type': 0, 'job': 4, 'name': '湖都の大盗賊ムスタファ', 'lv': 4, 'autosell': 0},
  {'id': 4027, 'type': 0, 'job': 0, 'name': '賭博師メフラム', 'lv': 1, 'autosell': 1},
  {'id': 4031, 'type': 0, 'job': 0, 'name': '女怪盗マディーナ', 'lv': 3, 'autosell': 0},
  {'id': 5007, 'type': 0, 'job': 4, 'name': '銀狼の導き手バリエナ', 'lv': 5, 'autosell': 0},
  {'id': 5011, 'type': 0, 'job': 0, 'name': '山猫の使いリンセ', 'lv': 5, 'autosell': 0},
  {'id': 5014, 'type': 0, 'job': 1, 'name': '千河の勇士ハジャダ', 'lv': 5, 'autosell': 0},
  {'id': 5022, 'type': 0, 'job': 3, 'name': '桜の樹人セレージャ', 'lv': 4, 'autosell': 0},
  {'id': 5024, 'type': 0, 'job': 3, 'name': '雪山の樹人パポラ', 'lv': 4, 'autosell': 0},
  {'id': 5025, 'type': 0, 'job': 0, 'name': 'お騒がせ三姉妹ディエス', 'lv': 3, 'autosell': 0},
  {'id': 5026, 'type': 0, 'job': 0, 'name': '千河の戦士ジェアダ', 'lv': 3, 'autosell': 0},
  {'id': 5028, 'type': 0, 'job': 2, 'name': '精霊の導きミニモ', 'lv': 3, 'autosell': 0},
  {'id': 6014, 'type': 0, 'job': 0, 'name': '歌舞伎者イヌチヨ', 'lv': 3, 'autosell': 0},
  {'id': 6021, 'type': 0, 'job': 0, 'name': '赤鬼の剣士バイセツ', 'lv': 3, 'autosell': 0},
  {'id': 6024, 'type': 0, 'job': 0, 'name': '宿命の剣士ハルアキ', 'lv': 3, 'autosell': 0},
  {'id': 6025, 'type': 0, 'job': 0, 'name': '宿命の剣士トウカ', 'lv': 4, 'autosell': 0},
  {'id': 7009, 'type': 0, 'job': 1, 'name': '復讐者クラリス', 'lv': 4, 'autosell': 0},
  {'id': 7010, 'type': 0, 'job': 0, 'name': '恋するお嬢様ベルナデット', 'lv': 4, 'autosell': 0},
  {'id': 7011, 'type': 0, 'job': 3, 'name': '盲目の神官ノエル', 'lv': 4, 'autosell': 0},
  {'id': 7013, 'type': 0, 'job': 0, 'name': '二刀の剣士イオ', 'lv': 4, 'autosell': 0},
  {'id': 7015, 'type': 0, 'job': 0, 'name': '主人公', 'lv': 3, 'autosell': 0},
  {'id': 7503, 'type': 0, 'job': 1, 'name': '冒涜の魔神カタリス', 'lv': 5, 'autosell': 0},
  {'id': 7504, 'type': 0, 'job': 0, 'name': '牢獄の魔神コロパティロン', 'lv': 5, 'autosell': 0},
  {'id': 8004, 'type': 0, 'job': 0, 'name': '閃光の霊刃使いレイジ', 'lv': 4, 'autosell': 0},
  {'id': 8005, 'type': 0, 'job': 0, 'name': '七色の霊刃使いサクヤ', 'lv': 5, 'autosell': 0},
  {'id': 8006, 'type': 0, 'job': 2, 'name': '復讐の霊刃使いリック', 'lv': 4, 'autosell': 0},
  {'id': 8007, 'type': 0, 'job': 2, 'name': '海賊令嬢ミスティ', 'lv': 5, 'autosell': 0},
  {'id': 8008, 'type': 0, 'job': 1, 'name': '銀の森の妖精姫アルティナ', 'lv': 5, 'autosell': 0},
  {'id': 90000, 'type': 3, 'job': 0, 'name': '成長アルカナ I', 'lv': 1, 'autosell': 0},
  {'id': 90001, 'type': 3, 'job': 1, 'name': '成長アルカナ I', 'lv': 1, 'autosell': 0},
  {'id': 90002, 'type': 3, 'job': 2, 'name': '成長アルカナ I', 'lv': 1, 'autosell': 0},
  {'id': 90003, 'type': 3, 'job': 3, 'name': '成長アルカナ I', 'lv': 1, 'autosell': 0},
  {'id': 90004, 'type': 3, 'job': 4, 'name': '成長アルカナ I', 'lv': 1, 'autosell': 0},
  {'id': 90005, 'type': 3, 'job': 0, 'name': '成長アルカナ II', 'lv': 2, 'autosell': 0},
  {'id': 90006, 'type': 3, 'job': 1, 'name': '成長アルカナ II', 'lv': 2, 'autosell': 0},
  {'id': 90007, 'type': 3, 'job': 2, 'name': '成長アルカナ II', 'lv': 2, 'autosell': 0},
  {'id': 90008, 'type': 3, 'job': 3, 'name': '成長アルカナ II', 'lv': 2, 'autosell': 0},
  {'id': 90009, 'type': 3, 'job': 4, 'name': '成長アルカナ II', 'lv': 2, 'autosell': 0},
  {'id': 90010, 'type': 3, 'job': 0, 'name': '成長アルカナ III', 'lv': 3, 'autosell': 0},
  {'id': 90011, 'type': 3, 'job': 1, 'name': '成長アルカナ III', 'lv': 3, 'autosell': 0},
  {'id': 90012, 'type': 3, 'job': 2, 'name': '成長アルカナ III', 'lv': 3, 'autosell': 0},
  {'id': 90013, 'type': 3, 'job': 3, 'name': '成長アルカナ III', 'lv': 3, 'autosell': 0},
  {'id': 90014, 'type': 3, 'job': 4, 'name': '成長アルカナ III', 'lv': 3, 'autosell': 0},
  {'id': 90015, 'type': 3, 'job': 0, 'name': '成長アルカナ IV', 'lv': 4, 'autosell': 0},
  {'id': 90016, 'type': 3, 'job': 1, 'name': '成長アルカナ IV', 'lv': 4, 'autosell': 0},
  {'id': 90017, 'type': 3, 'job': 2, 'name': '成長アルカナ IV', 'lv': 4, 'autosell': 0},
  {'id': 90018, 'type': 3, 'job': 3, 'name': '成長アルカナ IV', 'lv': 4, 'autosell': 0},
  {'id': 90019, 'type': 3, 'job': 4, 'name': '成長アルカナ IV', 'lv': 4, 'autosell': 0},
  {'id': 93000, 'type': 2, 'wp': 0, 'name': '鍛冶アルカナ 斬', 'lv': 1, 'autosell': 0},
  {'id': 93001, 'type': 2, 'wp': 1, 'name': '鍛冶アルカナ 打', 'lv': 1, 'autosell': 0},
  {'id': 93002, 'type': 2, 'wp': 2, 'name': '鍛冶アルカナ 突', 'lv': 1, 'autosell': 0},
  {'id': 93003, 'type': 2, 'wp': 3, 'name': '鍛冶アルカナ 弓', 'lv': 1, 'autosell': 0},
  {'id': 93004, 'type': 2, 'wp': 4, 'name': '鍛冶アルカナ 魔', 'lv': 1, 'autosell': 0},
  {'id': 93005, 'type': 2, 'wp': 5, 'name': '鍛冶アルカナ 聖', 'lv': 1, 'autosell': 0},
  {'id': 93006, 'type': 2, 'wp': 0, 'name': '研磨アルカナ 斬', 'lv': 3, 'autosell': 0},
  {'id': 93007, 'type': 2, 'wp': 1, 'name': '研磨アルカナ 打', 'lv': 3, 'autosell': 0},
  {'id': 93008, 'type': 2, 'wp': 2, 'name': '研磨アルカナ 突', 'lv': 3, 'autosell': 0},
  {'id': 93009, 'type': 2, 'wp': 3, 'name': '研磨アルカナ 弓', 'lv': 3, 'autosell': 0},
  {'id': 93010, 'type': 2, 'wp': 4, 'name': '研磨アルカナ 魔', 'lv': 3, 'autosell': 0},
  {'id': 93011, 'type': 2, 'wp': 5, 'name': '研磨アルカナ 聖', 'lv': 3, 'autosell': 0},
  {'id': 96002, 'type': 1, 'wp': 0, 'name': 'ロングソード', 'lv': 2, 'autosell': 0},
  {'id': 96006, 'type': 1, 'wp': 2, 'name': 'レイピア', 'lv': 3, 'autosell': 0},
  {'id': 96044, 'type': 1, 'wp': 1, 'name': 'スレイブクラブ', 'lv': 2, 'autosell': 0},
  {'id': 96052, 'type': 1, 'wp': 2, 'name': 'ジャベリン', 'lv': 2, 'autosell': 0},
  {'id': 96061, 'type': 1, 'wp': 3, 'name': 'ロングボウ', 'lv': 2, 'autosell': 0},
  {'id': 96073, 'type': 1, 'wp': 4, 'name': 'ウィローワンド', 'lv': 2, 'autosell': 0},
  {'id': 96076, 'type': 1, 'wp': 4, 'name': 'タワーワンド', 'lv': 2, 'autosell': 0},
  {'id': 96083, 'type': 1, 'wp': 5, 'name': 'ホーリーロッド', 'lv': 2, 'autosell': 0},
  {'id': 96118, 'type': 1, 'wp': 4, 'name': 'アイスワンド', 'lv': 2, 'autosell': 0},
  {'id': 96128, 'type': 1, 'wp': 0, 'name': '霊刃．雪姫', 'lv': 2, 'autosell': 0},
  {'id': 96129, 'type': 1, 'wp': 0, 'name': 'ケデュケイオン', 'lv': 3, 'autosell': 0},
  {'id': 96130, 'type': 1, 'wp': 0, 'name': '魔晶剣マナフレア', 'lv': 3, 'autosell': 0},
  {'id': 96131, 'type': 1, 'wp': 3, 'name': '真銀弓スカディ', 'lv': 3, 'autosell': 0},
  {'id': 96132, 'type': 1, 'wp': 4, 'name': 'マジック・パラソル', 'lv': 3, 'autosell': 0},
  {'id': 96925, 'type': 1, 'wp': 1, 'name': 'IXヘッジホッグ', 'lv': 3, 'autosell': 0},
  {'id': 97000, 'type': 1, 'wp': 0, 'name': 'グランフェイバー', 'lv': 3, 'autosell': 0},
  {'id': 97001, 'type': 1, 'wp': 0, 'name': '名刀マクハリ', 'lv': 3, 'autosell': 0},
]

wpList = [
  {'wp': 0, 'name': '斬'},
  {'wp': 1, 'name': '打'},
  {'wp': 2, 'name': '突'},
  {'wp': 3, 'name': '弓'},
  {'wp': 4, 'name': '魔'},
  {'wp': 5, 'name': '聖'},
]

jobList = [
  {'job': 0, 'name': '戦士', 'sname': '戦'},
  {'job': 1, 'name': '弓使い', 'sname': '弓'},
  {'job': 2, 'name': '魔法使い', 'sname': '魔'},
  {'job': 3, 'name': '僧侶', 'sname': '僧'},
  {'job': 4, 'name': '騎士', 'sname': '騎'},
]

typeList = [
  {'type': 'card', 'name': '角色卡', 'link': gachaList},
  {'type': 'weapon_ev', 'name': '武器卡', 'link': gachaList},
  {'type': 'weapon_rf', 'name': '鍛造卡', 'link': gachaList},  
  {'type': 'chara_rf', 'name': '成長卡', 'link': gachaList},
  {'type': 'item', 'name': '道具', 'link': itemList},
  {'type': 'stone', 'name': '道具', 'link': stoneList},
  {'type': 0, 'name': '角色卡', 'link': gachaList},
  {'type': 1, 'name': '武器卡', 'link': gachaList},
  {'type': 2, 'name': '鍛造卡', 'link': gachaList},
  {'type': 3, 'name': '成長卡', 'link': gachaList},
]

def i2n(id,type,value = None):
  resType = newSelect('type',type,typeList)
  resId = newSelect('id',id,resType['link'])
  #print resId.get('lv', False)
  if resId is None:
    idString = str(id)
  elif resId.get('lv', False) != False:
    if resId['type'] == TYPE_CARD or resId['type'] == TYPE_CHARA_RF:
      resJob = newSelect('job',resId['job'],jobList)
      idString = '%sS%s %s' % (resId['lv'],resJob['sname'],resId['name'])
    elif resId['type'] == TYPE_WEAPON_EV or resId['type'] == TYPE_WEAPON_RF:
      resWp = newSelect('wp',resId['wp'],wpList)
      idString = '%sS%s %s' % (resId['lv'],resWp['name'],resId['name'])
    else:
     idString = '%sS %s' % (resId['lv'],resId['name'])
  else:
    idString = resId['name']
  if value is None:
    respString = idString
  else:
    respString = resType['name'] + ' - ' + idString + ' x ' + str(value)
  return respString #.encode("utf-8")

def newSelect(where_title,where_value,from_table):
  for gacha in from_table:
    if gacha[where_title] == where_value:
      return gacha
  return None

def i2as(id,type):
  resType = newSelect('type',type,typeList)
  resId = newSelect('id',id,resType['link'])
  if resId is None or resType['link'] != gachaList:    
    return 0
  else:
    return resId['autosell']

def i2star(id):
  #resType = newSelect('type',type,typeList)
  resId = newSelect('id',id,gachaList)
  if resId is None: 
    return 99
  else:
    return resId['lv']

def i2type(id):
  #resType = newSelect('type',type,typeList)
  resId = newSelect('id',id,gachaList)
  if resId is None: 
    return -1
  else:
    return resId['type']