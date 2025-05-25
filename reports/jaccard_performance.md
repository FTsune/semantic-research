# Performance Analysis Report: jaccard

## Quantitative Metrics

- **Precision@1**: 0.9600
- **Precision@3**: 0.6867
- **Recall@3**: 0.6867
- **MRR**: 0.9767
- **Runtime (in seconds)**: 12.9358
- **Peak Memory (in KB)**: 1635.7129

---

## Qualitative Analysis

### Example 1
**Query:** What is the function of the Presidential Electoral Tribunal (PET)?

**Top-1 Match:**
> The Presidential Electoral Tribunal is a special tribunal composed of Supreme Court Justices that resolves electoral protests related to presidential and vice-presidential elections.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.2000`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.2000` - The Presidential Electoral Tribunal is a special tribunal composed of Supreme Court Justices that re...
2. ✅ `conceptual` | Score: `0.0769` - Electoral disputes require specialized forums to ensure the integrity of democratic processes....
3. ✅ `paraphrase` | Score: `0.0769` - The PET handles disputes about the outcome of elections for the highest executive positions in the P...


---

### Example 2
**Query:** What is 'estafa' under Philippine criminal law?

**Top-1 Match:**
> In Philippine law, estafa occurs when a person defrauds another of money or property through misrepresentation or deception.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2727`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2727` - In Philippine law, estafa occurs when a person defrauds another of money or property through misrepr...
2. ✅ `exact` | Score: `0.0667` - Estafa is a crime involving deceit or fraud where one party causes damage to another by abusing conf...
3. ❌ `irrelevant` | Score: `0.0000` - Trespassing is an offense that involves entering someone’s property without permission....


---

### Example 3
**Query:** What is the principle of 'in dubio pro reo' in Philippine jurisprudence?

**Top-1 Match:**
> When evidence is insufficient to establish guilt beyond reasonable doubt, the accused must be acquitted under the principle of in dubio pro reo.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2857`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2857` - When evidence is insufficient to establish guilt beyond reasonable doubt, the accused must be acquit...
2. ✅ `exact` | Score: `0.2353` - In dubio pro reo is a legal principle stating that in case of doubt, courts must rule in favor of th...
3. ❌ `irrelevant` | Score: `0.0909` - The Securities and Exchange Commission regulates corporations and securities in the Philippines....


---

### Example 4
**Query:** What is the concept of 'reserved powers' under the Local Government Code?

**Top-1 Match:**
> Under the Local Government Code, certain powers remain with the central government despite decentralization to local units.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.3333`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.3333` - Under the Local Government Code, certain powers remain with the central government despite decentral...
2. ✅ `exact` | Score: `0.3333` - Reserved powers are those authorities and functions retained by the national government even after d...
3. ❌ `irrelevant` | Score: `0.1667` - Local government units include provinces, cities, municipalities, and barangays....


---

### Example 5
**Query:** What is 'litis pendentia' as a ground for dismissal of a case?

**Top-1 Match:**
> Litis pendentia is a ground for dismissal when there is another pending action involving the same parties, same causes of action, and same reliefs sought.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.3333`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.3333` - Litis pendentia is a ground for dismissal when there is another pending action involving the same pa...
2. ✅ `paraphrase` | Score: `0.3000` - A case may be dismissed due to litis pendentia if an identical lawsuit is already being heard by ano...
3. ❌ `irrelevant` | Score: `0.0000` - Administrative agencies sometimes resolve disputes outside of the judiciary....


---

### Example 6
**Query:** What is the Cybercrime Prevention Act of 2012 (RA 10175)?

**Top-1 Match:**
> The Cybercrime Prevention Act criminalizes online offenses and provides mechanisms for investigation and prosecution of digital crimes.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2000`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2000` - The Cybercrime Prevention Act criminalizes online offenses and provides mechanisms for investigation...
2. ✅ `exact` | Score: `0.1765` - RA 10175 is a law that defines and penalizes cybercrimes in the Philippines, including illegal acces...
3. ❌ `irrelevant` | Score: `0.0000` - The National Telecommunications Commission regulates broadcast and telecommunications services....


---

### Example 7
**Query:** What is the concept of 'psychological incapacity' in Philippine family law?

