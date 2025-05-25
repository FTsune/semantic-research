# Performance Analysis Report: sbert

## Quantitative Metrics

- **Precision@1**: 1.0000
- **Precision@3**: 0.8933
- **Recall@3**: 0.8933
- **MRR**: 1.0000
- **Runtime (in seconds)**: 57.8214
- **Peak Memory (in KB)**: 130.0098

---

## Qualitative Analysis

### Example 1
**Query:** What is the function of the Presidential Electoral Tribunal (PET)?

**Top-1 Match:**
> The Presidential Electoral Tribunal is a special tribunal composed of Supreme Court Justices that resolves electoral protests related to presidential and vice-presidential elections.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.6925`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.6925` - The Presidential Electoral Tribunal is a special tribunal composed of Supreme Court Justices that re...
2. ✅ `paraphrase` | Score: `0.6707` - The PET handles disputes about the outcome of elections for the highest executive positions in the P...
3. ✅ `conceptual` | Score: `0.5213` - Electoral disputes require specialized forums to ensure the integrity of democratic processes....


---

### Example 2
**Query:** What is 'estafa' under Philippine criminal law?

**Top-1 Match:**
> In Philippine law, estafa occurs when a person defrauds another of money or property through misrepresentation or deception.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.8342`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.8342` - In Philippine law, estafa occurs when a person defrauds another of money or property through misrepr...
2. ✅ `exact` | Score: `0.7686` - Estafa is a crime involving deceit or fraud where one party causes damage to another by abusing conf...
3. ✅ `conceptual` | Score: `0.3419` - The Revised Penal Code penalizes various forms of fraudulent activities that cause financial harm....


---

### Example 3
**Query:** What is the principle of 'in dubio pro reo' in Philippine jurisprudence?

**Top-1 Match:**
> In dubio pro reo is a legal principle stating that in case of doubt, courts must rule in favor of the accused, embodying the presumption of innocence.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7654`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7654` - In dubio pro reo is a legal principle stating that in case of doubt, courts must rule in favor of th...
2. ✅ `paraphrase` | Score: `0.5341` - When evidence is insufficient to establish guilt beyond reasonable doubt, the accused must be acquit...
3. ✅ `conceptual` | Score: `0.3193` - Criminal justice systems incorporate safeguards to protect potentially innocent individuals from wro...


---

### Example 4
**Query:** What is the concept of 'reserved powers' under the Local Government Code?

**Top-1 Match:**
> Reserved powers are those authorities and functions retained by the national government even after devolution under the Local Government Code.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.8620`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.8620` - Reserved powers are those authorities and functions retained by the national government even after d...
2. ✅ `paraphrase` | Score: `0.6284` - Under the Local Government Code, certain powers remain with the central government despite decentral...
3. ✅ `conceptual` | Score: `0.4890` - The distribution of powers between national and local authorities defines the Philippine governance...


---

### Example 5
**Query:** What is 'litis pendentia' as a ground for dismissal of a case?

**Top-1 Match:**
> Litis pendentia is a ground for dismissal when there is another pending action involving the same parties, same causes of action, and same reliefs sought.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.8709`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.8709` - Litis pendentia is a ground for dismissal when there is another pending action involving the same pa...
2. ✅ `paraphrase` | Score: `0.7545` - A case may be dismissed due to litis pendentia if an identical lawsuit is already being heard by ano...
3. ❌ `irrelevant` | Score: `0.4022` - The rules of court establish procedures for filing pleadings and motions....


---

### Example 6
**Query:** What is the Cybercrime Prevention Act of 2012 (RA 10175)?

**Top-1 Match:**
> RA 10175 is a law that defines and penalizes cybercrimes in the Philippines, including illegal access, data interference, and cyber libel.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.6999`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.6999` - RA 10175 is a law that defines and penalizes cybercrimes in the Philippines, including illegal acces...
2. ✅ `paraphrase` | Score: `0.6982` - The Cybercrime Prevention Act criminalizes online offenses and provides mechanisms for investigation...
3. ✅ `conceptual` | Score: `0.3580` - Legal frameworks have evolved to address technological developments and their implications for crimi...


