# Performance Analysis Report: bertscore

## Quantitative Metrics

- **Precision@1**: 0.8200
- **Precision@3**: 0.6733
- **Recall@3**: 0.6733
- **MRR**: 0.9067
- **Runtime (in seconds)**: 835.3911
- **Peak Memory (in KB)**: 26296.9375

---

## Qualitative Analysis

### Example 1
**Query:** What is the function of the Presidential Electoral Tribunal (PET)?

**Top-1 Match:**
> The National Economic and Development Authority evaluates socioeconomic plans and programs.

**Top-1 Label:** `irrelevant` | **Relevant:** `False`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` - The National Economic and Development Authority evaluates socioeconomic plans and programs....
2. ✅ `exact` - The Presidential Electoral Tribunal is a special tribunal composed of Supreme Court Justices that re...
3. ✅ `paraphrase` - The PET handles disputes about the outcome of elections for the highest executive positions in the P...

⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.


---

### Example 2
**Query:** What is 'estafa' under Philippine criminal law?

**Top-1 Match:**
> In Philippine law, estafa occurs when a person defrauds another of money or property through misrepresentation or deception.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - In Philippine law, estafa occurs when a person defrauds another of money or property through misrepr...
2. ✅ `conceptual` - The Revised Penal Code penalizes various forms of fraudulent activities that cause financial harm....
3. ❌ `irrelevant` - The Public Attorney's Office provides free legal services to indigent clients....


---

### Example 3
**Query:** What is the principle of 'in dubio pro reo' in Philippine jurisprudence?

**Top-1 Match:**
> In dubio pro reo is a legal principle stating that in case of doubt, courts must rule in favor of the accused, embodying the presumption of innocence.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - In dubio pro reo is a legal principle stating that in case of doubt, courts must rule in favor of th...
2. ❌ `irrelevant` - The Securities and Exchange Commission regulates corporations and securities in the Philippines....
3. ✅ `paraphrase` - When evidence is insufficient to establish guilt beyond reasonable doubt, the accused must be acquit...


---

### Example 4
**Query:** What is the concept of 'reserved powers' under the Local Government Code?

**Top-1 Match:**
> Reserved powers are those authorities and functions retained by the national government even after devolution under the Local Government Code.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - Reserved powers are those authorities and functions retained by the national government even after d...
2. ✅ `paraphrase` - Under the Local Government Code, certain powers remain with the central government despite decentral...
3. ✅ `conceptual` - The distribution of powers between national and local authorities defines the Philippine governance...


---

### Example 5
**Query:** What is 'litis pendentia' as a ground for dismissal of a case?

**Top-1 Match:**
> Litis pendentia is a ground for dismissal when there is another pending action involving the same parties, same causes of action, and same reliefs sought.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - Litis pendentia is a ground for dismissal when there is another pending action involving the same pa...
2. ✅ `paraphrase` - A case may be dismissed due to litis pendentia if an identical lawsuit is already being heard by ano...
3. ❌ `irrelevant` - The rules of court establish procedures for filing pleadings and motions....


---

### Example 6
**Query:** What is the Cybercrime Prevention Act of 2012 (RA 10175)?

**Top-1 Match:**
> RA 10175 is a law that defines and penalizes cybercrimes in the Philippines, including illegal access, data interference, and cyber libel.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - RA 10175 is a law that defines and penalizes cybercrimes in the Philippines, including illegal acces...
2. ✅ `paraphrase` - The Cybercrime Prevention Act criminalizes online offenses and provides mechanisms for investigation...
3. ❌ `irrelevant` - The Department of Information and Communications Technology oversees the country's ICT development....


---

### Example 7
**Query:** What is the concept of 'psychological incapacity' in Philippine family law?

**Top-1 Match:**
> In Philippine family law, a marriage may be declared void if one spouse is found to have psychological incapacity that prevents them from performing marital duties.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - In Philippine family law, a marriage may be declared void if one spouse is found to have psychologic...
2. ✅ `conceptual` - The Family Code provides means to address fundamentally flawed marital relationships....
3. ✅ `exact` - Psychological incapacity refers to a serious psychological condition that renders a spouse incapable...


---

### Example 8
**Query:** What is the Anti-Money Laundering Act (AMLA) in the Philippines?

**Top-1 Match:**
> The Anti-Money Laundering Act criminalizes the process of concealing or disguising the proceeds of unlawful activities to make them appear to have originated from legitimate sources.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - The Anti-Money Laundering Act criminalizes the process of concealing or disguising the proceeds of u...
2. ❌ `irrelevant` - The Bangko Sentral ng Pilipinas sets monetary policies for financial stability....
3. ✅ `paraphrase` - AMLA establishes mechanisms to detect and prevent the conversion of illegally obtained funds into se...


---

### Example 9
**Query:** What is 'separation of powers' in the Philippine government?

**Top-1 Match:**
> The Philippine government structure distributes powers among different branches to prevent concentration of authority and ensure checks and balances.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - The Philippine government structure distributes powers among different branches to prevent concentra...
2. ✅ `exact` - Separation of powers is a constitutional principle that divides government authority among three bra...
3. ❌ `irrelevant` - The Supreme Court of the Philippines is composed of a Chief Justice and Associate Justices....


---

### Example 10
**Query:** What is the Philippine Competition Act (RA 10667)?

**Top-1 Match:**
> RA 10667 establishes the Philippine Competition Commission to prevent monopolies and ensure fair market competition.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - RA 10667 establishes the Philippine Competition Commission to prevent monopolies and ensure fair mar...
2. ❌ `irrelevant` - Business name registration is handled by the Department of Trade and Industry....
3. ✅ `exact` - The Philippine Competition Act aims to protect consumer welfare by promoting competitive markets and...


---

### Example 11
**Query:** What is the concept of 'intellectual property rights' under Philippine law?

**Top-1 Match:**
> The Intellectual Property Office of the Philippines processes applications for IP registration.

**Top-1 Label:** `irrelevant` | **Relevant:** `False`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` - The Intellectual Property Office of the Philippines processes applications for IP registration....
2. ❌ `irrelevant` - The Department of Trade and Industry handles business name registrations in the Philippines....
3. ✅ `conceptual` - Legal systems incentivize innovation by providing creators with exclusive rights to their intellectu...