**Top-1 Match:**
> In Philippine family law, a marriage may be declared void if one spouse is found to have psychological incapacity that prevents them from performing marital duties.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.3333`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.3333` - In Philippine family law, a marriage may be declared void if one spouse is found to have psychologic...
2. ✅ `exact` | Score: `0.1000` - Psychological incapacity refers to a serious psychological condition that renders a spouse incapable...
3. ✅ `conceptual` | Score: `0.0714` - The Family Code provides means to address fundamentally flawed marital relationships....


---

### Example 8
**Query:** What is the Anti-Money Laundering Act (AMLA) in the Philippines?

**Top-1 Match:**
> The Anti-Money Laundering Act criminalizes the process of concealing or disguising the proceeds of unlawful activities to make them appear to have originated from legitimate sources.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.2353`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.2353` - The Anti-Money Laundering Act criminalizes the process of concealing or disguising the proceeds of u...
2. ✅ `paraphrase` | Score: `0.0588` - AMLA establishes mechanisms to detect and prevent the conversion of illegally obtained funds into se...
3. ❌ `irrelevant` | Score: `0.0000` - The Bangko Sentral ng Pilipinas sets monetary policies for financial stability....


---

### Example 9
**Query:** What is 'separation of powers' in the Philippine government?

**Top-1 Match:**
> The Philippine government structure distributes powers among different branches to prevent concentration of authority and ensure checks and balances.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2143`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2143` - The Philippine government structure distributes powers among different branches to prevent concentra...
2. ✅ `exact` | Score: `0.2143` - Separation of powers is a constitutional principle that divides government authority among three bra...
3. ❌ `irrelevant` | Score: `0.1250` - The President serves as both head of state and head of government....


---

### Example 10
**Query:** What is the Philippine Competition Act (RA 10667)?

**Top-1 Match:**
> RA 10667 establishes the Philippine Competition Commission to prevent monopolies and ensure fair market competition.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.3333`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.3333` - RA 10667 establishes the Philippine Competition Commission to prevent monopolies and ensure fair mar...
2. ✅ `exact` | Score: `0.1579` - The Philippine Competition Act aims to protect consumer welfare by promoting competitive markets and...
3. ❌ `irrelevant` | Score: `0.0000` - Tariff rates on imported goods are adjusted periodically through executive orders....


---

### Example 11
**Query:** What is the concept of 'intellectual property rights' under Philippine law?

**Top-1 Match:**
> The Intellectual Property Office of the Philippines processes applications for IP registration.