---

### Example 7
**Query:** What is the concept of 'psychological incapacity' in Philippine family law?

**Top-1 Match:**
> Psychological incapacity refers to a serious psychological condition that renders a spouse incapable of fulfilling essential marital obligations, serving as a ground for declaration of nullity of marriage.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7629`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7629` - Psychological incapacity refers to a serious psychological condition that renders a spouse incapable...
2. ✅ `paraphrase` | Score: `0.7495` - In Philippine family law, a marriage may be declared void if one spouse is found to have psychologic...
3. ✅ `conceptual` | Score: `0.4168` - The Family Code provides means to address fundamentally flawed marital relationships....


---

### Example 8
**Query:** What is the Anti-Money Laundering Act (AMLA) in the Philippines?

**Top-1 Match:**
> AMLA establishes mechanisms to detect and prevent the conversion of illegally obtained funds into seemingly legal assets.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.6825`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.6825` - AMLA establishes mechanisms to detect and prevent the conversion of illegally obtained funds into se...
2. ✅ `exact` | Score: `0.6408` - The Anti-Money Laundering Act criminalizes the process of concealing or disguising the proceeds of u...
3. ✅ `conceptual` | Score: `0.4571` - Financial regulations aim to prevent criminal proceeds from entering the legitimate economy....


---

### Example 9
**Query:** What is 'separation of powers' in the Philippine government?

**Top-1 Match:**
> Separation of powers is a constitutional principle that divides government authority among three branches: executive, legislative, and judicial, with each serving as a check on the others.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7248`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7248` - Separation of powers is a constitutional principle that divides government authority among three bra...
2. ✅ `paraphrase` | Score: `0.7166` - The Philippine government structure distributes powers among different branches to prevent concentra...
3. ✅ `conceptual` | Score: `0.4461` - Constitutional democracies establish mechanisms to prevent abuse of power and protect democratic ins...


---

### Example 10
**Query:** What is the Philippine Competition Act (RA 10667)?

**Top-1 Match:**
> RA 10667 establishes the Philippine Competition Commission to prevent monopolies and ensure fair market competition.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.8059`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.8059` - RA 10667 establishes the Philippine Competition Commission to prevent monopolies and ensure fair mar...
2. ✅ `exact` | Score: `0.7477` - The Philippine Competition Act aims to protect consumer welfare by promoting competitive markets and...
3. ✅ `conceptual` | Score: `0.3859` - Economic regulations foster competitive business environments that benefit consumers and the economy...


---

### Example 11
**Query:** What is the concept of 'intellectual property rights' under Philippine law?

**Top-1 Match:**
> Philippine IP laws protect original works, inventions, and distinctive marks used in commerce from unauthorized use or reproduction.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.7590`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.7590` - Philippine IP laws protect original works, inventions, and distinctive marks used in commerce from u...
2. ✅ `exact` | Score: `0.6792` - Intellectual property rights are legal protections granted to creators and inventors for their creat...
3. ❌ `irrelevant` | Score: `0.6466` - The Intellectual Property Office of the Philippines processes applications for IP registration....


---

### Example 12
**Query:** What is the principle of 'stare decisis' in Philippine jurisprudence?

**Top-1 Match:**
> Stare decisis is the principle that courts follow precedents set by higher courts or their own previous decisions, ensuring consistency and predictability in the legal system.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.6791`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.6791` - Stare decisis is the principle that courts follow precedents set by higher courts or their own previ...
2. ❌ `irrelevant` | Score: `0.6146` - The Rules of Court govern civil and criminal procedure in Philippine courts....
3. ✅ `paraphrase` | Score: `0.5129` - Lower courts are bound by the decisions of the Supreme Court under the doctrine of stare decisis....


---

### Example 13
**Query:** What is 'bail' in Philippine criminal procedure?

