"use strict";(function(n){function o(n,t){return n?typeof n!="string"?[]:n.split(t):[]}var f=0,i=1,e=2,t=3,u=[["AF","AFG",4,"Afghanistan"],["AX","ALA",248,"Åland Islands"],["AL","ALB",8,"Albania"],["DZ","DZA",12,"Algeria"],["AS","ASM",16,"American Samoa"],["AD","AND",20,"Andorra"],["AO","AGO",24,"Angola"],["AI","AIA",660,"Anguilla"],["AQ","ATA",10,"Antarctica"],["AG","ATG",28,"Antigua and Barbuda"],["AR","ARG",32,"Argentina"],["AM","ARM",51,"Armenia"],["AW","ABW",533,"Aruba"],["AU","AUS",36,"Australia"],["AT","AUT",40,"Austria"],["AZ","AZE",31,"Azerbaijan"],["BS","BHS",44,"Bahamas"],["BH","BHR",48,"Bahrain"],["BD","BGD",50,"Bangladesh"],["BB","BRB",52,"Barbados"],["BY","BLR",112,"Belarus"],["BE","BEL",56,"Belgium"],["BZ","BLZ",84,"Belize"],["BJ","BEN",204,"Benin"],["BM","BMU",60,"Bermuda"],["BT","BTN",64,"Bhutan"],["BO","BOL",68,"Bolivia (Plurinational State of)"],["BQ","BES",535,"Bonaire, Sint Eustatius and Saba"],["BA","BIH",70,"Bosnia and Herzegovina"],["BW","BWA",72,"Botswana"],["BV","BVT",74,"Bouvet Island"],["BR","BRA",76,"Brazil"],["IO","IOT",86,"British Indian Ocean Territory"],["BN","BRN",96,"Brunei Darussalam"],["BG","BGR",100,"Bulgaria"],["BF","BFA",854,"Burkina Faso"],["BI","BDI",108,"Burundi"],["KH","KHM",116,"Cambodia"],["CM","CMR",120,"Cameroon"],["CA","CAN",124,"Canada"],["CV","CPV",132,"Cabo Verde"],["KY","CYM",136,"Cayman Islands"],["CF","CAF",140,"Central African Republic"],["TD","TCD",148,"Chad"],["CL","CHL",152,"Chile"],["CN","CHN",156,"China"],["CX","CXR",162,"Christmas Island"],["CC","CCK",166,"Cocos (Keeling) Islands"],["CO","COL",170,"Colombia"],["KM","COM",174,"Comoros"],["CG","COG",178,"Congo"],["CD","COD",180,"Congo (Democratic Republic of the)"],["CK","COK",184,"Cook Islands"],["CR","CRI",188,"Costa Rica"],["CI","CIV",384,"Côte d'Ivoire"],["HR","HRV",191,"Croatia"],["CU","CUB",192,"Cuba"],["CW","CUW",531,"Curaçao"],["CY","CYP",196,"Cyprus"],["CZ","CZE",203,"Czech Republic"],["DK","DNK",208,"Denmark"],["DJ","DJI",262,"Djibouti"],["DM","DMA",212,"Dominica"],["DO","DOM",214,"Dominican Republic"],["EC","ECU",218,"Ecuador"],["EG","EGY",818,"Egypt"],["SV","SLV",222,"El Salvador"],["GQ","GNQ",226,"Equatorial Guinea"],["ER","ERI",232,"Eritrea"],["EE","EST",233,"Estonia"],["ET","ETH",231,"Ethiopia"],["FK","FLK",238,"Falkland Islands (Malvinas)"],["FO","FRO",234,"Faroe Islands"],["FJ","FJI",242,"Fiji"],["FI","FIN",246,"Finland"],["FR","FRA",250,"France"],["GF","GUF",254,"French Guiana"],["PF","PYF",258,"French Polynesia"],["TF","ATF",260,"French Southern Territories"],["GA","GAB",266,"Gabon"],["GM","GMB",270,"Gambia"],["GE","GEO",268,"Georgia"],["DE","DEU",276,"Germany"],["GH","GHA",288,"Ghana"],["GI","GIB",292,"Gibraltar"],["GR","GRC",300,"Greece"],["GL","GRL",304,"Greenland"],["GD","GRD",308,"Grenada"],["GP","GLP",312,"Guadeloupe"],["GU","GUM",316,"Guam"],["GT","GTM",320,"Guatemala"],["GG","GGY",831,"Guernsey"],["GN","GIN",324,"Guinea"],["GW","GNB",624,"Guinea-Bissau"],["GY","GUY",328,"Guyana"],["HT","HTI",332,"Haiti"],["HM","HMD",334,"Heard Island and McDonald Islands"],["VA","VAT",336,"Holy See"],["HN","HND",340,"Honduras"],["HK","HKG",344,"Hong Kong"],["HU","HUN",348,"Hungary"],["IS","ISL",352,"Iceland"],["IN","IND",356,"India"],["ID","IDN",360,"Indonesia"],["IR","IRN",364,"Iran (Islamic Republic of)"],["IQ","IRQ",368,"Iraq"],["IE","IRL",372,"Ireland"],["IM","IMN",833,"Isle of Man"],["IL","ISR",376,"Israel"],["IT","ITA",380,"Italy"],["JM","JAM",388,"Jamaica"],["JP","JPN",392,"Japan"],["JE","JEY",832,"Jersey"],["JO","JOR",400,"Jordan"],["KZ","KAZ",398,"Kazakhstan"],["KE","KEN",404,"Kenya"],["KI","KIR",296,"Kiribati"],["KP","PRK",408,"Korea (Democratic People's Republic of)"],["KR","KOR",410,"Korea (Republic of)"],["KW","KWT",414,"Kuwait"],["KG","KGZ",417,"Kyrgyzstan"],["LA","LAO",418,"Lao People's Democratic Republic"],["LV","LVA",428,"Latvia"],["LB","LBN",422,"Lebanon"],["LS","LSO",426,"Lesotho"],["LR","LBR",430,"Liberia"],["LY","LBY",434,"Libya"],["LI","LIE",438,"Liechtenstein"],["LT","LTU",440,"Lithuania"],["LU","LUX",442,"Luxembourg"],["MO","MAC",446,"Macao"],["MK","MKD",807,"Macedonia (the former Yugoslav Republic of)"],["MG","MDG",450,"Madagascar"],["MW","MWI",454,"Malawi"],["MY","MYS",458,"Malaysia"],["MV","MDV",462,"Maldives"],["ML","MLI",466,"Mali"],["MT","MLT",470,"Malta"],["MH","MHL",584,"Marshall Islands"],["MQ","MTQ",474,"Martinique"],["MR","MRT",478,"Mauritania"],["MU","MUS",480,"Mauritius"],["YT","MYT",175,"Mayotte"],["MX","MEX",484,"Mexico"],["FM","FSM",583,"Micronesia (Federated States of)"],["MD","MDA",498,"Moldova (Republic of)"],["MC","MCO",492,"Monaco"],["MN","MNG",496,"Mongolia"],["ME","MNE",499,"Montenegro"],["MS","MSR",500,"Montserrat"],["MA","MAR",504,"Morocco"],["MZ","MOZ",508,"Mozambique"],["MM","MMR",104,"Myanmar"],["NA","NAM",516,"Namibia"],["NR","NRU",520,"Nauru"],["NP","NPL",524,"Nepal"],["NL","NLD",528,"Netherlands"],["NC","NCL",540,"New Caledonia"],["NZ","NZL",554,"New Zealand"],["NI","NIC",558,"Nicaragua"],["NE","NER",562,"Niger"],["NG","NGA",566,"Nigeria"],["NU","NIU",570,"Niue"],["NF","NFK",574,"Norfolk Island"],["MP","MNP",580,"Northern Mariana Islands"],["NO","NOR",578,"Norway"],["OM","OMN",512,"Oman"],["PK","PAK",586,"Pakistan"],["PW","PLW",585,"Palau"],["PS","PSE",275,"Palestine, State of"],["PA","PAN",591,"Panama"],["PG","PNG",598,"Papua New Guinea"],["PY","PRY",600,"Paraguay"],["PE","PER",604,"Peru"],["PH","PHL",608,"Philippines"],["PN","PCN",612,"Pitcairn"],["PL","POL",616,"Poland"],["PT","PRT",620,"Portugal"],["PR","PRI",630,"Puerto Rico"],["QA","QAT",634,"Qatar"],["RE","REU",638,"Réunion"],["RO","ROU",642,"Romania"],["RU","RUS",643,"Russian Federation"],["RW","RWA",646,"Rwanda"],["BL","BLM",652,"Saint Barthélemy"],["SH","SHN",654,"Saint Helena, Ascension and Tristan da Cunha"],["KN","KNA",659,"Saint Kitts and Nevis"],["LC","LCA",662,"Saint Lucia"],["MF","MAF",663,"Saint Martin (French part)"],["PM","SPM",666,"Saint Pierre and Miquelon"],["VC","VCT",670,"Saint Vincent and the Grenadines"],["WS","WSM",882,"Samoa"],["SM","SMR",674,"San Marino"],["ST","STP",678,"Sao Tome and Principe"],["SA","SAU",682,"Saudi Arabia"],["SN","SEN",686,"Senegal"],["RS","SRB",688,"Serbia"],["SC","SYC",690,"Seychelles"],["SL","SLE",694,"Sierra Leone"],["SG","SGP",702,"Singapore"],["SX","SXM",534,"Sint Maarten (Dutch part)"],["SK","SVK",703,"Slovakia"],["SI","SVN",705,"Slovenia"],["SB","SLB",90,"Solomon Islands"],["SO","SOM",706,"Somalia"],["ZA","ZAF",710,"South Africa"],["GS","SGS",239,"South Georgia and the South Sandwich Islands"],["SS","SSD",728,"South Sudan"],["ES","ESP",724,"Spain"],["LK","LKA",144,"Sri Lanka"],["SD","SDN",729,"Sudan"],["SR","SUR",740,"Suriname"],["SJ","SJM",744,"Svalbard and Jan Mayen"],["SZ","SWZ",748,"Swaziland"],["SE","SWE",752,"Sweden"],["CH","CHE",756,"Switzerland"],["SY","SYR",760,"Syrian Arab Republic"],["TW","TWN",158,"Taiwan, Province of China"],["TJ","TJK",762,"Tajikistan"],["TZ","TZA",834,"Tanzania, United Republic of"],["TH","THA",764,"Thailand"],["TL","TLS",626,"Timor-Leste"],["TG","TGO",768,"Togo"],["TK","TKL",772,"Tokelau"],["TO","TON",776,"Tonga"],["TT","TTO",780,"Trinidad and Tobago"],["TN","TUN",788,"Tunisia"],["TR","TUR",792,"Turkey"],["TM","TKM",795,"Turkmenistan"],["TC","TCA",796,"Turks and Caicos Islands"],["TV","TUV",798,"Tuvalu"],["UG","UGA",800,"Uganda"],["UA","UKR",804,"Ukraine"],["AE","ARE",784,"United Arab Emirates"],["GB","GBR",826,"United Kingdom of Great Britain and Northern Ireland"],["US","USA",840,"United States of America"],["UM","UMI",581,"United States Minor Outlying Islands"],["UY","URY",858,"Uruguay"],["UZ","UZB",860,"Uzbekistan"],["VU","VUT",548,"Vanuatu"],["VE","VEN",862,"Venezuela (Bolivarian Republic of)"],["VN","VNM",704,"Viet Nam"],["VG","VGB",92,"Virgin Islands (British)"],["VI","VIR",850,"Virgin Islands (U.S.)"],["WF","WLF",876,"Wallis and Futuna"],["EH","ESH",732,"Western Sahara"],["YE","YEM",887,"Yemen"],["ZM","ZMB",894,"Zambia"],["ZW","ZWE",716,"Zimbabwe"]],r={init:function(r){return r=r||{},this.each(function(){var h=n(this),p=r.value||h.val()||h.attr("value"),a=r.codeMode||h.data("code-mode")||"alpha3",w=r.showFlag===undefined?h.data("show-flag"):r.showFlag,l=a=="alpha2"?f:a=="numeric"?e:i,v=r.valueSet||o(h.data("value-set")," "),y=v.length==0?u:n.grep(u,function(n){return v.indexOf(n[l])>=0}),c,s;w?function(){var f=function(n){var i=s.scrollTop(),t=n.position().top,r=t+n.height();(t<0||r>s.height())&&s.scrollTop(i+t)},r=function(n){var r=n.data("country"),u;c.find("span.cs-flag-selected").removeClass().addClass("cs-flag-selected cs-flag "+r[i]);c.find("span.cs-name-selected").text(r[t]);u=r[l];h.val(u).change();n.addClass("cs-selected").siblings().removeClass("cs-selected");f(n)},u=function(n){var i=s.children("li.cs-selected"),t=null;i.length==0?t=s.children("li:first"):n=="up"?t=i.prev():n=="down"&&(t=i.next());t.length>0&&r(t)},e=function(i){s.children("li").each(function(){var u=n(this),f=u.data("country"),e=f[t];if(e.indexOf(i)===0)return r(u),!1})},o=function(){var n=c.position(),t=n.left,i=n.top+c.outerHeight();s.css({left:t+"px",top:i+"px"}).show()},a=function(t){s.children("li").each(function(){var i=n(this),u=i.data("country"),f=u[l];if(t==f)return r(i),!1})};h.hide().attr("autocomplete","off");c=n('<div class="cs-selector" tabindex="0"><span class="cs-flag-selected cs-flag XXX"><\/span><span class="cs-name-selected"><\/span><span class="cs-arrow"><\/span><\/div>').insertAfter(h);s=n('<ul class="cs-list" style="display: none;"><\/ul>').insertAfter(c);c.on("focus click",o).blur(function(){window.setTimeout(function(){s.hide()},200)}).keydown(function(n){var t=n.keyCode;switch(t){case 38:u("up");n.preventDefault();return;case 40:u("down");n.preventDefault();return}t>=65&&t<=90&&(e(String.fromCharCode(t)),n.preventDefault())});s.on("click","li",function(t){r(n(t.target));s.hide()});n.each(y,function(r,u){n('<li><span class="cs-flag '+u[i]+'"><\/span>'+u[t]+"<\/li>").data("country",u).appendTo(s)});a(h.val())}():(h.empty(),n.each(y,function(i,r){n('<option value="'+r[l]+'">'+r[t]+"<\/option>").data("country",r).appendTo(h)}),h.val(p))})}};n.fn.countrySelector=function(t){if(r[t])return r[t].apply(this,Array.prototype.slice.call(arguments,1));if(typeof t!="object"&&t)n.error("Method "+t+" does not exist on jQuery.countrySelector");else return r.init.apply(this,arguments)};n("select[data-role=country-selector]").countrySelector()})(jQuery);
﻿(function ($) {
    var ALPHA2_CODE = 0,
        ALPHA3_CODE = 1,
        NUMERIC_CODE = 2,
        NAME = 3,
        COUNTRIES = [["AF", "AFG", 4, "Afghanistan"], ["AX", "ALA", 248, "Åland Islands"], ["AL", "ALB", 8, "Albania"], ["DZ", "DZA", 12, "Algeria"], ["AS", "ASM", 16, "American Samoa"], ["AD", "AND", 20, "Andorra"], ["AO", "AGO", 24, "Angola"], ["AI", "AIA", 660, "Anguilla"], ["AQ", "ATA", 10, "Antarctica"], ["AG", "ATG", 28, "Antigua and Barbuda"], ["AR", "ARG", 32, "Argentina"], ["AM", "ARM", 51, "Armenia"], ["AW", "ABW", 533, "Aruba"], ["AU", "AUS", 36, "Australia"], ["AT", "AUT", 40, "Austria"], ["AZ", "AZE", 31, "Azerbaijan"], ["BS", "BHS", 44, "Bahamas"], ["BH", "BHR", 48, "Bahrain"], ["BD", "BGD", 50, "Bangladesh"], ["BB", "BRB", 52, "Barbados"], ["BY", "BLR", 112, "Belarus"], ["BE", "BEL", 56, "Belgium"], ["BZ", "BLZ", 84, "Belize"], ["BJ", "BEN", 204, "Benin"], ["BM", "BMU", 60, "Bermuda"], ["BT", "BTN", 64, "Bhutan"], ["BO", "BOL", 68, "Bolivia (Plurinational State of)"], ["BQ", "BES", 535, "Bonaire, Sint Eustatius and Saba"], ["BA", "BIH", 70, "Bosnia and Herzegovina"], ["BW", "BWA", 72, "Botswana"], ["BV", "BVT", 74, "Bouvet Island"], ["BR", "BRA", 76, "Brazil"], ["IO", "IOT", 86, "British Indian Ocean Territory"], ["BN", "BRN", 96, "Brunei Darussalam"], ["BG", "BGR", 100, "Bulgaria"], ["BF", "BFA", 854, "Burkina Faso"], ["BI", "BDI", 108, "Burundi"], ["KH", "KHM", 116, "Cambodia"], ["CM", "CMR", 120, "Cameroon"], ["CA", "CAN", 124, "Canada"], ["CV", "CPV", 132, "Cabo Verde"], ["KY", "CYM", 136, "Cayman Islands"], ["CF", "CAF", 140, "Central African Republic"], ["TD", "TCD", 148, "Chad"], ["CL", "CHL", 152, "Chile"], ["CN", "CHN", 156, "China"], ["CX", "CXR", 162, "Christmas Island"], ["CC", "CCK", 166, "Cocos (Keeling) Islands"], ["CO", "COL", 170, "Colombia"], ["KM", "COM", 174, "Comoros"], ["CG", "COG", 178, "Congo"], ["CD", "COD", 180, "Congo (Democratic Republic of the)"], ["CK", "COK", 184, "Cook Islands"], ["CR", "CRI", 188, "Costa Rica"], ["CI", "CIV", 384, "Côte d'Ivoire"], ["HR", "HRV", 191, "Croatia"], ["CU", "CUB", 192, "Cuba"], ["CW", "CUW", 531, "Curaçao"], ["CY", "CYP", 196, "Cyprus"], ["CZ", "CZE", 203, "Czech Republic"], ["DK", "DNK", 208, "Denmark"], ["DJ", "DJI", 262, "Djibouti"], ["DM", "DMA", 212, "Dominica"], ["DO", "DOM", 214, "Dominican Republic"], ["EC", "ECU", 218, "Ecuador"], ["EG", "EGY", 818, "Egypt"], ["SV", "SLV", 222, "El Salvador"], ["GQ", "GNQ", 226, "Equatorial Guinea"], ["ER", "ERI", 232, "Eritrea"], ["EE", "EST", 233, "Estonia"], ["ET", "ETH", 231, "Ethiopia"], ["FK", "FLK", 238, "Falkland Islands (Malvinas)"], ["FO", "FRO", 234, "Faroe Islands"], ["FJ", "FJI", 242, "Fiji"], ["FI", "FIN", 246, "Finland"], ["FR", "FRA", 250, "France"], ["GF", "GUF", 254, "French Guiana"], ["PF", "PYF", 258, "French Polynesia"], ["TF", "ATF", 260, "French Southern Territories"], ["GA", "GAB", 266, "Gabon"], ["GM", "GMB", 270, "Gambia"], ["GE", "GEO", 268, "Georgia"], ["DE", "DEU", 276, "Germany"], ["GH", "GHA", 288, "Ghana"], ["GI", "GIB", 292, "Gibraltar"], ["GR", "GRC", 300, "Greece"], ["GL", "GRL", 304, "Greenland"], ["GD", "GRD", 308, "Grenada"], ["GP", "GLP", 312, "Guadeloupe"], ["GU", "GUM", 316, "Guam"], ["GT", "GTM", 320, "Guatemala"], ["GG", "GGY", 831, "Guernsey"], ["GN", "GIN", 324, "Guinea"], ["GW", "GNB", 624, "Guinea-Bissau"], ["GY", "GUY", 328, "Guyana"], ["HT", "HTI", 332, "Haiti"], ["HM", "HMD", 334, "Heard Island and McDonald Islands"], ["VA", "VAT", 336, "Holy See"], ["HN", "HND", 340, "Honduras"], ["HK", "HKG", 344, "Hong Kong"], ["HU", "HUN", 348, "Hungary"], ["IS", "ISL", 352, "Iceland"], ["IN", "IND", 356, "India"], ["ID", "IDN", 360, "Indonesia"], ["IR", "IRN", 364, "Iran (Islamic Republic of)"], ["IQ", "IRQ", 368, "Iraq"], ["IE", "IRL", 372, "Ireland"], ["IM", "IMN", 833, "Isle of Man"], ["IL", "ISR", 376, "Israel"], ["IT", "ITA", 380, "Italy"], ["JM", "JAM", 388, "Jamaica"], ["JP", "JPN", 392, "Japan"], ["JE", "JEY", 832, "Jersey"], ["JO", "JOR", 400, "Jordan"], ["KZ", "KAZ", 398, "Kazakhstan"], ["KE", "KEN", 404, "Kenya"], ["KI", "KIR", 296, "Kiribati"], ["KP", "PRK", 408, "Korea (Democratic People's Republic of)"], ["KR", "KOR", 410, "Korea (Republic of)"], ["KW", "KWT", 414, "Kuwait"], ["KG", "KGZ", 417, "Kyrgyzstan"], ["LA", "LAO", 418, "Lao People's Democratic Republic"], ["LV", "LVA", 428, "Latvia"], ["LB", "LBN", 422, "Lebanon"], ["LS", "LSO", 426, "Lesotho"], ["LR", "LBR", 430, "Liberia"], ["LY", "LBY", 434, "Libya"], ["LI", "LIE", 438, "Liechtenstein"], ["LT", "LTU", 440, "Lithuania"], ["LU", "LUX", 442, "Luxembourg"], ["MO", "MAC", 446, "Macao"], ["MK", "MKD", 807, "Macedonia (the former Yugoslav Republic of)"], ["MG", "MDG", 450, "Madagascar"], ["MW", "MWI", 454, "Malawi"], ["MY", "MYS", 458, "Malaysia"], ["MV", "MDV", 462, "Maldives"], ["ML", "MLI", 466, "Mali"], ["MT", "MLT", 470, "Malta"], ["MH", "MHL", 584, "Marshall Islands"], ["MQ", "MTQ", 474, "Martinique"], ["MR", "MRT", 478, "Mauritania"], ["MU", "MUS", 480, "Mauritius"], ["YT", "MYT", 175, "Mayotte"], ["MX", "MEX", 484, "Mexico"], ["FM", "FSM", 583, "Micronesia (Federated States of)"], ["MD", "MDA", 498, "Moldova (Republic of)"], ["MC", "MCO", 492, "Monaco"], ["MN", "MNG", 496, "Mongolia"], ["ME", "MNE", 499, "Montenegro"], ["MS", "MSR", 500, "Montserrat"], ["MA", "MAR", 504, "Morocco"], ["MZ", "MOZ", 508, "Mozambique"], ["MM", "MMR", 104, "Myanmar"], ["NA", "NAM", 516, "Namibia"], ["NR", "NRU", 520, "Nauru"], ["NP", "NPL", 524, "Nepal"], ["NL", "NLD", 528, "Netherlands"], ["NC", "NCL", 540, "New Caledonia"], ["NZ", "NZL", 554, "New Zealand"], ["NI", "NIC", 558, "Nicaragua"], ["NE", "NER", 562, "Niger"], ["NG", "NGA", 566, "Nigeria"], ["NU", "NIU", 570, "Niue"], ["NF", "NFK", 574, "Norfolk Island"], ["MP", "MNP", 580, "Northern Mariana Islands"], ["NO", "NOR", 578, "Norway"], ["OM", "OMN", 512, "Oman"], ["PK", "PAK", 586, "Pakistan"], ["PW", "PLW", 585, "Palau"], ["PS", "PSE", 275, "Palestine, State of"], ["PA", "PAN", 591, "Panama"], ["PG", "PNG", 598, "Papua New Guinea"], ["PY", "PRY", 600, "Paraguay"], ["PE", "PER", 604, "Peru"], ["PH", "PHL", 608, "Philippines"], ["PN", "PCN", 612, "Pitcairn"], ["PL", "POL", 616, "Poland"], ["PT", "PRT", 620, "Portugal"], ["PR", "PRI", 630, "Puerto Rico"], ["QA", "QAT", 634, "Qatar"], ["RE", "REU", 638, "Réunion"], ["RO", "ROU", 642, "Romania"], ["RU", "RUS", 643, "Russian Federation"], ["RW", "RWA", 646, "Rwanda"], ["BL", "BLM", 652, "Saint Barthélemy"], ["SH", "SHN", 654, "Saint Helena, Ascension and Tristan da Cunha"], ["KN", "KNA", 659, "Saint Kitts and Nevis"], ["LC", "LCA", 662, "Saint Lucia"], ["MF", "MAF", 663, "Saint Martin (French part)"], ["PM", "SPM", 666, "Saint Pierre and Miquelon"], ["VC", "VCT", 670, "Saint Vincent and the Grenadines"], ["WS", "WSM", 882, "Samoa"], ["SM", "SMR", 674, "San Marino"], ["ST", "STP", 678, "Sao Tome and Principe"], ["SA", "SAU", 682, "Saudi Arabia"], ["SN", "SEN", 686, "Senegal"], ["RS", "SRB", 688, "Serbia"], ["SC", "SYC", 690, "Seychelles"], ["SL", "SLE", 694, "Sierra Leone"], ["SG", "SGP", 702, "Singapore"], ["SX", "SXM", 534, "Sint Maarten (Dutch part)"], ["SK", "SVK", 703, "Slovakia"], ["SI", "SVN", 705, "Slovenia"], ["SB", "SLB", 90, "Solomon Islands"], ["SO", "SOM", 706, "Somalia"], ["ZA", "ZAF", 710, "South Africa"], ["GS", "SGS", 239, "South Georgia and the South Sandwich Islands"], ["SS", "SSD", 728, "South Sudan"], ["ES", "ESP", 724, "Spain"], ["LK", "LKA", 144, "Sri Lanka"], ["SD", "SDN", 729, "Sudan"], ["SR", "SUR", 740, "Suriname"], ["SJ", "SJM", 744, "Svalbard and Jan Mayen"], ["SZ", "SWZ", 748, "Swaziland"], ["SE", "SWE", 752, "Sweden"], ["CH", "CHE", 756, "Switzerland"], ["SY", "SYR", 760, "Syrian Arab Republic"], ["TW", "TWN", 158, "Taiwan, Province of China"], ["TJ", "TJK", 762, "Tajikistan"], ["TZ", "TZA", 834, "Tanzania, United Republic of"], ["TH", "THA", 764, "Thailand"], ["TL", "TLS", 626, "Timor-Leste"], ["TG", "TGO", 768, "Togo"], ["TK", "TKL", 772, "Tokelau"], ["TO", "TON", 776, "Tonga"], ["TT", "TTO", 780, "Trinidad and Tobago"], ["TN", "TUN", 788, "Tunisia"], ["TR", "TUR", 792, "Turkey"], ["TM", "TKM", 795, "Turkmenistan"], ["TC", "TCA", 796, "Turks and Caicos Islands"], ["TV", "TUV", 798, "Tuvalu"], ["UG", "UGA", 800, "Uganda"], ["UA", "UKR", 804, "Ukraine"], ["AE", "ARE", 784, "United Arab Emirates"], ["GB", "GBR", 826, "United Kingdom of Great Britain and Northern Ireland"], ["US", "USA", 840, "United States of America"], ["UM", "UMI", 581, "United States Minor Outlying Islands"], ["UY", "URY", 858, "Uruguay"], ["UZ", "UZB", 860, "Uzbekistan"], ["VU", "VUT", 548, "Vanuatu"], ["VE", "VEN", 862, "Venezuela (Bolivarian Republic of)"], ["VN", "VNM", 704, "Viet Nam"], ["VG", "VGB", 92, "Virgin Islands (British)"], ["VI", "VIR", 850, "Virgin Islands (U.S.)"], ["WF", "WLF", 876, "Wallis and Futuna"], ["EH", "ESH", 732, "Western Sahara"], ["YE", "YEM", 887, "Yemen"], ["ZM", "ZMB", 894, "Zambia"], ["ZW", "ZWE", 716, "Zimbabwe"]];

    function split(string, seperator) {
        if (!string) return [];
        if (typeof string !== "string") return [];
        return string.split(seperator);
    }

    var methods = {
        init: function (options) {
            options = options || {};

            return this.each(function () {
                var _$this = $(this),
                    _initValue = options.value || _$this.val() || _$this.attr("value"),
                    _codeMode = options.codeMode || _$this.data("code-mode") || "alpha3",
                    _showFlag = options.showFlag === undefined ? _$this.data("show-flag") : options.showFlag,
                    _codeProp = _codeMode == "alpha2" ? ALPHA2_CODE : _codeMode == "numeric" ? NUMERIC_CODE : ALPHA3_CODE,
                    _valueSet = options.valueSet || split(_$this.data("value-set"), " "),
                    _countries = _valueSet.length == 0 ? COUNTRIES : $.grep(COUNTRIES, function (country) {
                        return _valueSet.indexOf(country[_codeProp]) >= 0;
                    });

                if (!_showFlag) {
                    _$this.empty();

                    $.each(_countries, function (i, country) {
                        $("<option value=\"" + country[_codeProp] + "\">" + country[NAME] + "</option>")
                            .data("country", country)
                            .appendTo(_$this);
                    });
                    _$this.val(_initValue);
                }
                else {
                    _$this.hide().attr("autocomplete", "off");

                    var _$selector = $("<div class=\"cs-selector\" tabindex=\"0\"><span class=\"cs-flag-selected cs-flag XXX\"></span><span class=\"cs-name-selected\"></span><span class=\"cs-arrow\"></span></div>")
                            .insertAfter(_$this),
                        _$list = $("<ul class=\"cs-list\" style=\"display: none;\"></ul>")
                            .insertAfter(_$selector);

                    function ensureVisible($li) {
                        var scrollTop = _$list.scrollTop(),
                            top = $li.position().top,
                            bottom = top + $li.height();

                        if (top < 0 || bottom > _$list.height()) {
                            _$list.scrollTop(scrollTop + top);
                        }
                    }

                    function select($li) {
                        var country = $li.data("country");
                        _$selector.find("span.cs-flag-selected")
                            .removeClass()
                            .addClass("cs-flag-selected cs-flag " + country[ALPHA3_CODE]);
                        _$selector.find("span.cs-name-selected")
                            .text(country[NAME]);

                        var value = country[_codeProp];

                        _$this.val(value).change();

                        $li.addClass("cs-selected")
                            .siblings().removeClass("cs-selected");
                        ensureVisible($li);
                    }

                    function move(direction) {
                        var $selected = _$list.children("li.cs-selected"),
                            $nextSelected = null;
                        if ($selected.length == 0) {
                            $nextSelected = _$list.children("li:first");
                        }
                        else {
                            if (direction == "up") {
                                $nextSelected = $selected.prev();
                            } else if (direction == "down") {
                                $nextSelected = $selected.next();
                            }
                        }
                        if ($nextSelected.length > 0) {
                            select($nextSelected);
                        }
                    }

                    function search(key) {
                        _$list.children("li").each(function () {
                            var $li = $(this),
                                country = $li.data("country"),
                                name = country[NAME];

                            if (name.indexOf(key) === 0) {
                                select($li);
                                return false; // break out
                            }
                        });
                    }

                    function showList() {
                        var position = _$selector.position(),
                            left = position.left,
                            top = position.top + _$selector.outerHeight();

                        _$list.css({ left: left + "px", top: top + "px" })
                            .show();
                    }

                    function setValue(code) {
                        _$list.children("li").each(function () {
                            var $li = $(this),
                                country = $li.data("country"),
                                code2 = country[_codeProp];

                            if (code == code2) {
                                select($li);
                                return false;
                            };
                        })
                    }

                    _$selector
                        .on("focus click", showList)
                        .blur(function () {
                            // use timer to ensure click event in dropdown list is triggerred
                            window.setTimeout(function () {
                                _$list.hide();
                            }, 200);
                        })
                        .keydown(function (event) {
                            var keyCode = event.keyCode;
                            switch (keyCode) {
                                case 38: // UP
                                    move("up");
                                    event.preventDefault();
                                    return;
                                case 40: // DOWN
                                    move("down");
                                    event.preventDefault();
                                    return;
                            }
                            if (keyCode >= 65 && keyCode <= 90) { // a-z
                                search(String.fromCharCode(keyCode));
                                event.preventDefault();
                            }
                        });

                    _$list.on("click", "li", function (evt) {
                        select($(evt.target));
                        _$list.hide();
                    });

                    $.each(_countries, function (i, country) {
                        $("<li><span class=\"cs-flag " + country[ALPHA3_CODE] + "\"></span>" + country[NAME] + "</li>")
                            .data("country", country)
                            .appendTo(_$list);
                    });

                    setValue(_$this.val());
                }

            });
        }
    };

    $.fn.countrySelector = function (method) {
        if (methods[method]) {
            return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
        } else if (typeof method === 'object' || !method) {
            return methods.init.apply(this, arguments);
        } else {
            $.error('Method ' + method + ' does not exist on jQuery.countrySelector');
        }
    }

    $("select[data-role=country-selector]").countrySelector();

})(jQuery);