**Top-1 Label:** `irrelevant` | **Relevant:** `False` | **Score:** `0.2727`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` | Score: `0.2727` - The Intellectual Property Office of the Philippines processes applications for IP registration....
2. ✅ `exact` | Score: `0.1667` - Intellectual property rights are legal protections granted to creators and inventors for their creat...
3. ✅ `conceptual` | Score: `0.1429` - Legal systems incentivize innovation by providing creators with exclusive rights to their intellectu...

⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.


---

### Example 12
**Query:** What is the principle of 'stare decisis' in Philippine jurisprudence?

**Top-1 Match:**
> Lower courts are bound by the decisions of the Supreme Court under the doctrine of stare decisis.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.1818`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.1818` - Lower courts are bound by the decisions of the Supreme Court under the doctrine of stare decisis....
2. ✅ `exact` | Score: `0.1765` - Stare decisis is the principle that courts follow precedents set by higher courts or their own previ...
3. ❌ `irrelevant` | Score: `0.0909` - The Rules of Court govern civil and criminal procedure in Philippine courts....


---

### Example 13
**Query:** What is 'bail' in Philippine criminal procedure?

**Top-1 Match:**
> In Philippine criminal procedure, bail allows temporary freedom for the accused while their case is being heard by posting security.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.3333`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.3333` - In Philippine criminal procedure, bail allows temporary freedom for the accused while their case is...
2. ❌ `irrelevant` | Score: `0.1111` - Criminal cases are initiated through the filing of a complaint or information....
3. ❌ `irrelevant` | Score: `0.1000` - The Philippine National Police is responsible for maintaining peace and order....


---

### Example 14
**Query:** What is the Anti-Hazing Law (RA 8049) in the Philippines?

**Top-1 Match:**
> The Anti-Hazing Law prohibits hazing and regulates initiation rites of fraternities, sororities, and organizations, imposing penalties for violations resulting in injury or death.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.1500`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.1500` - The Anti-Hazing Law prohibits hazing and regulates initiation rites of fraternities, sororities, and...
2. ✅ `paraphrase` | Score: `0.1176` - RA 8049 criminalizes dangerous initiation practices that cause physical or psychological harm to stu...
3. ❌ `irrelevant` | Score: `0.0909` - The Department of Education implements basic education policies in the Philippines....


---

### Example 15
**Query:** What is the principle of 'eminent domain' in Philippine property law?

**Top-1 Match:**
> Eminent domain is the inherent power of the state to take private property for public use upon payment of just compensation.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.2143`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.2143` - Eminent domain is the inherent power of the state to take private property for public use upon payme...
2. ✅ `paraphrase` | Score: `0.1176` - The government's authority to expropriate private land for public purposes, subject to fair payment,...
3. ✅ `conceptual` | Score: `0.0714` - Constitutional provisions balance private property rights with public interest needs....


---

### Example 16
**Query:** What is the 'Rule on DNA Evidence' in Philippine courts?

**Top-1 Match:**
> Philippine courts follow specific procedures for accepting and evaluating genetic test results as evidence.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2308`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2308` - Philippine courts follow specific procedures for accepting and evaluating genetic test results as ev...
2. ✅ `exact` | Score: `0.2143` - The Rule on DNA Evidence provides guidelines for the admissibility, collection, handling, and apprec...
3. ❌ `irrelevant` | Score: `0.0909` - The Philippine Statistics Authority conducts national censuses and surveys....


---

### Example 17
**Query:** What is the concept of 'visitorial power' over corporations?

**Top-1 Match:**
> Government regulators can inspect and investigate corporate activities through their visitorial powers.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2000`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2000` - Government regulators can inspect and investigate corporate activities through their visitorial powe...
2. ✅ `exact` | Score: `0.2000` - Visitorial power is the authority of regulatory agencies to examine the operations, books, and recor...
3. ❌ `irrelevant` | Score: `0.1111` - Corporations are required to submit annual financial statements....


---

### Example 18
**Query:** What is 'legal education' requirement for lawyers in the Philippines?

**Top-1 Match:**
> Continuing legal education is mandatory for practicing lawyers to stay updated with developments in the law.

**Top-1 Label:** `irrelevant` | **Relevant:** `False` | **Score:** `0.2500`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` | Score: `0.2500` - Continuing legal education is mandatory for practicing lawyers to stay updated with developments in...
2. ❌ `irrelevant` | Score: `0.2222` - The Integrated Bar of the Philippines is the national organization of lawyers....
3. ✅ `exact` | Score: `0.1765` - Legal education in the Philippines requires completion of a four-year Bachelor of Laws degree after...


---

### Example 19
**Query:** What is the concept of 'presidential immunity' in Philippine law?

**Top-1 Match:**
> While in office, the Philippine President enjoys immunity from certain legal proceedings related to their official functions.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.1429`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.1429` - While in office, the Philippine President enjoys immunity from certain legal proceedings related to...
2. ✅ `exact` | Score: `0.1250` - Presidential immunity is the legal doctrine that protects a sitting President from lawsuits for offi...
3. ❌ `irrelevant` | Score: `0.0000` - The Vice President can take over the presidency in cases of permanent vacancy....


---

### Example 20
**Query:** What is the Anti-Torture Act of 2009 (RA 9745)?

**Top-1 Match:**
> RA 9745 prohibits physical and mental torture and provides remedies and protection for victims.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2308`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2308` - RA 9745 prohibits physical and mental torture and provides remedies and protection for victims....
2. ✅ `exact` | Score: `0.1667` - The Anti-Torture Act criminalizes acts of torture and other cruel, inhuman, and degrading treatment...
3. ❌ `irrelevant` | Score: `0.0000` - The Commission on Human Rights monitors compliance with human rights standards....


---

### Example 21
**Query:** What is the doctrine of 'res judicata' in Philippine civil procedure?

**Top-1 Match:**
> Once a case has been decided with finality, the same issues cannot be relitigated between the same parties under the doctrine of res judicata.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2500`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2500` - Once a case has been decided with finality, the same issues cannot be relitigated between the same p...
2. ✅ `exact` | Score: `0.0909` - Res judicata is the principle that a final judgment on the merits by a court of competent jurisdicti...
3. ❌ `irrelevant` | Score: `0.0769` - Civil cases may involve claims for damages, specific performance, or injunction....


---

### Example 22
**Query:** What is the Philippine Deposit Insurance Corporation (PDIC)?