**Top-1 Match:**
> In Philippine criminal procedure, bail allows temporary freedom for the accused while their case is being heard by posting security.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.8311`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.8311` - In Philippine criminal procedure, bail allows temporary freedom for the accused while their case is...
2. ✅ `exact` | Score: `0.7180` - Bail is the security given for the release of a person in custody, conditioned upon the person's app...
3. ✅ `conceptual` | Score: `0.4877` - Pretrial release mechanisms balance the presumption of innocence with ensuring court appearance....


---

### Example 14
**Query:** What is the Anti-Hazing Law (RA 8049) in the Philippines?

**Top-1 Match:**
> The Anti-Hazing Law prohibits hazing and regulates initiation rites of fraternities, sororities, and organizations, imposing penalties for violations resulting in injury or death.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.6515`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.6515` - The Anti-Hazing Law prohibits hazing and regulates initiation rites of fraternities, sororities, and...
2. ✅ `paraphrase` | Score: `0.5970` - RA 8049 criminalizes dangerous initiation practices that cause physical or psychological harm to stu...
3. ✅ `conceptual` | Score: `0.4332` - Laws protect young people from harmful traditions that may endanger their wellbeing....


---

### Example 15
**Query:** What is the principle of 'eminent domain' in Philippine property law?

**Top-1 Match:**
> Eminent domain is the inherent power of the state to take private property for public use upon payment of just compensation.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7367`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7367` - Eminent domain is the inherent power of the state to take private property for public use upon payme...
2. ✅ `paraphrase` | Score: `0.6419` - The government's authority to expropriate private land for public purposes, subject to fair payment,...
3. ✅ `conceptual` | Score: `0.4678` - Constitutional provisions balance private property rights with public interest needs....


---

### Example 16
**Query:** What is the 'Rule on DNA Evidence' in Philippine courts?

**Top-1 Match:**
> Philippine courts follow specific procedures for accepting and evaluating genetic test results as evidence.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.7978`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.7978` - Philippine courts follow specific procedures for accepting and evaluating genetic test results as ev...
2. ✅ `exact` | Score: `0.6839` - The Rule on DNA Evidence provides guidelines for the admissibility, collection, handling, and apprec...
3. ✅ `conceptual` | Score: `0.4728` - Modern scientific methods have been integrated into legal procedures to improve accuracy in fact-fin...


---

### Example 17
**Query:** What is the concept of 'visitorial power' over corporations?

**Top-1 Match:**
> Visitorial power is the authority of regulatory agencies to examine the operations, books, and records of corporations to ensure compliance with laws and regulations.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7395`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7395` - Visitorial power is the authority of regulatory agencies to examine the operations, books, and recor...
2. ✅ `paraphrase` | Score: `0.6085` - Government regulators can inspect and investigate corporate activities through their visitorial powe...
3. ✅ `conceptual` | Score: `0.4097` - Regulatory frameworks enable government oversight of business entities to protect public interest....


---

### Example 18
**Query:** What is 'legal education' requirement for lawyers in the Philippines?

**Top-1 Match:**
> Legal education in the Philippines requires completion of a four-year Bachelor of Laws degree after obtaining an undergraduate degree, followed by passing the Bar examinations.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.8062`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.8062` - Legal education in the Philippines requires completion of a four-year Bachelor of Laws degree after...
2. ✅ `paraphrase` | Score: `0.7809` - To become a lawyer in the Philippines, one must graduate from an accredited law school and pass the...
3. ❌ `irrelevant` | Score: `0.5948` - The Integrated Bar of the Philippines is the national organization of lawyers....


---

### Example 19
**Query:** What is the concept of 'presidential immunity' in Philippine law?

**Top-1 Match:**
> While in office, the Philippine President enjoys immunity from certain legal proceedings related to their official functions.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.8569`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.8569` - While in office, the Philippine President enjoys immunity from certain legal proceedings related to...
2. ✅ `exact` | Score: `0.7438` - Presidential immunity is the legal doctrine that protects a sitting President from lawsuits for offi...
3. ✅ `conceptual` | Score: `0.3893` - Executive privileges aim to ensure the effective functioning of the highest office without undue jud...