﻿$(document).ready(function () {
  $('#lga').select2();
  $("#state_of_origin").select2();
  $("#state_of_origin").change(function () {
    var state = $(this).val();



    switch (state) {
      case "Abia":
        var data = ['Select item...', 'Aba North', 'Aba South', 'Arochukwu', 'Bende', 'Ikwuano', 'Isiala Ngwa North', 'Isiala Ngwa South', 'Isuikwuato', 'Obi Ngwa', 'Ohafia', 'Osisioma', 'Ugwunagbo', 'Ukwa East', 'Ukwa West', 'Umuahia North', 'muahia South', 'Umu Nneochi'];
        break;

      case "Adamawa":
        var data = ['Select item...', 'Demsa', 'Fufure', 'Ganye', 'Gayuk', 'Gombi', 'Grie', 'Hong', 'Jada', 'Larmurde', 'Madagali', 'Maiha', 'Mayo Belwa', 'Michika', 'Mubi North', 'Mubi South', 'Numan', 'Shelleng', 'Song', 'Toungo', 'Yola North', 'Yola South'];
        break;
      case "Akwa Ibom":
        var data = ['Select item...', 'Abak', 'Eastern Obolo', 'Eket', 'Esit Eket', 'Essien Udim', 'Etim Ekpo', 'Etinan', 'Ibeno', 'Ibesikpo Asutan', 'Ibiono-Ibom', 'Ika', 'Ikono', 'Ikot Abasi', 'Ikot Ekpene', 'Ini', 'Itu', 'Mbo', 'Mkpat-Enin', 'Nsit-Atai', 'Nsit-Ibom', 'Nsit-Ubium', 'Obot Akara', 'Okobo', 'Onna', 'Oron', 'Oruk Anam', 'Udung-Uko', 'Ukanafun', 'Uruan', 'Urue-Offong Oruko', 'Uyo'];
        break;
      case "Anambra":
        var data = ['Select item...', 'Aguata', 'Anambra East', 'Anambra West', 'Anaocha', 'Awka North', 'Awka South', 'Ayamelum', 'Dunukofia', 'Ekwusigo', 'Idemili North', 'Idemili South', 'Ihiala', 'Njikoka', 'Nnewi North', 'Nnewi South', 'Ogbaru', 'Onitsha North', 'Onitsha South', 'Orumba North', 'Orumba South', 'Oyi'];
        break;
      
      case "Bauchi":
        var data = ['Select item...', 'Alkaleri', 'Bauchi', 'Bogoro', 'Damban', 'Darazo', 'Dass', 'Gamawa', 'Ganjuwa', 'Giade', 'Itas-Gadau', 'Jama are', 'Katagum', 'Kirfi', 'Misau', 'Ningi', 'Shira', 'Tafawa Balewa', ' Toro', ' Warji', ' Zaki'];

        break;

      case "Bayelsa":
        var data = ['Select item...', 'Brass', 'Ekeremor', 'Kolokuma Opokuma', 'Nembe', 'Ogbia', 'Sagbama', 'Southern Ijaw', 'Yenagoa'];

        break;
      case "Benue":
        var data = ['Select item...', 'Agatu', 'Apa', 'Ado', 'Buruku', 'Gboko', 'Guma', 'Gwer East', 'Gwer West', 'Katsina-Ala', 'Konshisha', 'Kwande', 'Logo', 'Makurdi', 'Obi', 'Ogbadibo', 'Ohimini', 'Oju', 'Okpokwu', 'Oturkpo', 'Tarka', 'Ukum', 'Ushongo', 'Vandeikya'];

        break;
      case "Borno":
        var data = ['Select item...', 'Abadam', 'Askira-Uba', 'Bama', 'Bayo', 'Biu', 'Chibok', 'Damboa', 'Dikwa', 'Gubio', 'Guzamala', 'Gwoza', 'Hawul', 'Jere', 'Kaga', 'Kala-Balge', 'Konduga', 'Kukawa', 'Kwaya Kusar', 'Mafa', 'Magumeri', 'Maiduguri', 'Marte', 'Mobbar', 'Monguno', 'Ngala', 'Nganzai', 'Shani'];

        break;
      case "Cross River":
        var data = ['Select item...', 'Abi', 'Akamkpa', 'Akpabuyo', 'Bakassi', 'Bekwarra', 'Biase', 'Boki', 'Calabar Municipal', 'Calabar South', 'Etung', 'Ikom', 'Obanliku', 'Obubra', 'Obudu', 'Odukpani', 'Ogoja', 'Yakuur', 'Yala'];

        break;

      case "Delta":
        var data = ['Select item...', 'Aniocha North', 'Aniocha South', 'Bomadi', 'Burutu', 'Ethiope East', 'Ethiope West', 'Ika North East', 'Ika South', 'Isoko North', 'Isoko South', 'Ndokwa East', 'Ndokwa West', 'Okpe', 'Oshimili North', 'Oshimili South', 'Patani', 'Sapele', 'Udu', 'Ughelli North', 'Ughelli South', 'Ukwuani', 'Uvwie', 'Warri North', 'Warri South', 'Warri South West'];

        break;

      case "Ebonyi":
        var data = ['Select item...', 'Abakaliki', 'Afikpo North', 'Afikpo South', 'Ebonyi', 'Ezza North', 'Ezza South', 'Ikwo', 'Ishielu', 'Ivo', 'Izzi', 'Ohaozara', 'Ohaukwu', 'Onicha'];
        break;
      case "Edo":
        var data = ['Select item...', 'Akoko-Edo', 'Egor', 'Esan Central', 'Esan North-East', 'Esan South-East', 'Esan West', 'Etsako Central', 'Etsako East', 'Etsako West', 'Igueben', 'Ikpoba Okha', 'Orhionmwon', 'Oredo', 'Ovia North-East', 'Ovia South-West', 'Owan East', 'Owan West', 'Uhunmwonde'];
        break;

      case "Ekiti":
        var data = ['Select item...', 'Ado Ekiti', 'Efon', 'Ekiti East', 'Ekiti South-West', 'Ekiti West', 'Emure', 'Gbonyin', 'Ido Osi', 'Ijero', 'Ikere', 'Ikole', 'Ilejemeje', 'Irepodun-Ifelodun', 'Ise-Orun', 'Moba', 'Oye'];
        break;
      case "Rivers":
        var data = ['Select item...', 'Port Harcourt', 'Obio-Akpor', 'Okrika', 'Ogu–Bolo', 'Eleme', 'Tai', 'Gokana', 'Khana', 'Oyigbo', 'Opobo–Nkoro', 'Andoni', 'Bonny', 'Degema', 'Asari-Toru', 'Akuku-Toru', 'Abua–Odual', 'Ahoada West', 'Ahoada East', 'Ogba–Egbema–Ndoni', 'Emohua', 'Ikwerre', 'Etche', 'Omuma'];
        break;
      case "Enugu":
        var data = ['Select item...', 'Aninri', 'Awgu', 'Enugu East', 'Enugu North', 'Enugu South', 'Ezeagu', 'Igbo Etiti', 'Igbo Eze North', 'Igbo Eze South', 'Isi Uzo', 'Nkanu East', 'Nkanu West', 'Nsukka', 'Oji River', 'Udenu', 'Udi', 'Uzo Uwani'];
        break;
      case "FCT":
        var data = ['Select item...', 'Abaji', 'Bwari', 'Gwagwalada', 'Kuje', 'Kwali', 'Municipal Area Council'];
        break;
      case "Gombe":
        var data = ['Select item...', 'Akko', 'Balanga', 'Billiri', 'Dukku', 'Funakaye', 'Gombe', 'Kaltungo', 'Kwami', 'Nafada', 'Shongom', 'Yamaltu-Deba'];
        break;
      case "Imo":
        var data = ['Select item...', 'Aboh Mbaise', 'Ahiazu Mbaise', 'Ehime Mbano', 'Ezinihitte', 'Ideato North', 'Ideato South', 'Ihitte-Uboma', 'Ikeduru', 'Isiala Mbano', 'Isu', 'Mbaitoli', 'Ngor Okpala', 'Njaba', 'Nkwerre', 'Nwangele', 'Obowo', 'Oguta', 'Ohaji-Egbema', 'Okigwe', 'Orlu', 'Orsu', 'Oru East', 'Oru West', 'Owerri Municipal', 'Owerri North', 'Owerri West', 'Unuimo'];
        break;
      case "Jigawa":
        var data = ['Select item...', 'Auyo', 'Babura', 'Biriniwa', 'Birnin Kudu', 'Buji', 'Dutse', 'Gagarawa', 'Garki', 'Gumel', 'Guri', 'Gwaram', 'Gwiwa', 'Hadejia', 'Jahun', 'Kafin Hausa', 'Kazaure', 'Kiri Kasama', 'Kiyawa', 'Kaugama', 'Maigatari', 'Malam Madori', 'Miga', 'Ringim', 'Roni', 'Sule Tankarkar', 'Taura', 'Yankwashi'];
        break;
      case "Kaduna":
        var data = ['Select item...', 'Birnin Gwari', 'Chikun', 'Giwa', 'Igabi', 'Ikara', 'Jaba', 'Jema a', 'Kachia', 'Kaduna North', 'Kaduna South', 'Kagarko', 'Kajuru', 'Kaura', 'Kauru', 'Kubau', 'Kudan', 'Lere', 'Makarfi', 'Sabon Gari', 'Sanga', 'Soba', 'Zangon Kataf', 'Zaria'];
        break;
      case "Kano":
        var data = ['Select item...', 'Ajingi', 'Albasu', 'Bagwai', 'Bebeji', 'Bichi', 'Bunkure', 'Dala', 'Dambatta', 'Dawakin Kudu', 'Dawakin Tofa', 'Doguwa', 'Fagge', 'Gabasawa', 'Garko', 'Garun Mallam', 'Gaya', 'Gezawa', 'Gwale', 'Gwarzo', 'Kabo', 'Kano Municipal', 'Karaye', 'Kibiya', 'Kiru', 'Kumbotso', 'Kunchi', 'Kura', 'Madobi', 'Makoda', 'Minjibir', 'Nasarawa', 'Rano', 'Rimin Gado', 'Rogo', 'Shanono', 'Sumaila', 'Takai', 'Tarauni', 'Tofa', 'Tsanyawa', 'Tudun Wada', 'Ungogo', 'Warawa', 'Wudil'];
        break;
      case "Katsina":
        var data = ['Select item...', 'Bakori', 'Batagarawa', 'Batsari', 'Baure', 'Bindawa', 'Charanchi', 'Dandume', 'Danja', 'Dan Musa', 'Daura', 'Dutsi', 'Dutsin Ma', 'Faskari', 'Funtua', 'Ingawa', 'Jibia', 'Kafur', 'Kaita', 'Kankara', 'Kankia', 'Katsina', 'Kurfi', 'Kusada', 'Mai Adua', 'Malumfashi', 'Mani', 'Mashi', 'Matazu', 'Musawa', 'Rimi', 'Sabuwa', 'Safana', 'Sandamu', 'Zango'];
        break;
      case "Kebbi":
        var data = ['Select item...', 'Aleiro', 'Arewa Dandi', 'Argungu', 'Augie', 'Bagudo', 'Birnin Kebbi', 'Bunza', 'Dandi', 'Fakai', 'Gwandu', 'Jega', 'Kalgo', 'Koko Besse', 'Maiyama', 'Ngaski', 'Sakaba', 'Shanga', 'Suru', 'Wasagu Danko', 'Yauri', 'Zuru'];
        break;
      case "Kogi":
        var data = ['Select item...', 'Adavi', 'Ajaokuta', 'Ankpa', 'Bassa', 'Dekina', 'Ibaji', 'Idah', 'Igalamela Odolu', 'Ijumu', 'Kabba Bunu', 'Kogi', 'Lokoja', 'Mopa Muro', 'Ofu', 'Ogori Magongo', 'Okehi', 'Okene', 'Olamaboro', 'Omala', 'Yagba East', 'Yagba West'];
        break;
      case "Kwara":
        var data = ['Select item...', 'Asa', 'Baruten', 'Edu', 'Ekiti', 'Ifelodun', 'Ilorin East', 'Ilorin South', 'Ilorin West', 'Irepodun', 'Isin', 'Kaiama', 'Moro', 'Offa', 'Oke Ero', 'Oyun', 'Pategi'];
        break;
      case "Lagos":
        var data = ['Select item...', 'Agege', 'Ajeromi-Ifelodun', 'Alimosho', 'Amuwo-Odofin', 'Apapa', 'Badagry', 'Epe', 'Eti Osa', 'Ibeju-Lekki', 'Ifako-Ijaiye', 'Ikeja', 'Ikorodu', 'Kosofe', 'Lagos Island', 'Lagos Mainland', 'Mushin', 'Ojo', 'Oshodi-Isolo', 'Shomolu', 'Surulere'];
        break;
      case "Nasarawa":
        var data = ['Select item...', 'Akwanga', 'Awe', 'Doma', 'Karu', 'Keana', 'Keffi', 'Kokona', 'Lafia', 'Nasarawa', 'Nasarawa Egon', 'Obi', 'Toto', 'Wamba'];
        break;
      case "Niger":
        var data = ['Select item...', 'Agaie', 'Agwara', 'Bida', 'Borgu', 'Bosso', 'Chanchaga', 'Edati', 'Gbako', 'Gurara', 'Katcha', 'Kontagora', 'Lapai', 'Lavun', 'Magama', 'Mariga', 'Mashegu', 'Mokwa', 'Moya', 'Paikoro', 'Rafi', 'Rijau', 'Shiroro', 'Suleja', 'Tafa', 'Wushishi'];
        break;
      case "Ogun":
        var data = ['Select item...', 'Abeokuta North', 'Abeokuta South', 'Ado-Odo Ota', 'Egbado North', 'Egbado South', 'Ewekoro', 'Ifo', 'Ijebu East', 'Ijebu North', 'Ijebu North East', 'Ijebu Ode', 'Ikenne', 'Imeko Afon', 'Ipokia', 'Obafemi Owode', 'Odeda', 'Odogbolu', 'Ogun Waterside', 'Remo North', 'Shagamu'];
        break;
      case "Ondo":
        var data = ['Select item...', 'Akoko North-East', 'Akoko North-West', 'Akoko South-West', 'Akoko South-East', 'Akure North', 'Akure South', 'Ese Odo', 'Idanre', 'Ifedore', 'Ilaje', 'Ile Oluji-Okeigbo', 'Irele', 'Odigbo', 'Okitipupa', 'Ondo East', 'Ondo West', 'Ose', 'Owo'];
        break;
      case "Osun":
        var data = ['Select item...', 'Atakunmosa East', 'Atakunmosa West', 'Aiyedaade', 'Aiyedire', 'Boluwaduro', 'Boripe', 'Ede North', 'Ede South', 'Ife Central', 'Ife East', 'Ife North', 'Ife South', 'Egbedore', 'Ejigbo', 'Ifedayo', 'Ifelodun', 'Ila', 'Ilesa East', 'Ilesa West', 'Irepodun', 'Irewole', 'Isokan', 'Iwo', 'Obokun', 'Odo Otin', 'Ola Oluwa', 'Olorunda', 'Oriade', 'Orolu', 'Osogbo'];
        break;
      case "Oyo":
        var data = ['Select item...', 'Afijio', 'Akinyele', 'Atiba', 'Atisbo', 'Egbeda', 'Ibadan North', 'Ibadan North-East', 'Ibadan North-West', 'Ibadan South-East', 'Ibadan South-West', 'Ibarapa Central', 'Ibarapa East', 'Ibarapa North', 'Ido', 'Irepo', 'Iseyin', 'Itesiwaju', 'Iwajowa', 'Kajola', 'Lagelu', 'Ogbomosho North', 'Ogbomosho South', 'Ogo Oluwa', 'Olorunsogo', 'Oluyole', 'Ona Ara', 'Orelope', 'Ori Ire', 'Oyo', 'Oyo East', 'Saki East', 'Saki West', 'Surulere'];
        break;
      case "Plateau":
        var data = ['Select item...', 'Bokkos', 'Barkin Ladi', 'Bassa', 'Jos East', 'Jos North', 'Jos South', 'Kanam', 'Kanke', 'Langtang South', 'Langtang North', 'Mangu', 'Mikang', 'Pankshin', 'Qua an Pan', 'Riyom', 'Shendam', 'Wase'];
        break;
      case "Sokoto":
        var data = ['Select item...', 'Binji', 'Bodinga', 'Dange Shuni', 'Gada', 'Goronyo', 'Gudu', 'Gwadabawa', 'Illela', 'Isa', 'Kebbe', 'Kware', 'Rabah', 'Sabon Birni', 'Shagari', 'Silame', 'Sokoto North', 'Sokoto South', 'Tambuwal', 'Tangaza', 'Tureta', 'Wamako', 'Wurno', 'Yabo'];
        break;
      case "Taraba":
        var data = ['Select item...', 'Ardo Kola', 'Bali', 'Donga', 'Gashaka', 'Gassol', 'Ibi', 'Jalingo', 'Karim Lamido', 'Kumi', 'Lau', 'Sardauna', 'Takum', 'Ussa', 'Wukari', 'Yorro', 'Zing'];
        break;
      case "Yobe":
        var data = ['Select item...', 'Bade', 'Bursari', 'Damaturu', 'Fika', 'Fune', 'Geidam', 'Gujba', 'Gulani', 'Jakusko', 'Karasuwa', 'Machina', 'Nangere', 'Nguru', 'Potiskum', 'Tarmuwa', 'Yunusari', 'Yusufari'];
        break;
      case "Zamfara":
        var data = ['Select item...', 'Anka', 'Bakura', 'Birnin Magaji Kiyaw', 'Bukkuyum', 'Bungudu', 'Gummi', 'Gusau', 'Kaura Namoda', 'Maradun', 'Maru', 'Shinkafi', 'Talata Mafara', 'Chafe', 'Zurmi'];

    }




    var i;
    var html = [];
    //loop through the array
    for (var i = 0; i < data.length; i++) { //begin for loop

      //add the option elements to the html array
      html.push("<option>" + data[i] + "</option>")

    } //end for loop

    //add the option values to the select list with an id of lga
    document.getElementById("lga").innerHTML = html.join(''); 

  });

});
﻿$(document).ready(function(){$("#lga").select2(),$("#state").select2(),$("#state").change(function(){switch($(this).val()){case"Abia":var a=["Select item...","Aba North","Aba South","Arochukwu","Bende","Ikwuano","Isiala Ngwa North","Isiala Ngwa South","Isuikwuato","Obi Ngwa","Ohafia","Osisioma","Ugwunagbo","Ukwa East","Ukwa West","Umuahia North","muahia South","Umu Nneochi"];break;case"Adamawa":a=["Select item...","Demsa","Fufure","Ganye","Gayuk","Gombi","Grie","Hong","Jada","Larmurde","Madagali","Maiha","Mayo Belwa","Michika","Mubi North","Mubi South","Numan","Shelleng","Song","Toungo","Yola North","Yola South"];break;case"AkwaIbom":a=["Select item...","Abak","Eastern Obolo","Eket","Esit Eket","Essien Udim","Etim Ekpo","Etinan","Ibeno","Ibesikpo Asutan","Ibiono-Ibom","Ika","Ikono","Ikot Abasi","Ikot Ekpene","Ini","Itu","Mbo","Mkpat-Enin","Nsit-Atai","Nsit-Ibom","Nsit-Ubium","Obot Akara","Okobo","Onna","Oron","Oruk Anam","Udung-Uko","Ukanafun","Uruan","Urue-Offong Oruko","Uyo"];break;case"Anambra":case"Anambra":a=["Select item...","Aguata","Anambra East","Anambra West","Anaocha","Awka North","Awka South","Ayamelum","Dunukofia","Ekwusigo","Idemili North","Idemili South","Ihiala","Njikoka","Nnewi North","Nnewi South","Ogbaru","Onitsha North","Onitsha South","Orumba North","Orumba South","Oyi"];break;case"Bauchi":a=["Select item...","Alkaleri","Bauchi","Bogoro","Damban","Darazo","Dass","Gamawa","Ganjuwa","Giade","Itas-Gadau","Jama are","Katagum","Kirfi","Misau","Ningi","Shira","Tafawa Balewa"," Toro"," Warji"," Zaki"];break;case"Bayelsa":a=["Select item...","Brass","Ekeremor","Kolokuma Opokuma","Nembe","Ogbia","Sagbama","Southern Ijaw","Yenagoa"];break;case"Benue":a=["Select item...","Agatu","Apa","Ado","Buruku","Gboko","Guma","Gwer East","Gwer West","Katsina-Ala","Konshisha","Kwande","Logo","Makurdi","Obi","Ogbadibo","Ohimini","Oju","Okpokwu","Oturkpo","Tarka","Ukum","Ushongo","Vandeikya"];break;case"Borno":a=["Select item...","Abadam","Askira-Uba","Bama","Bayo","Biu","Chibok","Damboa","Dikwa","Gubio","Guzamala","Gwoza","Hawul","Jere","Kaga","Kala-Balge","Konduga","Kukawa","Kwaya Kusar","Mafa","Magumeri","Maiduguri","Marte","Mobbar","Monguno","Ngala","Nganzai","Shani"];break;case"Cross River":a=["Select item...","Abi","Akamkpa","Akpabuyo","Bakassi","Bekwarra","Biase","Boki","Calabar Municipal","Calabar South","Etung","Ikom","Obanliku","Obubra","Obudu","Odukpani","Ogoja","Yakuur","Yala"];break;case"Delta":a=["Select item...","Aniocha North","Aniocha South","Bomadi","Burutu","Ethiope East","Ethiope West","Ika North East","Ika South","Isoko North","Isoko South","Ndokwa East","Ndokwa West","Okpe","Oshimili North","Oshimili South","Patani","Sapele","Udu","Ughelli North","Ughelli South","Ukwuani","Uvwie","Warri North","Warri South","Warri South West"];break;case"Ebonyi":a=["Select item...","Abakaliki","Afikpo North","Afikpo South","Ebonyi","Ezza North","Ezza South","Ikwo","Ishielu","Ivo","Izzi","Ohaozara","Ohaukwu","Onicha"];break;case"Edo":a=["Select item...","Akoko-Edo","Egor","Esan Central","Esan North-East","Esan South-East","Esan West","Etsako Central","Etsako East","Etsako West","Igueben","Ikpoba Okha","Orhionmwon","Oredo","Ovia North-East","Ovia South-West","Owan East","Owan West","Uhunmwonde"];break;case"Ekiti":a=["Select item...","Ado Ekiti","Efon","Ekiti East","Ekiti South-West","Ekiti West","Emure","Gbonyin","Ido Osi","Ijero","Ikere","Ikole","Ilejemeje","Irepodun-Ifelodun","Ise-Orun","Moba","Oye"];break;case"Rivers":a=["Select item...","Port Harcourt","Obio-Akpor","Okrika","Ogu–Bolo","Eleme","Tai","Gokana","Khana","Oyigbo","Opobo–Nkoro","Andoni","Bonny","Degema","Asari-Toru","Akuku-Toru","Abua–Odual","Ahoada West","Ahoada East","Ogba–Egbema–Ndoni","Emohua","Ikwerre","Etche","Omuma"];break;case"Enugu":a=["Select item...","Aninri","Awgu","Enugu East","Enugu North","Enugu South","Ezeagu","Igbo Etiti","Igbo Eze North","Igbo Eze South","Isi Uzo","Nkanu East","Nkanu West","Nsukka","Oji River","Udenu","Udi","Uzo Uwani"];break;case"FCT":a=["Select item...","Abaji","Bwari","Gwagwalada","Kuje","Kwali","Municipal Area Council"];break;case"Gombe":a=["Select item...","Akko","Balanga","Billiri","Dukku","Funakaye","Gombe","Kaltungo","Kwami","Nafada","Shongom","Yamaltu-Deba"];break;case"Imo":a=["Select item...","Aboh Mbaise","Ahiazu Mbaise","Ehime Mbano","Ezinihitte","Ideato North","Ideato South","Ihitte-Uboma","Ikeduru","Isiala Mbano","Isu","Mbaitoli","Ngor Okpala","Njaba","Nkwerre","Nwangele","Obowo","Oguta","Ohaji-Egbema","Okigwe","Orlu","Orsu","Oru East","Oru West","Owerri Municipal","Owerri North","Owerri West","Unuimo"];break;case"Jigawa":a=["Select item...","Auyo","Babura","Biriniwa","Birnin Kudu","Buji","Dutse","Gagarawa","Garki","Gumel","Guri","Gwaram","Gwiwa","Hadejia","Jahun","Kafin Hausa","Kazaure","Kiri Kasama","Kiyawa","Kaugama","Maigatari","Malam Madori","Miga","Ringim","Roni","Sule Tankarkar","Taura","Yankwashi"];break;case"Kaduna":a=["Select item...","Birnin Gwari","Chikun","Giwa","Igabi","Ikara","Jaba","Jema a","Kachia","Kaduna North","Kaduna South","Kagarko","Kajuru","Kaura","Kauru","Kubau","Kudan","Lere","Makarfi","Sabon Gari","Sanga","Soba","Zangon Kataf","Zaria"];break;case"Kano":a=["Select item...","Ajingi","Albasu","Bagwai","Bebeji","Bichi","Bunkure","Dala","Dambatta","Dawakin Kudu","Dawakin Tofa","Doguwa","Fagge","Gabasawa","Garko","Garun Mallam","Gaya","Gezawa","Gwale","Gwarzo","Kabo","Kano Municipal","Karaye","Kibiya","Kiru","Kumbotso","Kunchi","Kura","Madobi","Makoda","Minjibir","Nasarawa","Rano","Rimin Gado","Rogo","Shanono","Sumaila","Takai","Tarauni","Tofa","Tsanyawa","Tudun Wada","Ungogo","Warawa","Wudil"];break;case"Katsina":a=["Select item...","Bakori","Batagarawa","Batsari","Baure","Bindawa","Charanchi","Dandume","Danja","Dan Musa","Daura","Dutsi","Dutsin Ma","Faskari","Funtua","Ingawa","Jibia","Kafur","Kaita","Kankara","Kankia","Katsina","Kurfi","Kusada","Mai Adua","Malumfashi","Mani","Mashi","Matazu","Musawa","Rimi","Sabuwa","Safana","Sandamu","Zango"];break;case"Kebbi":a=["Select item...","Aleiro","Arewa Dandi","Argungu","Augie","Bagudo","Birnin Kebbi","Bunza","Dandi","Fakai","Gwandu","Jega","Kalgo","Koko Besse","Maiyama","Ngaski","Sakaba","Shanga","Suru","Wasagu Danko","Yauri","Zuru"];break;case"Kogi":a=["Select item...","Adavi","Ajaokuta","Ankpa","Bassa","Dekina","Ibaji","Idah","Igalamela Odolu","Ijumu","Kabba Bunu","Kogi","Lokoja","Mopa Muro","Ofu","Ogori Magongo","Okehi","Okene","Olamaboro","Omala","Yagba East","Yagba West"];break;case"Kwara":a=["Select item...","Asa","Baruten","Edu","Ekiti","Ifelodun","Ilorin East","Ilorin South","Ilorin West","Irepodun","Isin","Kaiama","Moro","Offa","Oke Ero","Oyun","Pategi"];break;case"Lagos":a=["Select item...","Agege","Ajeromi-Ifelodun","Alimosho","Amuwo-Odofin","Apapa","Badagry","Epe","Eti Osa","Ibeju-Lekki","Ifako-Ijaiye","Ikeja","Ikorodu","Kosofe","Lagos Island","Lagos Mainland","Mushin","Ojo","Oshodi-Isolo","Shomolu","Surulere"];break;case"Nasarawa":a=["Select item...","Akwanga","Awe","Doma","Karu","Keana","Keffi","Kokona","Lafia","Nasarawa","Nasarawa Egon","Obi","Toto","Wamba"];break;case"Niger":a=["Select item...","Agaie","Agwara","Bida","Borgu","Bosso","Chanchaga","Edati","Gbako","Gurara","Katcha","Kontagora","Lapai","Lavun","Magama","Mariga","Mashegu","Mokwa","Moya","Paikoro","Rafi","Rijau","Shiroro","Suleja","Tafa","Wushishi"];break;case"Ogun":a=["Select item...","Abeokuta North","Abeokuta South","Ado-Odo Ota","Egbado North","Egbado South","Ewekoro","Ifo","Ijebu East","Ijebu North","Ijebu North East","Ijebu Ode","Ikenne","Imeko Afon","Ipokia","Obafemi Owode","Odeda","Odogbolu","Ogun Waterside","Remo North","Shagamu"];break;case"Ondo":a=["Select item...","Akoko North-East","Akoko North-West","Akoko South-West","Akoko South-East","Akure North","Akure South","Ese Odo","Idanre","Ifedore","Ilaje","Ile Oluji-Okeigbo","Irele","Odigbo","Okitipupa","Ondo East","Ondo West","Ose","Owo"];break;case"Osun":a=["Select item...","Atakunmosa East","Atakunmosa West","Aiyedaade","Aiyedire","Boluwaduro","Boripe","Ede North","Ede South","Ife Central","Ife East","Ife North","Ife South","Egbedore","Ejigbo","Ifedayo","Ifelodun","Ila","Ilesa East","Ilesa West","Irepodun","Irewole","Isokan","Iwo","Obokun","Odo Otin","Ola Oluwa","Olorunda","Oriade","Orolu","Osogbo"];break;case"Oyo":a=["Select item...","Afijio","Akinyele","Atiba","Atisbo","Egbeda","Ibadan North","Ibadan North-East","Ibadan North-West","Ibadan South-East","Ibadan South-West","Ibarapa Central","Ibarapa East","Ibarapa North","Ido","Irepo","Iseyin","Itesiwaju","Iwajowa","Kajola","Lagelu","Ogbomosho North","Ogbomosho South","Ogo Oluwa","Olorunsogo","Oluyole","Ona Ara","Orelope","Ori Ire","Oyo","Oyo East","Saki East","Saki West","Surulere"];break;case"Plateau":a=["Select item...","Bokkos","Barkin Ladi","Bassa","Jos East","Jos North","Jos South","Kanam","Kanke","Langtang South","Langtang North","Mangu","Mikang","Pankshin","Qua an Pan","Riyom","Shendam","Wase"];break;case"Sokoto":a=["Select item...","Binji","Bodinga","Dange Shuni","Gada","Goronyo","Gudu","Gwadabawa","Illela","Isa","Kebbe","Kware","Rabah","Sabon Birni","Shagari","Silame","Sokoto North","Sokoto South","Tambuwal","Tangaza","Tureta","Wamako","Wurno","Yabo"];break;case"Taraba":a=["Select item...","Ardo Kola","Bali","Donga","Gashaka","Gassol","Ibi","Jalingo","Karim Lamido","Kumi","Lau","Sardauna","Takum","Ussa","Wukari","Yorro","Zing"];break;case"Yobe":a=["Select item...","Bade","Bursari","Damaturu","Fika","Fune","Geidam","Gujba","Gulani","Jakusko","Karasuwa","Machina","Nangere","Nguru","Potiskum","Tarmuwa","Yunusari","Yusufari"];break;case"Zamfara":a=["Select item...","Anka","Bakura","Birnin Magaji Kiyaw","Bukkuyum","Bungudu","Gummi","Gusau","Kaura Namoda","Maradun","Maru","Shinkafi","Talata Mafara","Chafe","Zurmi"]}for(var e=[],o=0;o<a.length;o++)e.push("<option>"+a[o]+"</option>");document.getElementById("lga").innerHTML=e.join("")})});