**Top-1 Match:**
> The PDIC is a government-owned corporation that protects depositors by providing insurance coverage for deposits in case of bank failures.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.2857`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.2857` - The PDIC is a government-owned corporation that protects depositors by providing insurance coverage...
2. ✅ `paraphrase` | Score: `0.1429` - PDIC insures bank deposits up to a specified maximum amount and liquidates closed banks to protect d...
3. ❌ `irrelevant` | Score: `0.0000` - The Securities and Exchange Commission oversees corporate registration and stock market activities....


---

### Example 23
**Query:** What is the 'writ of kalikasan' in Philippine environmental law?

**Top-1 Match:**
> The writ of kalikasan allows citizens to seek court protection against large-scale environmental harm affecting communities.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2000`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2000` - The writ of kalikasan allows citizens to seek court protection against large-scale environmental har...
2. ✅ `exact` | Score: `0.1429` - The writ of kalikasan is a legal remedy available to persons whose constitutional right to a balance...
3. ❌ `irrelevant` | Score: `0.0909` - The Department of Environment and Natural Resources implements environmental policies....


---

### Example 24
**Query:** What is 'warranty against eviction' in Philippine contracts of sale?

**Top-1 Match:**
> In sales contracts, sellers guarantee that buyers will not face legal troubles from other parties claiming ownership of the purchased property.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.1250`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.1250` - In sales contracts, sellers guarantee that buyers will not face legal troubles from other parties cl...
2. ✅ `exact` | Score: `0.1176` - Warranty against eviction is the seller's obligation to protect the buyer against legal claims of th...
3. ❌ `irrelevant` | Score: `0.1000` - A deed of sale transfers ownership from seller to buyer....


---

### Example 25
**Query:** What is the 'Anti-Fencing Law' (PD 1612) in the Philippines?

**Top-1 Match:**
> The Anti-Fencing Law penalizes the act of buying, selling, receiving, possessing, or in any manner dealing with articles or items that are known or should be known to have been derived from theft or robbery.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.1500`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.1500` - The Anti-Fencing Law penalizes the act of buying, selling, receiving, possessing, or in any manner d...
2. ✅ `paraphrase` | Score: `0.1250` - PD 1612 criminalizes the buying and selling of stolen goods to discourage theft by eliminating marke...
3. ✅ `conceptual` | Score: `0.0714` - Criminal laws address not only direct perpetrators but also those who facilitate or profit from illi...


---

### Example 26
**Query:** What is the principle of 'state immunity from suit' in the Philippines?

**Top-1 Match:**
> State immunity from suit is the principle that the State cannot be sued without its consent, based on the sovereign authority of the state and public policy considerations.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.3077`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.3077` - State immunity from suit is the principle that the State cannot be sued without its consent, based o...
2. ✅ `paraphrase` | Score: `0.0833` - The Philippine government is generally protected from lawsuits unless it expressly allows itself to...
3. ✅ `conceptual` | Score: `0.0625` - Sovereign immunity reflects the traditional view that subjecting governments to routine litigation m...


---

### Example 27
**Query:** What is the 'Blue Sky Law' in Philippine securities regulation?

**Top-1 Match:**
> The Blue Sky Law refers to the Securities Regulation Code that requires registration and disclosure of securities offerings to protect investors from fraudulent investments.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.3125`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.3125` - The Blue Sky Law refers to the Securities Regulation Code that requires registration and disclosure...
2. ✅ `paraphrase` | Score: `0.2000` - Philippine securities laws prevent the selling of speculative or fraudulent investments by requiring...
3. ❌ `irrelevant` | Score: `0.1667` - The Philippine Stock Exchange is the country's primary securities trading market....


---

### Example 28
**Query:** What is 'land reform' in Philippine agrarian law?

**Top-1 Match:**
> Philippine land reform programs aim to break up large landholdings and distribute them to farmers who till the land.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2308`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2308` - Philippine land reform programs aim to break up large landholdings and distribute them to farmers wh...
2. ✅ `exact` | Score: `0.1333` - Land reform is the comprehensive redistribution of agricultural lands to tenant-farmers and agricult...
3. ❌ `irrelevant` | Score: `0.1111` - Agriculture is a major sector in the Philippine economy....


---

### Example 29
**Query:** What is the 'Omnibus Election Code' in the Philippines?