---

### Example 20
**Query:** What is the Anti-Torture Act of 2009 (RA 9745)?

**Top-1 Match:**
> The Anti-Torture Act criminalizes acts of torture and other cruel, inhuman, and degrading treatment or punishment, establishing liability for perpetrators, particularly state agents.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7359`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7359` - The Anti-Torture Act criminalizes acts of torture and other cruel, inhuman, and degrading treatment...
2. ✅ `paraphrase` | Score: `0.6920` - RA 9745 prohibits physical and mental torture and provides remedies and protection for victims....
3. ❌ `irrelevant` | Score: `0.4634` - The Commission on Human Rights monitors compliance with human rights standards....


---

### Example 21
**Query:** What is the doctrine of 'res judicata' in Philippine civil procedure?

**Top-1 Match:**
> Res judicata is the principle that a final judgment on the merits by a court of competent jurisdiction is conclusive between the parties and constitutes an absolute bar to a subsequent action involving the same cause of action.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.6981`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.6981` - Res judicata is the principle that a final judgment on the merits by a court of competent jurisdicti...
2. ✅ `paraphrase` | Score: `0.5124` - Once a case has been decided with finality, the same issues cannot be relitigated between the same p...
3. ❌ `irrelevant` | Score: `0.5050` - Courts issue decisions after trial and submission of evidence....


---

### Example 22
**Query:** What is the Philippine Deposit Insurance Corporation (PDIC)?

**Top-1 Match:**
> The PDIC is a government-owned corporation that protects depositors by providing insurance coverage for deposits in case of bank failures.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.8181`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.8181` - The PDIC is a government-owned corporation that protects depositors by providing insurance coverage...
2. ✅ `paraphrase` | Score: `0.7007` - PDIC insures bank deposits up to a specified maximum amount and liquidates closed banks to protect d...
3. ❌ `irrelevant` | Score: `0.5550` - The Bangko Sentral ng Pilipinas regulates the banking industry....


---

### Example 23
**Query:** What is the 'writ of kalikasan' in Philippine environmental law?

**Top-1 Match:**
> The writ of kalikasan is a legal remedy available to persons whose constitutional right to a balanced and healthful ecology is violated by an environmental damage of such magnitude that it threatens life, health, or property.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.8185`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.8185` - The writ of kalikasan is a legal remedy available to persons whose constitutional right to a balance...
2. ✅ `paraphrase` | Score: `0.7830` - The writ of kalikasan allows citizens to seek court protection against large-scale environmental har...
3. ✅ `conceptual` | Score: `0.4909` - Special legal procedures exist to address environmental issues and enforce constitutional guarantees...


---

### Example 24
**Query:** What is 'warranty against eviction' in Philippine contracts of sale?

**Top-1 Match:**
> Warranty against eviction is the seller's obligation to protect the buyer against legal claims of third persons that may disturb the buyer's peaceful possession of the thing sold.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.8316`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.8316` - Warranty against eviction is the seller's obligation to protect the buyer against legal claims of th...
2. ✅ `paraphrase` | Score: `0.5491` - In sales contracts, sellers guarantee that buyers will not face legal troubles from other parties cl...
3. ✅ `conceptual` | Score: `0.5316` - Contract law provides protections for purchasers against hidden defects in title....


---

### Example 25
**Query:** What is the 'Anti-Fencing Law' (PD 1612) in the Philippines?

**Top-1 Match:**
> The Anti-Fencing Law penalizes the act of buying, selling, receiving, possessing, or in any manner dealing with articles or items that are known or should be known to have been derived from theft or robbery.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7021`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7021` - The Anti-Fencing Law penalizes the act of buying, selling, receiving, possessing, or in any manner d...
2. ✅ `paraphrase` | Score: `0.5051` - PD 1612 criminalizes the buying and selling of stolen goods to discourage theft by eliminating marke...
3. ✅ `conceptual` | Score: `0.2140` - Criminal laws address not only direct perpetrators but also those who facilitate or profit from illi...