---

### Example 12
**Query:** What is the principle of 'stare decisis' in Philippine jurisprudence?

**Top-1 Match:**
> The Rules of Court govern civil and criminal procedure in Philippine courts.

**Top-1 Label:** `irrelevant` | **Relevant:** `False`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` - The Rules of Court govern civil and criminal procedure in Philippine courts....
2. ✅ `exact` - Stare decisis is the principle that courts follow precedents set by higher courts or their own previ...
3. ✅ `paraphrase` - Lower courts are bound by the decisions of the Supreme Court under the doctrine of stare decisis....

⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.


---

### Example 13
**Query:** What is 'bail' in Philippine criminal procedure?

**Top-1 Match:**
> In Philippine criminal procedure, bail allows temporary freedom for the accused while their case is being heard by posting security.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - In Philippine criminal procedure, bail allows temporary freedom for the accused while their case is...
2. ❌ `irrelevant` - The Philippine National Police is responsible for maintaining peace and order....
3. ❌ `irrelevant` - Criminal cases are initiated through the filing of a complaint or information....


---

### Example 14
**Query:** What is the Anti-Hazing Law (RA 8049) in the Philippines?

**Top-1 Match:**
> The Department of Education implements basic education policies in the Philippines.

**Top-1 Label:** `irrelevant` | **Relevant:** `False`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` - The Department of Education implements basic education policies in the Philippines....
2. ✅ `paraphrase` - RA 8049 criminalizes dangerous initiation practices that cause physical or psychological harm to stu...
3. ✅ `exact` - The Anti-Hazing Law prohibits hazing and regulates initiation rites of fraternities, sororities, and...

⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.


---

### Example 15
**Query:** What is the principle of 'eminent domain' in Philippine property law?

**Top-1 Match:**
> The Land Registration Authority oversees the country’s land title system.

**Top-1 Label:** `irrelevant` | **Relevant:** `False`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` - The Land Registration Authority oversees the country’s land title system....
2. ✅ `exact` - Eminent domain is the inherent power of the state to take private property for public use upon payme...
3. ✅ `paraphrase` - The government's authority to expropriate private land for public purposes, subject to fair payment,...

⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.


---

### Example 16
**Query:** What is the 'Rule on DNA Evidence' in Philippine courts?

**Top-1 Match:**
> Philippine courts follow specific procedures for accepting and evaluating genetic test results as evidence.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - Philippine courts follow specific procedures for accepting and evaluating genetic test results as ev...
2. ✅ `exact` - The Rule on DNA Evidence provides guidelines for the admissibility, collection, handling, and apprec...
3. ✅ `conceptual` - Modern scientific methods have been integrated into legal procedures to improve accuracy in fact-fin...


---

### Example 17
**Query:** What is the concept of 'visitorial power' over corporations?

**Top-1 Match:**
> Visitorial power is the authority of regulatory agencies to examine the operations, books, and records of corporations to ensure compliance with laws and regulations.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - Visitorial power is the authority of regulatory agencies to examine the operations, books, and recor...
2. ✅ `paraphrase` - Government regulators can inspect and investigate corporate activities through their visitorial powe...
3. ❌ `irrelevant` - Corporations are required to submit annual financial statements....


---

### Example 18
**Query:** What is 'legal education' requirement for lawyers in the Philippines?

**Top-1 Match:**
> To become a lawyer in the Philippines, one must graduate from an accredited law school and pass the Bar exams administered by the Supreme Court.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - To become a lawyer in the Philippines, one must graduate from an accredited law school and pass the...
2. ❌ `irrelevant` - Continuing legal education is mandatory for practicing lawyers to stay updated with developments in...
3. ❌ `irrelevant` - The Integrated Bar of the Philippines is the national organization of lawyers....


---

### Example 19
**Query:** What is the concept of 'presidential immunity' in Philippine law?

**Top-1 Match:**
> While in office, the Philippine President enjoys immunity from certain legal proceedings related to their official functions.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - While in office, the Philippine President enjoys immunity from certain legal proceedings related to...
2. ✅ `conceptual` - Executive privileges aim to ensure the effective functioning of the highest office without undue jud...
3. ❌ `irrelevant` - Cabinet meetings are typically held in Malacañang Palace....


---

### Example 20
**Query:** What is the Anti-Torture Act of 2009 (RA 9745)?

**Top-1 Match:**
> RA 9745 prohibits physical and mental torture and provides remedies and protection for victims.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - RA 9745 prohibits physical and mental torture and provides remedies and protection for victims....
2. ❌ `irrelevant` - The Department of Justice oversees the National Prosecution Service....
3. ✅ `exact` - The Anti-Torture Act criminalizes acts of torture and other cruel, inhuman, and degrading treatment...


---

### Example 21
**Query:** What is the doctrine of 'res judicata' in Philippine civil procedure?

**Top-1 Match:**
> Res judicata is the principle that a final judgment on the merits by a court of competent jurisdiction is conclusive between the parties and constitutes an absolute bar to a subsequent action involving the same cause of action.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - Res judicata is the principle that a final judgment on the merits by a court of competent jurisdicti...
2. ✅ `paraphrase` - Once a case has been decided with finality, the same issues cannot be relitigated between the same p...
3. ❌ `irrelevant` - Civil cases may involve claims for damages, specific performance, or injunction....


---

### Example 22
**Query:** What is the Philippine Deposit Insurance Corporation (PDIC)?

**Top-1 Match:**
> The PDIC is a government-owned corporation that protects depositors by providing insurance coverage for deposits in case of bank failures.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - The PDIC is a government-owned corporation that protects depositors by providing insurance coverage...
2. ❌ `irrelevant` - The Bangko Sentral ng Pilipinas regulates the banking industry....
3. ❌ `irrelevant` - The Securities and Exchange Commission oversees corporate registration and stock market activities....


---

### Example 23
**Query:** What is the 'writ of kalikasan' in Philippine environmental law?

**Top-1 Match:**
> The writ of kalikasan allows citizens to seek court protection against large-scale environmental harm affecting communities.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - The writ of kalikasan allows citizens to seek court protection against large-scale environmental har...
2. ✅ `exact` - The writ of kalikasan is a legal remedy available to persons whose constitutional right to a balance...
3. ❌ `irrelevant` - The Securities Regulation Code governs the registration and sale of securities in the Philippines....


---

### Example 24
**Query:** What is 'warranty against eviction' in Philippine contracts of sale?

**Top-1 Match:**
> Contract law provides protections for purchasers against hidden defects in title.

**Top-1 Label:** `conceptual` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `conceptual` - Contract law provides protections for purchasers against hidden defects in title....
2. ✅ `paraphrase` - In sales contracts, sellers guarantee that buyers will not face legal troubles from other parties cl...
3. ✅ `exact` - Warranty against eviction is the seller's obligation to protect the buyer against legal claims of th...


---

### Example 25
**Query:** What is the 'Anti-Fencing Law' (PD 1612) in the Philippines?

**Top-1 Match:**
> The Commission on Human Rights investigates violations of civil liberties.

**Top-1 Label:** `irrelevant` | **Relevant:** `False`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` - The Commission on Human Rights investigates violations of civil liberties....
2. ✅ `paraphrase` - PD 1612 criminalizes the buying and selling of stolen goods to discourage theft by eliminating marke...
3. ✅ `exact` - The Anti-Fencing Law penalizes the act of buying, selling, receiving, possessing, or in any manner d...

⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.


---

### Example 26
**Query:** What is the principle of 'state immunity from suit' in the Philippines?

**Top-1 Match:**
> The Public Attorney’s Office provides legal aid to indigent litigants.

**Top-1 Label:** `irrelevant` | **Relevant:** `False`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` - The Public Attorney’s Office provides legal aid to indigent litigants....
2. ✅ `exact` - State immunity from suit is the principle that the State cannot be sued without its consent, based o...
3. ✅ `paraphrase` - The Philippine government is generally protected from lawsuits unless it expressly allows itself to...

⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.


---

### Example 27
**Query:** What is the 'Blue Sky Law' in Philippine securities regulation?

**Top-1 Match:**
> The Blue Sky Law refers to the Securities Regulation Code that requires registration and disclosure of securities offerings to protect investors from fraudulent investments.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - The Blue Sky Law refers to the Securities Regulation Code that requires registration and disclosure...
2. ❌ `irrelevant` - The Philippine Stock Exchange is the country's primary securities trading market....
3. ✅ `paraphrase` - Philippine securities laws prevent the selling of speculative or fraudulent investments by requiring...


---

### Example 28
**Query:** What is 'land reform' in Philippine agrarian law?

**Top-1 Match:**
> Agriculture is a major sector in the Philippine economy.

**Top-1 Label:** `irrelevant` | **Relevant:** `False`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` - Agriculture is a major sector in the Philippine economy....
2. ✅ `conceptual` - Rural development policies address historical inequities in land ownership and access....
3. ✅ `paraphrase` - Philippine land reform programs aim to break up large landholdings and distribute them to farmers wh...

⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.


---

### Example 29
**Query:** What is the 'Omnibus Election Code' in the Philippines?