**Top-1 Match:**
> The Omnibus Election Code is the comprehensive law governing the conduct of elections in the Philippines, including voter registration, candidacy requirements, campaign regulations, and election offenses.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.2500`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.2500` - The Omnibus Election Code is the comprehensive law governing the conduct of elections in the Philipp...
2. ✅ `paraphrase` | Score: `0.1429` - Batas Pambansa 881 outlines the rules and procedures for Philippine elections, from filing of candid...
3. ❌ `irrelevant` | Score: `0.1000` - The Philippine electoral system uses automated counting machines....


---

### Example 30
**Query:** What is the concept of 'piercing the veil of corporate fiction' in Philippine corporation law?

**Top-1 Match:**
> Piercing the veil of corporate fiction is a doctrine that disregards the separate legal personality of a corporation when it is used to defeat public convenience, justify wrong, protect fraud, or defend crime.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.2273`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.2273` - Piercing the veil of corporate fiction is a doctrine that disregards the separate legal personality...
2. ❌ `irrelevant` | Score: `0.1538` - Partnerships and cooperatives also have distinct legal personalities in Philippine law....
3. ❌ `irrelevant` | Score: `0.0833` - Corporations have juridical personality separate from their shareholders....


---

### Example 31
**Query:** What is the Anti-Carnapping Act of 1972 (RA 6539)?

**Top-1 Match:**
> The Anti-Carnapping Act defines and penalizes the theft of motor vehicles, imposing heavier penalties when violence, intimidation, or force is used.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.1765`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.1765` - The Anti-Carnapping Act defines and penalizes the theft of motor vehicles, imposing heavier penaltie...
2. ✅ `paraphrase` | Score: `0.1176` - RA 6539 criminalizes the unlawful taking of motor vehicles, with graduated penalties depending on ci...
3. ❌ `irrelevant` | Score: `0.0000` - Traffic rules are enforced by the Metropolitan Manila Development Authority....


---

### Example 32
**Query:** What is the 'Revised Corporation Code' (RA 11232) of the Philippines?

**Top-1 Match:**
> RA 11232 updated the Corporation Code to improve ease of doing business and align with global corporate governance standards.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2667`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2667` - RA 11232 updated the Corporation Code to improve ease of doing business and align with global corpor...
2. ✅ `exact` | Score: `0.1765` - The Revised Corporation Code modernizes Philippine corporate law by allowing one-person corporations...
3. ❌ `irrelevant` | Score: `0.0000` - Barangay micro business enterprises receive special tax incentives....


---

### Example 33
**Query:** What is the concept of 'public domain' in Philippine property law?

**Top-1 Match:**
> In Philippine law, public domain properties belong to the government and generally cannot be privately owned or sold.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.4167`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.4167` - In Philippine law, public domain properties belong to the government and generally cannot be private...
2. ✅ `exact` | Score: `0.0909` - Public domain refers to lands and resources owned by the State that cannot be alienated and are outs...
3. ❌ `irrelevant` | Score: `0.0000` - Mining companies must obtain permits from the government to operate....


---

### Example 34
**Query:** What is the 'Solo Parents' Welfare Act' (RA 8972) in the Philippines?

**Top-1 Match:**
> The Solo Parents' Welfare Act provides comprehensive support programs and benefits for single parents, including flexible work arrangements, parental leave, and educational benefits for their children.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.1905`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.1905` - The Solo Parents' Welfare Act provides comprehensive support programs and benefits for single parent...
2. ✅ `paraphrase` | Score: `0.1111` - RA 8972 establishes social protection and assistance for single mothers and fathers facing the chall...
3. ❌ `irrelevant` | Score: `0.0769` - The Department of Social Welfare and Development implements social service programs....


---

### Example 35
**Query:** What is the purpose of the Writ of Amparo in the Philippines?

**Top-1 Match:**
> In the Philippines, the Writ of Amparo serves as a safeguard for individuals facing threats to their fundamental rights, especially in situations involving state agents.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.1875`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.1875` - In the Philippines, the Writ of Amparo serves as a safeguard for individuals facing threats to their...
2. ✅ `exact` | Score: `0.1053` - The Writ of Amparo is a legal remedy designed to protect individuals from threats to their life, lib...
3. ❌ `irrelevant` | Score: `0.0714` - The Writ of Habeas Corpus is a legal action that requires a person under arrest to be brought before...


---

### Example 36
**Query:** Define 'force majeure' under Philippine law.