---

### Example 26
**Query:** What is the principle of 'state immunity from suit' in the Philippines?

**Top-1 Match:**
> The Philippine government is generally protected from lawsuits unless it expressly allows itself to be sued.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.7696`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.7696` - The Philippine government is generally protected from lawsuits unless it expressly allows itself to...
2. ✅ `exact` | Score: `0.7173` - State immunity from suit is the principle that the State cannot be sued without its consent, based o...
3. ✅ `conceptual` | Score: `0.5010` - Sovereign immunity reflects the traditional view that subjecting governments to routine litigation m...


---

### Example 27
**Query:** What is the 'Blue Sky Law' in Philippine securities regulation?

**Top-1 Match:**
> The Blue Sky Law refers to the Securities Regulation Code that requires registration and disclosure of securities offerings to protect investors from fraudulent investments.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7636`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7636` - The Blue Sky Law refers to the Securities Regulation Code that requires registration and disclosure...
2. ✅ `paraphrase` | Score: `0.6007` - Philippine securities laws prevent the selling of speculative or fraudulent investments by requiring...
3. ❌ `irrelevant` | Score: `0.4910` - The Philippine Stock Exchange is the country's primary securities trading market....


---

### Example 28
**Query:** What is 'land reform' in Philippine agrarian law?

**Top-1 Match:**
> Philippine land reform programs aim to break up large landholdings and distribute them to farmers who till the land.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.8072`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.8072` - Philippine land reform programs aim to break up large landholdings and distribute them to farmers wh...
2. ✅ `exact` | Score: `0.7465` - Land reform is the comprehensive redistribution of agricultural lands to tenant-farmers and agricult...
3. ✅ `conceptual` | Score: `0.5459` - Rural development policies address historical inequities in land ownership and access....


---

### Example 29
**Query:** What is the 'Omnibus Election Code' in the Philippines?

**Top-1 Match:**
> The Omnibus Election Code is the comprehensive law governing the conduct of elections in the Philippines, including voter registration, candidacy requirements, campaign regulations, and election offenses.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.9040`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.9040` - The Omnibus Election Code is the comprehensive law governing the conduct of elections in the Philipp...
2. ✅ `paraphrase` | Score: `0.7096` - Batas Pambansa 881 outlines the rules and procedures for Philippine elections, from filing of candid...
3. ❌ `irrelevant` | Score: `0.6032` - The Philippine electoral system uses automated counting machines....


---

### Example 30
**Query:** What is the concept of 'piercing the veil of corporate fiction' in Philippine corporation law?

**Top-1 Match:**
> Piercing the veil of corporate fiction is a doctrine that disregards the separate legal personality of a corporation when it is used to defeat public convenience, justify wrong, protect fraud, or defend crime.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.8251`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.8251` - Piercing the veil of corporate fiction is a doctrine that disregards the separate legal personality...
2. ✅ `conceptual` | Score: `0.4908` - Legal doctrines prevent the abuse of corporate structures to evade liability or perpetrate injustice...
3. ❌ `irrelevant` | Score: `0.4707` - Partnerships and cooperatives also have distinct legal personalities in Philippine law....


---

### Example 31
**Query:** What is the Anti-Carnapping Act of 1972 (RA 6539)?

**Top-1 Match:**
> The Anti-Carnapping Act defines and penalizes the theft of motor vehicles, imposing heavier penalties when violence, intimidation, or force is used.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7289`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7289` - The Anti-Carnapping Act defines and penalizes the theft of motor vehicles, imposing heavier penaltie...
2. ✅ `paraphrase` | Score: `0.5447` - RA 6539 criminalizes the unlawful taking of motor vehicles, with graduated penalties depending on ci...
3. ✅ `conceptual` | Score: `0.3723` - Special criminal laws address specific forms of property crimes that have significant social impact....