**Top-1 Match:**
> The Omnibus Election Code is the comprehensive law governing the conduct of elections in the Philippines, including voter registration, candidacy requirements, campaign regulations, and election offenses.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - The Omnibus Election Code is the comprehensive law governing the conduct of elections in the Philipp...
2. ❌ `irrelevant` - The Philippine electoral system uses automated counting machines....
3. ❌ `irrelevant` - The Philippine Constitution provides for a bicameral legislature composed of the Senate and House of...


---

### Example 30
**Query:** What is the concept of 'piercing the veil of corporate fiction' in Philippine corporation law?

**Top-1 Match:**
> Piercing the veil of corporate fiction is a doctrine that disregards the separate legal personality of a corporation when it is used to defeat public convenience, justify wrong, protect fraud, or defend crime.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - Piercing the veil of corporate fiction is a doctrine that disregards the separate legal personality...
2. ❌ `irrelevant` - Partnerships and cooperatives also have distinct legal personalities in Philippine law....
3. ✅ `conceptual` - Legal doctrines prevent the abuse of corporate structures to evade liability or perpetrate injustice...


---

### Example 31
**Query:** What is the Anti-Carnapping Act of 1972 (RA 6539)?

**Top-1 Match:**
> RA 6539 criminalizes the unlawful taking of motor vehicles, with graduated penalties depending on circumstances and resulting harm.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - RA 6539 criminalizes the unlawful taking of motor vehicles, with graduated penalties depending on ci...
2. ✅ `exact` - The Anti-Carnapping Act defines and penalizes the theft of motor vehicles, imposing heavier penaltie...
3. ❌ `irrelevant` - Traffic rules are enforced by the Metropolitan Manila Development Authority....


---

### Example 32
**Query:** What is the 'Revised Corporation Code' (RA 11232) of the Philippines?

**Top-1 Match:**
> RA 11232 updated the Corporation Code to improve ease of doing business and align with global corporate governance standards.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - RA 11232 updated the Corporation Code to improve ease of doing business and align with global corpor...
2. ✅ `exact` - The Revised Corporation Code modernizes Philippine corporate law by allowing one-person corporations...
3. ✅ `conceptual` - Corporate laws evolve to accommodate changing business environments and technological advancements....


---

### Example 33
**Query:** What is the concept of 'public domain' in Philippine property law?

**Top-1 Match:**
> In Philippine law, public domain properties belong to the government and generally cannot be privately owned or sold.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - In Philippine law, public domain properties belong to the government and generally cannot be private...
2. ❌ `irrelevant` - Private lands can be registered under the Torrens system....
3. ❌ `irrelevant` - The Department of Agriculture promotes productivity in rural farming communities....


---

### Example 34
**Query:** What is the 'Solo Parents' Welfare Act' (RA 8972) in the Philippines?

**Top-1 Match:**
> RA 8972 establishes social protection and assistance for single mothers and fathers facing the challenges of raising children alone.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - RA 8972 establishes social protection and assistance for single mothers and fathers facing the chall...
2. ✅ `exact` - The Solo Parents' Welfare Act provides comprehensive support programs and benefits for single parent...
3. ✅ `conceptual` - Social legislation addresses the needs of vulnerable family structures and promotes child welfare....


---

### Example 35
**Query:** What is the purpose of the Writ of Amparo in the Philippines?

**Top-1 Match:**
> In the Philippines, the Writ of Amparo serves as a safeguard for individuals facing threats to their fundamental rights, especially in situations involving state agents.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - In the Philippines, the Writ of Amparo serves as a safeguard for individuals facing threats to their...
2. ✅ `exact` - The Writ of Amparo is a legal remedy designed to protect individuals from threats to their life, lib...
3. ❌ `irrelevant` - The Writ of Habeas Corpus is a legal action that requires a person under arrest to be brought before...


---

### Example 36
**Query:** Define 'force majeure' under Philippine law.