**Top-1 Match:**
> Unforeseen events like typhoons or earthquakes that hinder contract performance are considered force majeure in Philippine jurisprudence.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2000`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2000` - Unforeseen events like typhoons or earthquakes that hinder contract performance are considered force...
2. ✅ `exact` | Score: `0.1333` - Force majeure refers to events beyond the control of parties, such as natural disasters, which preve...
3. ❌ `irrelevant` | Score: `0.0000` - Disputes over contract interpretation are resolved by courts or arbitral tribunals....


---

### Example 37
**Query:** What rights are protected under the Indigenous Peoples' Rights Act (IPRA)?

**Top-1 Match:**
> Under IPRA, indigenous peoples are granted rights to their ancestral lands and the preservation of their cultural practices.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.3333`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.3333` - Under IPRA, indigenous peoples are granted rights to their ancestral lands and the preservation of t...
2. ✅ `exact` | Score: `0.3333` - The IPRA protects the rights of Indigenous Cultural Communities/Indigenous Peoples to their ancestra...
3. ✅ `conceptual` | Score: `0.0714` - Laws exist to ensure the protection and promotion of indigenous communities' heritage and traditions...


---

### Example 38
**Query:** What is the principle of 'parens patriae' in Philippine law?

**Top-1 Match:**
> The state has the authority to protect individuals who cannot protect themselves under the concept of parens patriae.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2000`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2000` - The state has the authority to protect individuals who cannot protect themselves under the concept o...
2. ✅ `exact` | Score: `0.1333` - Parens patriae is the doctrine that allows the state to act as guardian for those unable to care for...
3. ❌ `irrelevant` | Score: `0.0000` - The Department of Foreign Affairs handles diplomatic relations and overseas services....


---

### Example 39
**Query:** What does 'double jeopardy' mean in the context of criminal law?

**Top-1 Match:**
> A person cannot be tried again for a crime for which they were already acquitted or convicted, which is known as double jeopardy.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.1667`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.1667` - A person cannot be tried again for a crime for which they were already acquitted or convicted, which...
2. ✅ `exact` | Score: `0.1538` - Double jeopardy protects a person from being prosecuted twice for the same offense after acquittal o...
3. ❌ `irrelevant` | Score: `0.0769` - Criminal cases involve the state prosecuting a person for an alleged offense....


---

### Example 40
**Query:** What is the role of the Sandiganbayan in the Philippine judiciary?

**Top-1 Match:**
> The Sandiganbayan is a special court in the Philippines that hears cases involving graft and corruption by public officials.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.1538`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.1538` - The Sandiganbayan is a special court in the Philippines that hears cases involving graft and corrupt...
2. ✅ `conceptual` | Score: `0.0909` - There are special courts in the Philippines assigned to try specific categories of cases....
3. ✅ `paraphrase` | Score: `0.0769` - Cases involving corruption and misuse of government funds by public officials are handled by the San...


---

### Example 41
**Query:** What is the doctrine of exhaustion of administrative remedies?

**Top-1 Match:**
> The doctrine of exhaustion of administrative remedies requires a party to seek relief from administrative bodies before going to court.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.3636`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.3636` - The doctrine of exhaustion of administrative remedies requires a party to seek relief from administr...
2. ✅ `paraphrase` | Score: `0.1667` - Before filing a case in court, a person must first utilize the remedies available within the concern...
3. ✅ `conceptual` | Score: `0.1000` - Administrative bodies are empowered to resolve disputes within their specialized jurisdictions....


---

### Example 42
**Query:** Define 'agrarian reform' in the Philippine context.

**Top-1 Match:**
> In the Philippines, agrarian reform is a government initiative to transfer land ownership from landlords to tenants and farmers.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2308`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2308` - In the Philippines, agrarian reform is a government initiative to transfer land ownership from landl...
2. ✅ `exact` | Score: `0.1250` - Agrarian reform refers to the redistribution of agricultural land to farmers and farmworkers, aiming...
3. ❌ `irrelevant` | Score: `0.0000` - Public schools provide free education to all Filipino children....


---

### Example 43
**Query:** What is the Anti-Violence Against Women and Their Children Act (RA 9262)?

**Top-1 Match:**
> RA 9262 is a Philippine law that defines and penalizes violence against women and their children, including physical, psychological, and economic abuse.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.3125`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.3125` - RA 9262 is a Philippine law that defines and penalizes violence against women and their children, in...
2. ✅ `paraphrase` | Score: `0.2667` - The Anti-VAWC Act protects women and children from various forms of abuse committed by partners or f...
3. ❌ `irrelevant` | Score: `0.0769` - The Child and Youth Welfare Code protects the rights of minors....