---

### Example 32
**Query:** What is the 'Revised Corporation Code' (RA 11232) of the Philippines?

**Top-1 Match:**
> The Revised Corporation Code modernizes Philippine corporate law by allowing one-person corporations, perpetual corporate existence, and electronic filing, among other innovations.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7347`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7347` - The Revised Corporation Code modernizes Philippine corporate law by allowing one-person corporations...
2. ✅ `paraphrase` | Score: `0.6988` - RA 11232 updated the Corporation Code to improve ease of doing business and align with global corpor...
3. ✅ `conceptual` | Score: `0.3755` - Corporate laws evolve to accommodate changing business environments and technological advancements....


---

### Example 33
**Query:** What is the concept of 'public domain' in Philippine property law?

**Top-1 Match:**
> In Philippine law, public domain properties belong to the government and generally cannot be privately owned or sold.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.8489`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.8489` - In Philippine law, public domain properties belong to the government and generally cannot be private...
2. ✅ `exact` | Score: `0.6986` - Public domain refers to lands and resources owned by the State that cannot be alienated and are outs...
3. ❌ `irrelevant` | Score: `0.4621` - Private lands can be registered under the Torrens system....


---

### Example 34
**Query:** What is the 'Solo Parents' Welfare Act' (RA 8972) in the Philippines?

**Top-1 Match:**
> RA 8972 establishes social protection and assistance for single mothers and fathers facing the challenges of raising children alone.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.7167`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.7167` - RA 8972 establishes social protection and assistance for single mothers and fathers facing the chall...
2. ✅ `exact` | Score: `0.7076` - The Solo Parents' Welfare Act provides comprehensive support programs and benefits for single parent...
3. ✅ `conceptual` | Score: `0.5866` - Social legislation addresses the needs of vulnerable family structures and promotes child welfare....


---

### Example 35
**Query:** What is the purpose of the Writ of Amparo in the Philippines?

**Top-1 Match:**
> In the Philippines, the Writ of Amparo serves as a safeguard for individuals facing threats to their fundamental rights, especially in situations involving state agents.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.7807`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.7807` - In the Philippines, the Writ of Amparo serves as a safeguard for individuals facing threats to their...
2. ✅ `exact` | Score: `0.6919` - The Writ of Amparo is a legal remedy designed to protect individuals from threats to their life, lib...
3. ❌ `irrelevant` | Score: `0.4464` - The Writ of Habeas Corpus is a legal action that requires a person under arrest to be brought before...


---

### Example 36
**Query:** Define 'force majeure' under Philippine law.

**Top-1 Match:**
> Unforeseen events like typhoons or earthquakes that hinder contract performance are considered force majeure in Philippine jurisprudence.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.7920`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.7920` - Unforeseen events like typhoons or earthquakes that hinder contract performance are considered force...
2. ✅ `exact` | Score: `0.6957` - Force majeure refers to events beyond the control of parties, such as natural disasters, which preve...
3. ❌ `irrelevant` | Score: `0.3455` - Breach of contract occurs when one party fails to fulfill their obligations....


---

### Example 37
**Query:** What rights are protected under the Indigenous Peoples' Rights Act (IPRA)?

**Top-1 Match:**
> The IPRA protects the rights of Indigenous Cultural Communities/Indigenous Peoples to their ancestral domains, self-governance, social justice, and cultural integrity.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.8359`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.8359` - The IPRA protects the rights of Indigenous Cultural Communities/Indigenous Peoples to their ancestra...
2. ✅ `paraphrase` | Score: `0.8118` - Under IPRA, indigenous peoples are granted rights to their ancestral lands and the preservation of t...
3. ✅ `conceptual` | Score: `0.6437` - Laws exist to ensure the protection and promotion of indigenous communities' heritage and traditions...


---

### Example 38
**Query:** What is the principle of 'parens patriae' in Philippine law?