**Top-1 Match:**
> Unforeseen events like typhoons or earthquakes that hinder contract performance are considered force majeure in Philippine jurisprudence.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - Unforeseen events like typhoons or earthquakes that hinder contract performance are considered force...
2. ✅ `exact` - Force majeure refers to events beyond the control of parties, such as natural disasters, which preve...
3. ❌ `irrelevant` - Breach of contract occurs when one party fails to fulfill their obligations....


---

### Example 37
**Query:** What rights are protected under the Indigenous Peoples' Rights Act (IPRA)?

**Top-1 Match:**
> Under IPRA, indigenous peoples are granted rights to their ancestral lands and the preservation of their cultural practices.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - Under IPRA, indigenous peoples are granted rights to their ancestral lands and the preservation of t...
2. ✅ `exact` - The IPRA protects the rights of Indigenous Cultural Communities/Indigenous Peoples to their ancestra...
3. ✅ `conceptual` - Laws exist to ensure the protection and promotion of indigenous communities' heritage and traditions...


---

### Example 38
**Query:** What is the principle of 'parens patriae' in Philippine law?

**Top-1 Match:**
> The state has the authority to protect individuals who cannot protect themselves under the concept of parens patriae.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - The state has the authority to protect individuals who cannot protect themselves under the concept o...
2. ✅ `exact` - Parens patriae is the doctrine that allows the state to act as guardian for those unable to care for...
3. ❌ `irrelevant` - Local governments are required to allocate funds for disaster preparedness....


---

### Example 39
**Query:** What does 'double jeopardy' mean in the context of criminal law?

**Top-1 Match:**
> The legal system includes protections against repeated prosecution.

**Top-1 Label:** `conceptual` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `conceptual` - The legal system includes protections against repeated prosecution....
2. ❌ `irrelevant` - Criminal cases involve the state prosecuting a person for an alleged offense....
3. ❌ `irrelevant` - The barangay justice system handles disputes at the community level....


---

### Example 40
**Query:** What is the role of the Sandiganbayan in the Philippine judiciary?

**Top-1 Match:**
> The Sandiganbayan is a special court in the Philippines that hears cases involving graft and corruption by public officials.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - The Sandiganbayan is a special court in the Philippines that hears cases involving graft and corrupt...
2. ✅ `paraphrase` - Cases involving corruption and misuse of government funds by public officials are handled by the San...
3. ❌ `irrelevant` - The Supreme Court is the highest judicial body in the country....


---

### Example 41
**Query:** What is the doctrine of exhaustion of administrative remedies?

**Top-1 Match:**
> The doctrine of exhaustion of administrative remedies requires a party to seek relief from administrative bodies before going to court.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - The doctrine of exhaustion of administrative remedies requires a party to seek relief from administr...
2. ✅ `conceptual` - Administrative bodies are empowered to resolve disputes within their specialized jurisdictions....
3. ❌ `irrelevant` - A court can review the decisions of government agencies....


---

### Example 42
**Query:** Define 'agrarian reform' in the Philippine context.

**Top-1 Match:**
> In the Philippines, agrarian reform is a government initiative to transfer land ownership from landlords to tenants and farmers.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - In the Philippines, agrarian reform is a government initiative to transfer land ownership from landl...
2. ❌ `irrelevant` - Farming is a primary source of livelihood in rural areas....
3. ✅ `exact` - Agrarian reform refers to the redistribution of agricultural land to farmers and farmworkers, aiming...


---

### Example 43
**Query:** What is the Anti-Violence Against Women and Their Children Act (RA 9262)?

**Top-1 Match:**
> RA 9262 is a Philippine law that defines and penalizes violence against women and their children, including physical, psychological, and economic abuse.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - RA 9262 is a Philippine law that defines and penalizes violence against women and their children, in...
2. ✅ `paraphrase` - The Anti-VAWC Act protects women and children from various forms of abuse committed by partners or f...
3. ❌ `irrelevant` - The Child and Youth Welfare Code protects the rights of minors....


---