---

### Example 44
**Query:** What is the purpose of the Katarungang Pambarangay system?

**Top-1 Match:**
> The Katarungang Pambarangay system is a local justice system that aims to amicably settle disputes at the barangay level before they escalate to formal courts.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.2000`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.2000` - The Katarungang Pambarangay system is a local justice system that aims to amicably settle disputes a...
2. ❌ `irrelevant` | Score: `0.0000` - Environmental agencies enforce laws protecting natural resources....
3. ❌ `irrelevant` | Score: `0.0000` - The Commission on Elections supervises the conduct of elections....


---

### Example 45
**Query:** What is the doctrine of primary jurisdiction in administrative law?

**Top-1 Match:**
> The doctrine of primary jurisdiction holds that courts should defer to administrative agencies when a case requires the agency’s specialized expertise.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.3077`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.3077` - The doctrine of primary jurisdiction holds that courts should defer to administrative agencies when...
2. ❌ `irrelevant` | Score: `0.1250` - Administrative agencies are part of the executive branch....
3. ❌ `irrelevant` | Score: `0.0000` - The Philippine National Police is responsible for maintaining peace and order....


---

### Example 46
**Query:** Explain the concept of 'just compensation' in expropriation cases.

**Top-1 Match:**
> In expropriation, property owners must be paid fairly for the land acquired by the government.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.0833`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.0833` - In expropriation, property owners must be paid fairly for the land acquired by the government....
2. ✅ `exact` | Score: `0.0588` - Just compensation refers to the fair value of property taken by the government for public use, ensur...
3. ❌ `irrelevant` | Score: `0.0000` - Philippine educational institutions follow the K-12 curriculum framework....


---

### Example 47
**Query:** What is the Anti-Terrorism Act of 2020 (RA 11479)?

**Top-1 Match:**
> The Anti-Terrorism Act allows law enforcers to arrest and monitor individuals suspected of terrorist acts.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.2143`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.2143` - The Anti-Terrorism Act allows law enforcers to arrest and monitor individuals suspected of terrorist...
2. ✅ `exact` | Score: `0.1765` - RA 11479 is a law enacted to strengthen the Philippines' legal framework against terrorism, includin...
3. ❌ `irrelevant` | Score: `0.0833` - The Dangerous Drugs Act penalizes possession and use of illegal drugs....


---

### Example 48
**Query:** What is the legal implication of 'informed consent' in medical treatment?

**Top-1 Match:**
> Informed consent means a patient agrees to a medical procedure after understanding its risks, benefits, and alternatives.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.1333`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.1333` - Informed consent means a patient agrees to a medical procedure after understanding its risks, benefi...
2. ✅ `conceptual` | Score: `0.0833` - Medical ethics require transparency and voluntary participation in procedures....
3. ✅ `paraphrase` | Score: `0.0714` - Doctors must ensure that patients voluntarily agree to treatment based on sufficient information....


---

### Example 49
**Query:** What is the role of the Civil Service Commission (CSC)?

**Top-1 Match:**
> The Civil Service Commission oversees the integrity and efficiency of the civil service and ensures merit-based appointments in government.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.2308`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.2308` - The Civil Service Commission oversees the integrity and efficiency of the civil service and ensures...
2. ❌ `irrelevant` | Score: `0.1000` - The Philippine Sports Commission develops national sports programs....
3. ❌ `irrelevant` | Score: `0.0909` - Local government units administer basic services to their constituents....


---

### Example 50
**Query:** What is the 'Comprehensive Dangerous Drugs Act' (RA 9165) of the Philippines?

**Top-1 Match:**
> The Comprehensive Dangerous Drugs Act criminalizes the importation, sale, possession, and use of illegal drugs, establishing rehabilitation programs and a national drug prevention campaign.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.2105`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.2105` - The Comprehensive Dangerous Drugs Act criminalizes the importation, sale, possession, and use of ill...
2. ❌ `irrelevant` | Score: `0.1667` - The Philippine Drug Enforcement Agency is the lead agency in anti-drug operations....
3. ✅ `paraphrase` | Score: `0.1667` - RA 9165 penalizes drug-related offenses and provides for treatment and rehabilitation of drug depend...


---