**Top-1 Match:**
> Parens patriae is the doctrine that allows the state to act as guardian for those unable to care for themselves, such as minors or persons with disabilities.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.6914`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.6914` - Parens patriae is the doctrine that allows the state to act as guardian for those unable to care for...
2. ✅ `paraphrase` | Score: `0.5952` - The state has the authority to protect individuals who cannot protect themselves under the concept o...
3. ✅ `conceptual` | Score: `0.3030` - Minors and vulnerable individuals are provided special legal protections....


---

### Example 39
**Query:** What does 'double jeopardy' mean in the context of criminal law?

**Top-1 Match:**
> Double jeopardy protects a person from being prosecuted twice for the same offense after acquittal or conviction.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.8496`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.8496` - Double jeopardy protects a person from being prosecuted twice for the same offense after acquittal o...
2. ✅ `paraphrase` | Score: `0.6160` - A person cannot be tried again for a crime for which they were already acquitted or convicted, which...
3. ✅ `conceptual` | Score: `0.4812` - The legal system includes protections against repeated prosecution....


---

### Example 40
**Query:** What is the role of the Sandiganbayan in the Philippine judiciary?

**Top-1 Match:**
> The Sandiganbayan is a special court in the Philippines that hears cases involving graft and corruption by public officials.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7697`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7697` - The Sandiganbayan is a special court in the Philippines that hears cases involving graft and corrupt...
2. ✅ `paraphrase` | Score: `0.6507` - Cases involving corruption and misuse of government funds by public officials are handled by the San...
3. ✅ `conceptual` | Score: `0.5886` - There are special courts in the Philippines assigned to try specific categories of cases....


---

### Example 41
**Query:** What is the doctrine of exhaustion of administrative remedies?

**Top-1 Match:**
> The doctrine of exhaustion of administrative remedies requires a party to seek relief from administrative bodies before going to court.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.8167`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.8167` - The doctrine of exhaustion of administrative remedies requires a party to seek relief from administr...
2. ✅ `paraphrase` | Score: `0.5079` - Before filing a case in court, a person must first utilize the remedies available within the concern...
3. ✅ `conceptual` | Score: `0.4926` - Administrative bodies are empowered to resolve disputes within their specialized jurisdictions....


---

### Example 42
**Query:** Define 'agrarian reform' in the Philippine context.

**Top-1 Match:**
> In the Philippines, agrarian reform is a government initiative to transfer land ownership from landlords to tenants and farmers.