### Example 44
**Query:** What is the purpose of the Katarungang Pambarangay system?

**Top-1 Match:**
> The Katarungang Pambarangay system is a local justice system that aims to amicably settle disputes at the barangay level before they escalate to formal courts.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - The Katarungang Pambarangay system is a local justice system that aims to amicably settle disputes a...
2. ✅ `paraphrase` - Barangay justice promotes community-based resolution of disputes through conciliation and mediation....
3. ❌ `irrelevant` - The Commission on Elections supervises the conduct of elections....


---

### Example 45
**Query:** What is the doctrine of primary jurisdiction in administrative law?

**Top-1 Match:**
> The doctrine of primary jurisdiction holds that courts should defer to administrative agencies when a case requires the agency’s specialized expertise.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - The doctrine of primary jurisdiction holds that courts should defer to administrative agencies when...
2. ❌ `irrelevant` - Administrative agencies are part of the executive branch....
3. ❌ `irrelevant` - The Commission on Audit reviews government expenditures for legality and propriety....


---

### Example 46
**Query:** Explain the concept of 'just compensation' in expropriation cases.

**Top-1 Match:**
> In expropriation, property owners must be paid fairly for the land acquired by the government.

**Top-1 Label:** `paraphrase` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `paraphrase` - In expropriation, property owners must be paid fairly for the land acquired by the government....
2. ✅ `exact` - Just compensation refers to the fair value of property taken by the government for public use, ensur...
3. ✅ `conceptual` - Constitutional rights protect property owners from unjust land seizures....


---

### Example 47
**Query:** What is the Anti-Terrorism Act of 2020 (RA 11479)?

**Top-1 Match:**
> RA 11479 is a law enacted to strengthen the Philippines' legal framework against terrorism, including provisions for extended detention and surveillance.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - RA 11479 is a law enacted to strengthen the Philippines' legal framework against terrorism, includin...
2. ✅ `paraphrase` - The Anti-Terrorism Act allows law enforcers to arrest and monitor individuals suspected of terrorist...
3. ✅ `conceptual` - National security laws grant the government broader powers to combat terrorism....


---

### Example 48
**Query:** What is the legal implication of 'informed consent' in medical treatment?

**Top-1 Match:**
> Informed consent means a patient agrees to a medical procedure after understanding its risks, benefits, and alternatives.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - Informed consent means a patient agrees to a medical procedure after understanding its risks, benefi...
2. ✅ `conceptual` - Medical ethics require transparency and voluntary participation in procedures....
3. ✅ `paraphrase` - Doctors must ensure that patients voluntarily agree to treatment based on sufficient information....


---

### Example 49
**Query:** What is the role of the Civil Service Commission (CSC)?

**Top-1 Match:**
> The Civil Service Commission oversees the integrity and efficiency of the civil service and ensures merit-based appointments in government.

**Top-1 Label:** `exact` | **Relevant:** `True`

✅ **Top-1 retrieval correct.**

**Top-3 Retrieved Passages:**
1. ✅ `exact` - The Civil Service Commission oversees the integrity and efficiency of the civil service and ensures...
2. ✅ `paraphrase` - CSC is responsible for ensuring fair hiring and disciplinary standards for government employees....
3. ❌ `irrelevant` - The Department of Health handles national health policies....


---

### Example 50
**Query:** What is the 'Comprehensive Dangerous Drugs Act' (RA 9165) of the Philippines?

**Top-1 Match:**
> The Philippine Drug Enforcement Agency is the lead agency in anti-drug operations.

**Top-1 Label:** `irrelevant` | **Relevant:** `False`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` - The Philippine Drug Enforcement Agency is the lead agency in anti-drug operations....
2. ✅ `exact` - The Comprehensive Dangerous Drugs Act criminalizes the importation, sale, possession, and use of ill...
3. ❌ `irrelevant` - The Land Transportation Office issues driver’s licenses and vehicle registrations....


---