**Top-1 Label:** `paraphrase` | **Relevant:** `True` | **Score:** `0.8825`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` | Score: `0.8825` - In the Philippines, agrarian reform is a government initiative to transfer land ownership from landl...
2. ✅ `exact` | Score: `0.7306` - Agrarian reform refers to the redistribution of agricultural land to farmers and farmworkers, aiming...
3. ✅ `conceptual` | Score: `0.4872` - Programs exist to ensure equitable land distribution and uplift rural communities....


---

### Example 43
**Query:** What is the Anti-Violence Against Women and Their Children Act (RA 9262)?

**Top-1 Match:**
> RA 9262 is a Philippine law that defines and penalizes violence against women and their children, including physical, psychological, and economic abuse.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7144`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7144` - RA 9262 is a Philippine law that defines and penalizes violence against women and their children, in...
2. ✅ `paraphrase` | Score: `0.6673` - The Anti-VAWC Act protects women and children from various forms of abuse committed by partners or f...
3. ✅ `conceptual` | Score: `0.5462` - Philippine laws aim to safeguard vulnerable groups from domestic violence....


---

### Example 44
**Query:** What is the purpose of the Katarungang Pambarangay system?

**Top-1 Match:**
> The Katarungang Pambarangay system is a local justice system that aims to amicably settle disputes at the barangay level before they escalate to formal courts.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7761`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7761` - The Katarungang Pambarangay system is a local justice system that aims to amicably settle disputes a...
2. ✅ `paraphrase` | Score: `0.3462` - Barangay justice promotes community-based resolution of disputes through conciliation and mediation....
3. ❌ `irrelevant` | Score: `0.2125` - The Regional Trial Court handles serious civil and criminal cases....


---

### Example 45
**Query:** What is the doctrine of primary jurisdiction in administrative law?

**Top-1 Match:**
> The doctrine of primary jurisdiction holds that courts should defer to administrative agencies when a case requires the agency’s specialized expertise.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7781`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7781` - The doctrine of primary jurisdiction holds that courts should defer to administrative agencies when...
2. ✅ `conceptual` | Score: `0.4325` - Some disputes are better handled by expert government bodies before judicial intervention....
3. ❌ `irrelevant` | Score: `0.3919` - Administrative agencies are part of the executive branch....


---

### Example 46
**Query:** Explain the concept of 'just compensation' in expropriation cases.

**Top-1 Match:**
> Just compensation refers to the fair value of property taken by the government for public use, ensuring that the owner is not left at a disadvantage.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7147`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7147` - Just compensation refers to the fair value of property taken by the government for public use, ensur...
2. ✅ `paraphrase` | Score: `0.6930` - In expropriation, property owners must be paid fairly for the land acquired by the government....
3. ✅ `conceptual` | Score: `0.4129` - Constitutional rights protect property owners from unjust land seizures....


---

### Example 47
**Query:** What is the Anti-Terrorism Act of 2020 (RA 11479)?

**Top-1 Match:**
> RA 11479 is a law enacted to strengthen the Philippines' legal framework against terrorism, including provisions for extended detention and surveillance.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.6683`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.6683` - RA 11479 is a law enacted to strengthen the Philippines' legal framework against terrorism, includin...
2. ✅ `paraphrase` | Score: `0.6625` - The Anti-Terrorism Act allows law enforcers to arrest and monitor individuals suspected of terrorist...
3. ✅ `conceptual` | Score: `0.5801` - National security laws grant the government broader powers to combat terrorism....


---

### Example 48
**Query:** What is the legal implication of 'informed consent' in medical treatment?

**Top-1 Match:**
> Informed consent means a patient agrees to a medical procedure after understanding its risks, benefits, and alternatives.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.8087`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.8087` - Informed consent means a patient agrees to a medical procedure after understanding its risks, benefi...
2. ✅ `paraphrase` | Score: `0.6394` - Doctors must ensure that patients voluntarily agree to treatment based on sufficient information....
3. ✅ `conceptual` | Score: `0.5464` - Medical ethics require transparency and voluntary participation in procedures....


---

### Example 49
**Query:** What is the role of the Civil Service Commission (CSC)?

**Top-1 Match:**
> The Civil Service Commission oversees the integrity and efficiency of the civil service and ensures merit-based appointments in government.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.7731`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.7731` - The Civil Service Commission oversees the integrity and efficiency of the civil service and ensures...
2. ✅ `paraphrase` | Score: `0.7301` - CSC is responsible for ensuring fair hiring and disciplinary standards for government employees....
3. ✅ `conceptual` | Score: `0.4516` - Government institutions are expected to uphold professionalism and accountability in public service....


---

### Example 50
**Query:** What is the 'Comprehensive Dangerous Drugs Act' (RA 9165) of the Philippines?

**Top-1 Match:**
> The Comprehensive Dangerous Drugs Act criminalizes the importation, sale, possession, and use of illegal drugs, establishing rehabilitation programs and a national drug prevention campaign.

**Top-1 Label:** `exact` | **Relevant:** `True` | **Score:** `0.6725`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` | Score: `0.6725` - The Comprehensive Dangerous Drugs Act criminalizes the importation, sale, possession, and use of ill...
2. ✅ `paraphrase` | Score: `0.6465` - RA 9165 penalizes drug-related offenses and provides for treatment and rehabilitation of drug depend...
3. ❌ `irrelevant` | Score: `0.6113` - The Philippine Drug Enforcement Agency is the lead agency in anti-drug operations....


---

