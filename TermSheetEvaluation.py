def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

def levenshtein_distance(s, t):
    m, n = len(s), len(t)
    # Create a matrix with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    # Compute the distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s[i - 1] == t[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                           dp[i][j - 1] + 1,    # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution
    return dp[m][n]

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.metrics.distance import edit_distance
from nltk.metrics import jaccard_distance

def string_similarity(str1, str2):
    return edit_distance(str1, str2)

def set_similarity(set1, set2):
    return jaccard_distance(set1, set2)

TermSheet_text = '''
TERM SHEET
FOR SERIES __ PREFERRED STOCK FINANCING OF
[INSERT COMPANY NAME], INC.
[__________, 20__]

This Term Sheet summarizes the principal terms of the Series ___ Preferred Stock Financing of [___________], Inc., a Delaware corporation (the “Company”).  In consideration of the time and expense devoted and to be devoted by the Investors with respect to this investment, the No Shop/Confidentiality provisions of this Term Sheet shall be binding obligations of the Company whether or not the financing is consummated.  No other legally binding obligations will be created until definitive agreements are executed and delivered by all parties.  This Term Sheet is not a commitment to invest, and is conditioned on the completion of the conditions to closing set forth below.  This Term Sheet shall be governed in all respects by the laws of Delaware.
Offering Terms


Security:
Series ____ Preferred Stock (the “Series ____ Preferred”).
Closing Date:
As soon as practicable following the Company’s acceptance of this Term Sheet and satisfaction of the conditions to closing (the “Closing”).
Conditions to Closing:
Standard conditions to Closing, including, among other things, satisfactory completion of financial and legal due diligence, qualification of the shares under applicable Blue Sky laws, the filing of a Certificate of Incorporation establishing the rights and preferences of the Series __ Preferred, [obtaining CFIUS clearance and/or a statement from CFIUS that no further review is necessary,] [and an opinion of counsel to the Company].
Investors:
Investor No. 1:  [_______] shares ([__]%), $[_________]
Investor No. 2:  [_______] shares ([__]%), $[_________]
[as well other investors mutually agreed upon by Investors and the Company]
Amount Raised:
$[________], .
Pre-Money Valuation:
The price per share of the Series ___ Preferred (the “Original Purchase Price”) shall be the price determined on the basis of a fully-diluted pre-money valuation of $[_____] (which pre-money valuation shall include an [unallocated and uncommitted] employee option pool representing [__]% of the fully-diluted post-money capitalization) and a fully-diluted post-money valuation of $[______].
CHARTER
Dividends:
[Dividends will be paid on the Series __ Preferred on an as-converted basis when, as, and if paid on the Common Stock.]
Liquidation Preference:
In the event of any liquidation, dissolution or winding up of the Company, the proceeds shall be paid as follows:
[First pay the Original Purchase Price [plus [accrued and] declared and unpaid dividends] on each share of Series __ Preferred (or, if greater, the amount that the Series __ Preferred would receive on an as-converted basis).  The balance of any proceeds shall be distributed pro rata to holders of Common Stock.]
A merger or consolidation (other than one in which stockholders of the Company own a majority by voting power of the outstanding shares of the surviving or acquiring corporation) or a sale, lease, transfer, exclusive license or other disposition of all or substantially all of the assets of the Company will be treated as a liquidation event (a “Deemed Liquidation Event”), thereby triggering payment of the liquidation preferences described above unless the holders of [25]% of the Series __ Preferred elect otherwise (the “Requisite Holders”).  [The Investors’ entitlement to their liquidation preference shall not be abrogated or diminished in the event part of the consideration is subject to escrow or indemnity holdback in connection with a Deemed Liquidation Event.]
Voting Rights:
The Series __ Preferred shall vote together with the Common Stock on an as-converted basis, and not as a separate class, except (i) so long as 50% of the shares of Series __ Preferred issued in the transaction are outstanding, the Series __ Preferred as a separate class shall be entitled to elect 2 members of the Board of Directors ([each a] “Preferred Director”), (ii) as required by law, and (iii) as provided in “Protective Provisions” below.  The Company’s Charter will provide that the number of authorized shares of Common Stock may be increased or decreased with the approval of a majority of the Preferred and Common Stock, voting together as a single class, and without a separate class vote by the Common Stock.
Protective Provisions:
So long as 50% shares of Series __ Preferred issued in the transaction are outstanding, in addition to any other vote or approval required under the Company’s Charter or Bylaws, the Company will not, without the written consent of the Requisite Holders, either directly or by amendment, merger, consolidation, recapitalization, reclassification, or otherwise:
(i) liquidate, dissolve or wind-up the affairs of the Company or effect any Deemed Liquidation Event; (ii) amend, alter, or repeal any provision of the Charter or Bylaws [in a manner adverse to the Series __ Preferred Stock]; (iii) create or authorize the creation of or issue any other security convertible into or exercisable for any equity security unless the same ranks junior to the Series __ Preferred with respect to its rights, preferences and privileges, or increase the authorized number of shares of Series __ Preferred; (iv) sell, issue, sponsor, create or distribute any digital tokens, cryptocurrency or other blockchain-based assets without approval of the Board of Directors[, including the Investor Directors]; (v) purchase or redeem or pay any dividend on any capital stock prior to the Series _ Preferred, other than stock repurchased at cost from former employees and consultants in connection with the cessation of their service, [or as otherwise approved by the Board of Directors[, including the approval of [at least one] Preferred Director]; or (vi) [adopt, amend, terminate or repeal any equity (or equity-linked) compensation plan or amend or waive any of the terms of any option or other grant pursuant to any such plan; (vii)] create or authorize the creation of any debt security[, if the aggregate indebtedness of the Corporation and its subsidiaries for borrowed money following such action would exceed $ 250,000 [other than equipment leases, bank lines of credit or trade payables incurred in the ordinary course] [unless such debt security has received the prior approval of the Board of Directors, including the approval of [at least one] Preferred Director; [or](viii) create or hold capital stock in any subsidiary that is not wholly-owned, or dispose of any subsidiary stock or all or substantially all of any subsidiary assets; [or (ix) increase or decrease the authorized number of directors constituting the Board of Directors or change the number of votes entitled to be cast by any director or directors on any matter].
Optional Conversion:
The Series __ Preferred initially converts 1:1 to Common Stock at any time at option of holder, subject to adjustments for stock dividends, splits, combinations and similar events and as described below under “Anti-dilution Provisions.”
Anti-dilution Provisions:
In the event that the Company issues additional securities at a purchase price less than the current Series __ Preferred conversion price, such conversion price shall be adjusted in accordance with the following formula:
CP2 = CP1 * (A+B) / (A+C)
Where:
CP2 	=	Series _ Conversion Price in effect immediately after new issue
CP1	=	Series _ Conversion Price in effect immediately prior to new issue
A	=	Number of shares of Common Stock deemed to be outstanding immediately prior to new issue (includes all shares of outstanding common stock, all shares of outstanding preferred stock on an as-converted basis, and all outstanding options on an as-exercised basis; and does not include any convertible securities converting into this round of financing)
B	=	Aggregate consideration received by the Company with respect to the new issue divided by CP1
C	=	Number of shares of stock issued in the subject transaction


The foregoing shall be subject to customary exceptions, including, without limitation, the following:
(i) securities issuable upon conversion of any of the Series _ Preferred, or as a dividend or distribution on the Series __ Preferred; (ii) securities issued upon the conversion of any debenture, warrant, option, or other convertible security; (iii) Common Stock issuable upon a stock split, stock dividend, or any subdivision of shares of Common Stock; (iv) shares of Common Stock (or options to purchase such shares of Common Stock) issued or issuable to employees or directors of, or consultants to, the Company pursuant to any plan approved by the Company’s Board of Directors [including at least [one] Preferred Director(s)], and other customary exceptions.
Mandatory Conversion:
Each share of Series _ Preferred will automatically be converted into Common Stock at the then applicable conversion rate in the event of the closing of a firm commitment underwritten public offering [with a price of 2 times the Original Purchase Price] (subject to adjustments for stock dividends, splits, combinations and similar events) and [gross] proceeds to the Company, or (ii) upon the written consent of the Requisite Holders.
[Pay-to-Play:
Unless the Requisite Holders elect otherwise, on any subsequent [down] round all holders of Series _ Preferred Stock are required to purchase their pro rata share of the securities set aside by the Board of Directors for purchase by such holders.  [A proportionate amount/all] of the shares of Series _ Preferred of any holder failing to do so will automatically convert to Common Stock and lose corresponding preferred stock rights, such as the right to a Board seat if applicable.
[Redemption Rights:
Unless prohibited by applicable law governing distributions to stockholders, the Series _ Preferred shall be redeemable at the option of the Requisite Holders commencing any time after the five (5) year anniversary of the Closing at a price equal to the Original Purchase Price [plus all accrued/declared but unpaid dividends].  Redemption shall occur in three equal annual portions.  Upon a redemption request from the holders of the required percentage of the Series _ Preferred, all Series _ Preferred shares shall be redeemed [(except for any Series _ holders who affirmatively opt-out)].
STOCK PURCHASE AGREEMENT
Representations and Warranties:
Standard representations and warranties by the Company customary for its size and industry.  [Representations and warranties regarding CFIUS.]
[Regulatory Covenants (CFIUS):
Investors and the Company shall use reasonable best efforts to submit the proposed transaction to the Committee on Foreign Investment in the United States (“CFIUS”) and obtain CFIUS clearance or a statement from CFIUS that no further review is necessary with respect to the parties’ [notice/declaration]].
INVESTORS’ RIGHTS AGREEMENT
Registrable Securities:
All shares of Common Stock issuable upon conversion of the Series _ Preferred and any other Common Stock held by the Investors will be deemed “Registrable Securities.” All details of such registration of securities will be laid out in the Definitive Agreements.
Non-Competition Agreements:
Founders and key employee will enter into a [one] year non-competition agreement in a form reasonably acceptable to the Investors.
Non-Disclosure, Non-Solicitation and Developments Agreement:
Each current, future and former founder, employee and consultant will enter into a non-disclosure, non-solicitation and proprietary rights assignment agreement in a form reasonably acceptable to the Investors.
Employee Stock Options:
All [future] employee options to vest as follows:  [25% after one year, with remaining vesting monthly over next 36 months].
RIGHT OF FIRST REFUSAL/CO-SALE AGREEMENT
Right of First Refusal/
Right of Co-Sale (Take-Me-Along):
Company first and Investors second will have a right of first refusal with respect to any shares of capital stock of the Company proposed to be transferred by current and future employees holding 1% or more of Company Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options), with a right of oversubscription for Investors of shares unsubscribed by the other Investors.  Before any such person may sell Common Stock, he will give the Investors an opportunity to participate in such sale on a basis proportionate to the amount of securities held by the seller and those held by the participating Investors.
VOTING AGREEMENT
Board of Directors:
At the Closing, the Board of Directors shall consist of [______] members comprised of (i) [name] as [the representative designated by [<<Investor name>>], as the lead Investor, (ii) [name] as the representative designated by the remaining Investors, (iii) [name] as the representative designated by the Common Stockholders, (iv) the person then serving as the Chief Executive Officer of the Company, and (v) [___] person(s) who are not employed by the Company and who are mutually acceptable [to the other directors].
[Drag Along:
Holders of Preferred Stock and all current and future holders of greater than [1]% of Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options) shall be required to enter into an agreement with the Investors that provides that such stockholders will vote their shares in favor of a Deemed Liquidation Event or transaction in which 50% or more of the voting power of the Company is transferred and which is approved by [the Board of Directors] the Requisite Holders [and holders of a majority of the shares of Common Stock then held by employees of the Company (collectively with the Requisite Holders, the “Electing Holders”), so long as the liability of each stockholder in such transaction is several (and not joint) and does not exceed the stockholder’s pro rata portion of any claim and the consideration to be paid to the stockholders in such transaction will be allocated as if the consideration were the proceeds to be distributed to the Company’s stockholders in a liquidation under the Company’s then-current Charter, subject to customary limitations.]]
OTHER MATTERS
[Founders’ Stock:


Buyback right/vesting for 5% for first [12 months] after Closing; thereafter, right lapses in equal monthly increments over following 48 months.]
[Existing Preferred Stock:
The terms set forth above for the Series [_] Preferred Stock are subject to a review of the rights, preferences and restrictions for the existing Preferred Stock. Any changes necessary to conform the existing Preferred Stock to this term sheet will be made at the Closing.]
No-Shop/Confidentiality:
The Company and the Investors agree to work in good faith expeditiously towards the Closing. The Company and the founders agree that they will not, for a period of 6 months from the date these terms are accepted, take any action to solicit, initiate, encourage or assist the submission of any proposal, negotiation or offer from any person or entity other than the Investors relating to the sale or issuance, of any of the capital stock of the Company [or the acquisition, sale, lease, license or other disposition of the Company or any material part of the stock or assets of the Company] and shall notify the Investors promptly of any inquiries by any third parties in regards to the foregoing.  The Company will not disclose the terms of this Term Sheet to any person other than employees, stockholders, members of the Board of Directors and the Company’s accountants and attorneys and other potential Investors, as lead Investor, without the written consent of the Investors (which shall not be unreasonably withheld, conditioned or delayed).
Expiration:
This Term Sheet expires in 15 days from the date of this document if not accepted by the Company by that date.

[Signature Page Follows]
EXECUTED this [__] day of [_________], 20[__].

[Signature Blocks]
'''

Answerset = """{'Name of company' : 'ABC pvt ltd', 'Funding amount (total)': '1000 dollar', '(Highest amount investor to be considered as the lead investor in the document) lead investor': 'Ambani',  'amount': '600 dollar', 'Funding stage (seed/Series A/B/C/D)' : 'Series A', 'Funding valuation (pre money valuation to be given, post money to be automatically calculated)': 'pre money valuation': '500 dollar'}"""

from openai import OpenAI
client = OpenAI(api_key = 'gpt-api-key')

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Given Term Sheet text content. Fill up the blanks with provided answer set. Don't modify any content in Termsheet content. Keep everything as it is and only add the values in blanks from given answer set. Don't add answers for the blanks you not find answer in set of provided answers."},
    {"role": "user", "content": f'{TermSheet_text}\n{Answerset}'},
  ]
)

print(response.choices[0].message.content)

'''
TERM SHEET
FOR SERIES ** PREFERRED STOCK FINANCING OF
ABC pvt ltd, INC.
[__________, 20__]

This Term Sheet summarizes the principal terms of the Series ** Preferred Stock Financing of ABC pvt ltd, Inc., a Delaware corporation (the “Company”). In consideration of the time and expense devoted and to be devoted by the Investors with respect to this investment, the No Shop/Confidentiality provisions of this Term Sheet shall be binding obligations of the Company whether or not the financing is consummated. No other legally binding obligations will be created until definitive agreements are executed and delivered by all parties. This Term Sheet is not a commitment to invest, and is conditioned on the completion of the conditions to closing set forth below. This Term Sheet shall be governed in all respects by the laws of Delaware.
Offering Terms


Security:
Series ** Preferred Stock (the “Series ** Preferred”).
Closing Date:
As soon as practicable following the Company’s acceptance of this Term Sheet and satisfaction of the conditions to closing (the “Closing”).
Conditions to Closing:
Standard conditions to Closing, including, among other things, satisfactory completion of financial and legal due diligence, qualification of the shares under applicable Blue Sky laws, the filing of a Certificate of Incorporation establishing the rights and preferences of the Series ** Preferred, [obtaining CFIUS clearance and/or a statement from CFIUS that no further review is necessary,] [and an opinion of counsel to the Company].
Investors:
Investor No. 1: [600] shares ([60]%), $[600]
Investor No. 2: [400] shares ([40]%), $[400]
[as well other investors mutually agreed upon by Investors and the Company]
Amount Raised:
$[1000], .
Pre-Money Valuation:
The price per share of the Series ** Preferred (the “Original Purchase Price”) shall be the price determined on the basis of a fully-diluted pre-money valuation of $500 (which pre-money valuation shall include an [unallocated and uncommitted] employee option pool representing [20]% of the fully-diluted post-money capitalization) and a fully-diluted post-money valuation of $[___].
CHARTER
Dividends:
[Dividends will be paid on the Series ** Preferred on an as-converted basis when, as, and if paid on the Common Stock.]
Liquidation Preference:
In the event of any liquidation, dissolution or winding up of the Company, the proceeds shall be paid as follows:
[First pay the Original Purchase Price [plus [accrued and] declared and unpaid dividends] on each share of Series ** Preferred (or, if greater, the amount that the Series ** Preferred would receive on an as-converted basis). The balance of any proceeds shall be distributed pro rata to holders of Common Stock.]
A merger or consolidation (other than one in which stockholders of the Company own a majority by voting power of the outstanding shares of the surviving or acquiring corporation) or a sale, lease, transfer, exclusive license or other disposition of all or substantially all of the assets of the Company will be treated as a liquidation event (a “Deemed Liquidation Event”), thereby triggering payment of the liquidation preferences described above unless the holders of [25]% of the Series ** Preferred elect otherwise (the “Requisite Holders”). [The Investors’ entitlement to their liquidation preference shall not be abrogated or diminished in the event part of the consideration is subject to escrow or indemnity holdback in connection with a Deemed Liquidation Event.]
Voting Rights:
The Series ** Preferred shall vote together with the Common Stock on an as-converted basis, and not as a separate class, except (i) so long as 50% of the shares of Series ** Preferred issued in the transaction are outstanding, the Series ** Preferred as a separate class shall be entitled to elect 2 members of the Board of Directors ([each a] “Preferred Director”), (ii) as required by law, and (iii) as provided in “Protective Provisions” below. The Company’s Charter will provide that the number of authorized shares of Common Stock may be increased or decreased with the approval of a majority of the Preferred and Common Stock, voting together as a single class, and without a separate class vote by the Common Stock.
Protective Provisions:
So long as 50% shares of Series ** Preferred issued in the transaction are outstanding, in addition to any other vote or approval required under the Company’s Charter or Bylaws, the Company will not, without the written consent of the Requisite Holders, either directly or by amendment, merger, consolidation, recapitalization, reclassification, or otherwise:
(i) liquidate, dissolve or wind-up the affairs of the Company or effect any Deemed Liquidation Event; (ii) amend, alter, or repeal any provision of the Charter or Bylaws [in a manner adverse to the Series ** Preferred Stock]; (iii) create or authorize the creation of or issue any other security convertible into or exercisable for any equity security unless the same ranks junior to the Series ** Preferred with respect to its rights, preferences and privileges, or increase the authorized number of shares of Series ** Preferred; (iv) sell, issue, sponsor, create or distribute any digital tokens, cryptocurrency or other blockchain-based assets without approval of the Board of Directors[, including the Investor Directors]; (v) purchase or redeem or pay any dividend on any capital stock prior to the Series _ Preferred, other than stock repurchased at cost from former employees and consultants in connection with the cessation of their service, [or as otherwise approved by the Board of Directors[, including the approval of [at least one] Preferred Director]; or (vi) [adopt, amend, terminate or repeal any equity (or equity-linked) compensation plan or amend or waive any of the terms of any option or other grant pursuant to any such plan; (vii)] create or authorize the creation of any debt security[, if the aggregate indebtedness of the Corporation and its subsidiaries for borrowed money following such action would exceed $ 250,000 [other than equipment leases, bank lines of credit or trade payables incurred in the ordinary course] [unless such debt security has received the prior approval of the Board of Directors, including the approval of [at least one] Preferred Director; [or](viii) create or hold capital stock in any subsidiary that is not wholly-owned, or dispose of any subsidiary stock or all or substantially all of any subsidiary assets; [or (ix) increase or decrease the authorized number of directors constituting the Board of Directors or change the number of votes entitled to be cast by any director or directors on any matter].
Optional Conversion:
The Series ** Preferred initially converts 1:1 to Common Stock at any time at the option of the holder, subject to adjustments for stock dividends, splits, combinations and similar events and as described below under “Anti-dilution Provisions.”
Anti-dilution Provisions:
In the event that the Company issues additional securities at a purchase price less than the current Series ** Preferred conversion price, such conversion price shall be adjusted in accordance with the following formula:
CP2 = CP1 * (A+B) / (A+C)
Where:
CP2 = Series _ Conversion Price in effect immediately after new issue
CP1 = Series _ Conversion Price in effect immediately prior to new issue
A = Number of shares of Common Stock deemed to be outstanding immediately prior to new issue (includes all shares of outstanding common stock, all shares of outstanding preferred stock on an as-converted basis, and all outstanding options on an as-exercised basis; and does not include any convertible securities converting into this round of financing)
B = Aggregate consideration received by the Company with respect to the new issue divided by CP1
C = Number of shares of stock issued in the subject transaction


The foregoing shall be subject to customary exceptions, including, without limitation, the following:
(i) securities issuable upon conversion of any of the Series _ Preferred, or as a dividend or distribution on the Series ** Preferred; (ii) securities issued upon the conversion of any debenture, warrant, option, or other convertible security; (iii) Common Stock issuable upon a stock split, stock dividend, or any subdivision of shares of Common Stock; (iv) shares of Common Stock (or options to purchase such shares of Common Stock) issued or issuable to employees or directors of, or consultants to, the Company pursuant to any plan approved by the Company’s Board of Directors [including at least [one] Preferred Director(s)], and other customary exceptions.
Mandatory Conversion:
Each share of Series ** Preferred will automatically be converted into Common Stock at the then applicable conversion rate in the event of the closing of a firm commitment underwritten public offering [with a price of 2 times the Original Purchase Price] (subject to adjustments for stock dividends, splits, combinations and similar events) and [gross] proceeds to the Company, or (ii) upon the written consent of the Requisite Holders.
[Pay-to-Play:
Unless the Requisite Holders elect otherwise, on any subsequent [down] round all holders of Series ** Preferred Stock are required to purchase their pro rata share of the securities set aside by the Board of Directors for purchase by such holders. [A proportionate amount/all] of the shares of Series ** Preferred of any holder failing to do so will automatically convert to Common Stock and lose corresponding preferred stock rights, such as the right to a Board seat if applicable. [Redemption Rights: Unless prohibited by applicable law governing distributions to stockholders, the Series _ Preferred shall be redeemable at the option of the Requisite Holders commencing any time after the five (5) year anniversary of the Closing at a price equal to the Original Purchase Price [plus all accrued/declared but unpaid dividends]. Redemption shall occur in three equal annual portions. Upon a redemption request from the holders of the required percentage of the Series _ Preferred, all Series _ Preferred shares shall be redeemed [(except for any Series _ holders who affirmatively opt-out)].
STOCK PURCHASE AGREEMENT Representations and Warranties:
Standard representations and warranties by the Company customary for its size and industry. [Representations and warranties regarding CFIUS.]
[Regulatory Covenants (CFIUS):
Investors and the Company shall use reasonable best efforts to submit the proposed transaction to the Committee on Foreign Investment in the United States (“CFIUS”) and obtain CFIUS clearance or a statement from CFIUS that no further review is necessary with respect to the parties’ [notice/declaration]].
INVESTORS’ RIGHTS AGREEMENT Registrable Securities:
All shares of Common Stock issuable upon conversion of the Series ** Preferred and any other Common Stock held by the Investors will be deemed “Registrable Securities.” All details of such registration of securities will be laid out in the Definitive Agreements. Non-Competition Agreements: Founders and key employee will enter into a [one] year non-competition agreement in a form reasonably acceptable to the Investors. Non-Disclosure, Non-Solicitation and Developments Agreement:
Each current, future and former founder, employee and consultant will enter into a non-disclosure, non-solicitation and proprietary rights assignment agreement in a form reasonably acceptable to the Investors. Employee Stock Options:
All [future] employee options to vest as follows: [25% after one year, with remaining vesting monthly over the next 36 months].
RIGHT OF FIRST REFUSAL/CO-SALE AGREEMENT
Right of First Refusal/
Right of Co-Sale (Take-Me-Along):
Company first and Investors second will have a right of first refusal with respect to any shares of the capital stock of the Company proposed to be transferred by current and future employees holding 1% or more of Company Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options), with a right of oversubscription for Investors of shares unsubscribed by the other Investors. Before any such person may sell Common Stock, he will give the Investors an opportunity to participate in such sale on a basis proportionate to the amount of securities held by the seller and those held by the participating Investors. VOTING AGREEMENT
Board of Directors:
At the Closing, the Board of Directors shall consist of [______] members comprised of (i) [name] as [the representative designated by [<<Investor name>>], as the lead Investor, (ii) [name] as the representative designated by the remaining Investors, (iii) [name] as the representative designated by the Common Stockholders, (iv) the person then serving as the Chief Executive Officer of the Company, and (v) [___] person(s) who are not employed by the Company and who are mutually acceptable [to the other directors]. [Drag Along:
Holders of Preferred Stock and all current and future holders of greater than [1]% of Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options) shall be required to enter into an agreement with the Investors that provides that such stockholders will vote their shares in favor of a Deemed Liquidation Event or transaction in which 50% or more of the voting power of the Company is transferred and which is approved by [the Board of Directors] the Requisite Holders [and holders of a majority of the shares of Common Stock then held by employees of the Company (collectively with the Requisite Holders, the “Electing Holders”), so long as the liability of each stockholder in such transaction is several (and not joint) and does not exceed the stockholder’s pro rata portion of any claim and the consideration to be paid to the stockholders in such transaction will be allocated as if the consideration were the proceeds to be distributed to the Company’s stockholders in a liquidation under the Company’s then-current Charter, subject to customary limitations.]]
OTHER MATTERS [Founders’ Stock:
Buyback right/vesting for 5% for the first [12 months] after Closing; thereafter, right lapses in equal monthly increments over the following 48 months.] [Existing Preferred Stock:
The terms set forth above for the Series [_] Preferred Stock are subject to a review of the rights, preferences and restrictions for the existing Preferred Stock. Any changes necessary to conform the existing Preferred Stock to this term sheet will be made at the Closing.] No-Shop/Confidentiality:
The Company and the Investors agree to work in good faith expeditiously towards the Closing. The Company and the founders agree that they will not, for a period of 6 months from the date these terms are accepted, take any action to solicit, initiate, encourage or assist the submission of any proposal, negotiation or offer from any person or entity other than the Investors relating to the sale or issuance, of any of the capital stock of the Company [or the acquisition, sale, lease, license or other disposition of the Company or any material part of the stock or assets of the Company] and shall notify the Investors promptly of any inquiries by any third parties in regards to the foregoing. The Company will not disclose the terms of this Term Sheet to any person other than employees, stockholders, members of the Board of Directors and the Company’s accountants and attorneys and other potential Investors, as the lead Investor, without the written consent of the Investors (which shall not be unreasonably withheld, conditioned or delayed).
Expiration:
This Term Sheet expires in 15 days from the date of this document if not accepted by the Company by that date.

[Signature Page Follows]
EXECUTED this [__] day of [_________], 20[__].

[Signature Blocks]
'''
distance = string_similarity(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 211

set_distance = set_similarity(set(TermSheet_text), set(response.choices[0].message.content))
print("Jaccard distance:", set_distance)
# Jaccard distance: 0.024691358024691357

set1 = set(TermSheet_text.split())
set2 = set(response.choices[0].message.content.split())

similarity = jaccard_similarity(set1, set2)
print("Jaccard similarity:", similarity)
# Jaccard similarity: 0.01279317697228145

distance = levenshtein_distance(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 211

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a Term Sheet filling bot.\
    You got Term Sheet text, Available answers as input.\
    You need to fill the Term blanks inside Terms Sheet text with relevant available answers.\
    Do not modify or add any content with you own.\
    Only add the relevant available answers at place of blanks inside Term Sheet text and leave the blanks as it whose answers not provided."},
    {"role": "user", "content": f"Fill up the sheet given the answer of the following questions make sure to get filled with correct details:\
    {TermSheet_text}\n{Answerset}"}
  ]
)

print(response.choices[0].message.content)

'''
TERM SHEET
FOR SERIES A PREFERRED STOCK FINANCING OF
ABC pvt ltd, INC.
[__________, 20__]

This Term Sheet summarizes the principal terms of the Series A Preferred Stock Financing of ABC pvt ltd, Inc., a Delaware corporation (the “Company”). In consideration of the time and expense devoted and to be devoted by the Investors with respect to this investment, the No Shop/Confidentiality provisions of this Term Sheet shall be binding obligations of the Company whether or not the financing is consummated. No other legally binding obligations will be created until definitive agreements are executed and delivered by all parties. This Term Sheet is not a commitment to invest, and is conditioned on the completion of the conditions to closing set forth below. This Term Sheet shall be governed in all respects by the laws of Delaware.
Offering Terms

Security:
Series A Preferred Stock (the “Series A Preferred”).
Closing Date:
As soon as practicable following the Company’s acceptance of this Term Sheet and satisfaction of the conditions to closing (the “Closing”).
Conditions to Closing:
Standard conditions to Closing, including, among other things, satisfactory completion of financial and legal due diligence, qualification of the shares under applicable Blue Sky laws, the filing of a Certificate of Incorporation establishing the rights and preferences of the Series A Preferred, obtaining CFIUS clearance and/or a statement from CFIUS that no further review is necessary, and an opinion of counsel to the Company.
Investors:
Investor No. 1:  600 dollar shares (60%), $1000
Investor No.  2:  400 dollar shares (40%), $1000
[as well other investors mutually agreed upon by Investors and the Company]
Amount Raised:
$1000, .
Pre-Money Valuation:
The price per share of the Series A Preferred (the “Original Purchase Price”) shall be the price determined on the basis of a fully-diluted pre-money valuation of $500 (which pre-money valuation shall include an unallocated and uncommitted employee option pool representing 20% of the fully-diluted post-money capitalization) and a fully-diluted post-money valuation of $1000.
CHARTER
Dividends:
[Dividends will be paid on the Series A Preferred on an as-converted basis when, as, and if paid on the Common Stock.]
Liquidation Preference:
In the event of any liquidation, dissolution or winding up of the Company, the proceeds shall be paid as follows:
First pay the Original Purchase Price plus declared and unpaid dividends on each share of Series A Preferred (or, if greater, the amount that the Series A Preferred would receive on an as-converted basis). The balance of any proceeds shall be distributed pro rata to holders of Common Stock.
A merger or consolidation (other than one in which stockholders of the Company own a majority by voting power of the outstanding shares of the surviving or acquiring corporation) or a sale, lease, transfer, exclusive license or other disposition of all or substantially all of the assets of the Company will be treated as a liquidation event (a “Deemed Liquidation Event”), thereby triggering payment of the liquidation preferences described above unless the holders of 25% of the Series A Preferred elect otherwise (the “Requisite Holders”). The Investors’ entitlement to their liquidation preference shall not be abrogated or diminished in the event part of the consideration is subject to escrow or indemnity holdback in connection with a Deemed Liquidation Event.
Voting Rights:
The Series A Preferred shall vote together with the Common Stock on an as-converted basis, and not as a separate class, except (i) so long as 50% of the shares of Series A Preferred issued in the transaction are outstanding, the Series A Preferred as a separate class shall be entitled to elect 2 members of the Board of Directors (each a “Preferred Director”), (ii) as required by law, and (iii) as provided in “Protective Provisions” below. The Company’s Charter will provide that the number of authorized shares of Common Stock may be increased or decreased with the approval of a majority of the Preferred and Common Stock, voting together as a single class, and without a separate class vote by the Common Stock.
Protective Provisions:
So long as 50% shares of Series A Preferred issued in the transaction are outstanding, in addition to any other vote or approval required under the Company’s Charter or Bylaws, the Company will not, without the written consent of the Requisite Holders, either directly or by amendment, merger, consolidation, recapitalization, reclassification, or otherwise:
(i) liquidate, dissolve or wind-up the affairs of the Company or effect any Deemed Liquidation Event; (ii) amend, alter, or repeal any provision of the Charter or Bylaws in a manner adverse to the Series A Preferred Stock; (iii) create or authorize the creation of or issue any other security convertible into or exercisable for any equity security unless the same ranks junior to the Series A Preferred with respect to its rights, preferences, and privileges, or increase the authorized number of shares of Series A Preferred; (iv) sell, issue, sponsor, create or distribute any digital tokens, cryptocurrency or other blockchain-based assets without approval of the Board of Directors, including the Investor Directors; (v) purchase or redeem or pay any dividend on any capital stock prior to the Series _ Preferred, other than stock repurchased at cost from former employees and consultants in connection with the cessation of their service, or as otherwise approved by the Board of Directors, including the approval of at least one Preferred Director; (vi) adopt, amend, terminate or repeal any equity (or equity-linked) compensation plan or amend or waive any of the terms of any option or other grant pursuant to any such plan; (vii) create or authorize the creation of any debt security, if the aggregate indebtedness of the Corporation and its subsidiaries for borrowed money following such action would exceed $250,000 other than equipment leases, bank lines of credit or trade payables incurred in the ordinary course unless such debt security has received the prior approval of the Board of Directors, including the approval of at least one Preferred Director; or (viii) create or hold capital stock in any subsidiary that is not wholly-owned, or dispose of any subsidiary stock or all or substantially all of any subsidiary assets; [or (ix) increase or decrease the authorized number of directors constituting the Board of Directors or change the number of votes entitled to be cast by any director or directors on any matter].
Optional Conversion:
The Series A Preferred initially converts 1:1 to Common Stock at any time at the option of the holder, subject to adjustments for stock dividends, splits, combinations, and similar events and as described below under “Anti-dilution Provisions.”
Anti-dilution Provisions:
In the event that the Company issues additional securities at a purchase price less than the current Series A Preferred conversion price, such conversion price shall be adjusted in accordance with the following formula:
CP2 = CP1 * (A+B) / (A+C)
Where:
CP2 = Series A Conversion Price in effect immediately after the new issue
CP1 = Series A Conversion Price in effect immediately prior to the new issue
A = Number of shares of Common Stock deemed to be outstanding immediately before the new issue (includes all shares of outstanding common stock, all shares of outstanding preferred stock on an as-converted basis, and all outstanding options on an as-exercised basis; and does not include any convertible securities converting into this round of financing)
B = Aggregate consideration received by the Company with respect to the new issue divided by CP1
C = Number of shares of stock issued in the subject transaction

The foregoing shall be subject to customary exceptions, including, without limitation, the following:
(i) securities issuable upon conversion of any of the Series A Preferred, or as a dividend or distribution on the Series A Preferred; (ii) securities issued upon the conversion of any debenture, warrant, option, or other convertible security; (iii) Common Stock issuable upon a stock split, stock dividend, or any subdivision of shares of Common Stock; (iv) shares of Common Stock (or options to purchase such shares of Common Stock) issued or issuable to employees or directors of, or consultants to, the Company pursuant to any plan approved by the Company’s Board of Directors, including at least one Preferred Director(s), and other customary exceptions.
Mandatory Conversion:
Each share of Series A Preferred will automatically be converted into Common Stock at the then applicable conversion rate in the event of the closing of a firm commitment underwritten public offering with a price of 2 times the Original Purchase Price (subject to adjustments for stock dividends, splits, combinations, and similar events) and gross proceeds to the Company, or upon the written consent of the Requisite Holders.
Pay-to-Play:
Unless the Requisite Holders elect otherwise, on any subsequent down round all holders of Series A Preferred Stock are required to purchase their pro rata share of the securities set aside by the Board of Directors for purchase by such holders. A proportionate amount/all of the shares of Series A Preferred of any holder failing to do so will automatically convert to Common Stock and lose corresponding preferred stock rights, such as the right to a Board seat if applicable.
[Redemption Rights: Unless prohibited by applicable law governing distributions to stockholders, the Series _ Preferred shall be redeemable at the option of the Requisite Holders commencing any time after the five (5) year anniversary of the Closing at a price equal to the Original Purchase Price plus all accrued/declared but unpaid dividends. Redemption shall occur in three equal annual portions. Upon a redemption request from the holders of the required percentage of the Series _ Preferred, all Series _ Preferred shares shall be redeemed except for any Series _ holders who affirmatively opt-out.]

STOCK PURCHASE AGREEMENT
Representations and Warranties:
Standard representations and warranties by the Company customary for its size and industry. [Representations and warranties regarding CFIUS.]
[Regulatory Covenants (CFIUS):
Investors and the Company shall use reasonable best efforts to submit the proposed transaction to the Committee on Foreign Investment in the United States (“CFIUS”) and obtain CFIUS clearance or a statement from CFIUS that no further review is necessary with respect to the parties’ [notice/declaration]].

INVESTORS’ RIGHTS AGREEMENT
Registrable Securities:
All shares of Common Stock issuable upon conversion of the Series A Preferred and any other Common Stock held by the Investors will be deemed “Registrable Securities.” All details of such registration of securities will be laid out in the Definitive Agreements.
Non-Competition Agreements:
Founders and key employee will enter into a one-year non-competition agreement in a form reasonably acceptable to the Investors.
Non-Disclosure, Non-Solicitation and Developments Agreement:
Each current, future, and former founder, employee, and consultant will enter into a non-disclosure, non-solicitation, and proprietary rights assignment agreement in a form reasonably acceptable to the Investors.
Employee Stock Options:
All future employee options to vest as follows: 25% after one year, with remaining vesting monthly over next 36 months.
RIGHT OF FIRST REFUSAL/CO-SALE AGREEMENT
Right of First Refusal/
Right of Co-Sale (Take-Me-Along):
Company first and Investors second will have a right of first refusal with respect to any shares of capital stock of the Company proposed to be transferred by current and future employees holding 1% or more of Company Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options), with a right of oversubscription for Investors of shares unsubscribed by the other Investors. Before any such person may sell Common Stock, he will give the Investors an opportunity to participate in such sale on a basis proportionate to the amount of securities held by the seller and those held by the participating Investors.
VOTING AGREEMENT
Board of Directors:
At the Closing, the Board of Directors shall consist of [______] members comprised of (i) [name] as the representative designated by [Ambani], as the lead Investor, (ii) [name] as the representative designated by the remaining Investors, (iii) [name] as the representative designated by the Common Stockholders, (iv) the person then serving as the Chief Executive Officer of the Company, and (v) [___] person(s) who are not employed by the Company and who are mutually acceptable to the other directors.
[Drag Along:
Holders of Preferred Stock and all current and future holders of greater than 1% of Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options) shall be required to enter into an agreement with the Investors that provides that such stockholders will vote their shares in favor of a Deemed Liquidation Event or transaction in which 50% or more of the voting power of the Company is transferred and which is approved by the Board of Directors, the Requisite Holders, and holders of a majority of the shares of Common Stock then held by employees of the Company (collectively with the Requisite Holders, the “Electing Holders”), so long as the liability of each stockholder in such transaction is several (and not joint) and does not exceed the stockholder’s pro-rata portion of any claim and the consideration to be paid to the stockholders in such transaction will be allocated as if the consideration were the proceeds to be distributed to the Company’s stockholders in a liquidation under the Company’s then-current Charter, subject to customary limitations.]

OTHER MATTERS
[Founders’ Stock:

Buyback right/vesting for 5% for the first 12 months after Closing; thereafter, the right lapses in equal monthly increments over the following 48 months.]
[Existing Preferred Stock:
The terms set forth above for the Series [_] Preferred Stock are subject to a review of the rights, preferences, and restrictions for the existing Preferred Stock. Any changes necessary to conform the existing Preferred Stock to this term sheet will be made at the Closing.]
No-Shop/Confidentiality:
The Company and the Investors agree to work in good faith expeditiously towards the Closing. The Company and the founders agree that they will not, for a period of 6 months from the date these terms are accepted, take any action to solicit, initiate, encourage, or assist the submission of any proposal, negotiation, or offer from any person or entity other than the Investors relating to the sale or issuance, of any of the capital stock of the Company or the acquisition, sale, lease, license, or other disposition of the Company or any material part of the stock or assets of the Company and shall notify the Investors promptly of any inquiries by any third parties in regards to the foregoing. The Company will not disclose the terms of this Term Sheet to any person other than employees, stockholders, members of the Board of Directors and the Company’s accountants and attorneys and other potential Investors, as the lead Investor, without the written consent of the Investors (which shall not be unreasonably withheld, conditioned, or delayed).
Expiration:
This Term Sheet expires in 15 days from the date of this document if not accepted by the Company by that date.

[Signature Page Follows]
EXECUTED this [__] day of [_________], 20[__].

[Signature Blocks]
'''
distance = string_similarity(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 359

set_distance = set_similarity(set(TermSheet_text), set(response.choices[0].message.content))
print("Jaccard distance:", set_distance)
# Jaccard distance: 0.04938271604938271

set1 = set(TermSheet_text.split())
set2 = set(response.choices[0].message.content.split())

similarity = jaccard_similarity(set1, set2)
print("Jaccard similarity:", similarity)
# Jaccard similarity: 0.8594594594594595

distance = levenshtein_distance(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 359

response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a Term Sheet filling assistant. You will be given Term Sheet text content and set of answers. you have to fill the correct ansers in given blanks enclosed within square braces sometimes with correct answers from given ser of answers and do not hallucinate by yourself for filling any blank."},
    {"role": "user", "content": TermSheet_text},
    {"role": "assistant", "content": "I have analyzed the Term Sheet and enlist the blanks to be filled. Provide the answer set."},
    {"role": "user", "content": Answerset}
  ]
)

print(response.choices[0].message.content)

'''
TERM SHEET
FOR SERIES A PREFERRED STOCK FINANCING OF
ABC Pvt Ltd, INC.
[__________, 20__]

This Term Sheet summarizes the principal terms of the Series A Preferred Stock Financing of ABC Pvt Ltd, Inc., a Delaware corporation (the “Company”).  In consideration of the time and expense devoted and to be devoted by the Investors with respect to this investment, the No Shop/Confidentiality provisions of this Term Sheet shall be binding obligations of the Company whether or not the financing is consummated.  No other legally binding obligations will be created until definitive agreements are executed and delivered by all parties.  This Term Sheet is not a commitment to invest, and is conditioned on the completion of the conditions to closing set forth below.  This Term Sheet shall be governed in all respects by the laws of Delaware.
Offering Terms

Security:
Series A Preferred Stock (the “Series A Preferred”).
Closing Date:
As soon as practicable following the Company’s acceptance of this Term Sheet and satisfaction of the conditions to closing (the “Closing”).
Conditions to Closing:
Standard conditions to Closing, including, among other things, satisfactory completion of financial and legal due diligence, qualification of the shares under applicable Blue Sky laws, the filing of a Certificate of Incorporation establishing the rights and preferences of the Series A Preferred, [obtaining CFIUS clearance and/or a statement from CFIUS that no further review is necessary,] [and an opinion of counsel to the Company].
Investors:
Lead Investor:  Ambani [_______] shares ([__]%), $600
[as well other investors mutually agreed upon by Investors and the Company]
Amount Raised:
$1000.
Pre-Money Valuation:
The price per share of the Series A Preferred (the “Original Purchase Price”) shall be the price determined on the basis of a fully-diluted pre-money valuation of $500 (which pre-money valuation shall include an [unallocated and uncommitted] employee option pool representing [__]% of the fully-diluted post-money capitalization) and a fully-diluted post-money valuation of $1500.

Other sections remain the same.
'''
distance = string_similarity(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 13843

set_distance = set_similarity(set(TermSheet_text), set(response.choices[0].message.content))
print("Jaccard distance:", set_distance)
# Jaccard distance: 0.1728395061728395

set1 = set(TermSheet_text.split())
set2 = set(response.choices[0].message.content.split())

similarity = jaccard_similarity(set1, set2)
print("Jaccard similarity:", similarity)
# Jaccard similarity: 0.20225988700564973

distance = levenshtein_distance(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 13843

response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "Read the given Term Sheet text content carefully and analyze the blanks in the text that is to be filled from a given set of answers. you have to fill the correct answers in given blanks enclosed within square braces sometimes with correct answers from given set of answers and do not hallucinate by yourself for filling any blank."},
    {"role": "user", "content": TermSheet_text},
    {"role": "assistant", "content": "I have analyzed the Term Sheet and enlist the blanks to be filled. Provide the answer set. I will provide the Appropriately filled Term Sheet text from provided answers in set of answers and leave the blanks as it is whose answers are not available inside the set."},
    {"role": "user", "content": Answerset}
  ]
)

print(response.choices[0].message.content)

'''
TERM SHEET 
FOR SERIES A PREFERRED STOCK FINANCING OF
ABC pvt ltd, INC.
[__________, 20__]

This Term Sheet summarizes the principal terms of the Series A Preferred Stock Financing of ABC pvt ltd, Inc., a Delaware corporation (the “Company”).  In consideration of the time and expense devoted and to be devoted by the Investors with respect to this investment, the No Shop/Confidentiality provisions of this Term Sheet shall be binding obligations of the Company whether or not the financing is consummated.  No other legally binding obligations will be created until definitive agreements are executed and delivered by all parties.  This Term Sheet is not a commitment to invest, and is conditioned on the completion of the conditions to closing set forth below.  This Term Sheet shall be governed in all respects by the laws of Delaware.
Offering Terms

Security: Series A Preferred Stock (the “Series A Preferred”).
Closing Date: As soon as practicable following the Company’s acceptance of this Term Sheet and satisfaction of the conditions to closing (the “Closing”).
Conditions to Closing: Standard conditions to Closing, including, among other things, satisfactory completion of financial and legal due diligence, qualification of the shares under applicable Blue Sky laws, the filing of a Certificate of Incorporation establishing the rights and preferences of the Series A Preferred, [obtaining CFIUS clearance and/or a statement from CFIUS that no further review is necessary,] [and an opinion of counsel to the Company].
Investors: Lead Investor: Ambani [_______] shares ([__]%), $600
[as well other investors mutually agreed upon by Investors and the Company]
Amount Raised: $1000, .
Pre-Money Valuation: The price per share of the Series A Preferred (the “Original Purchase Price”) shall be the price determined on the basis of a fully-diluted pre-money valuation of $500 (which pre-money valuation shall include an [unallocated and uncommitted] employee option pool representing [__]% of the fully-diluted post-money capitalization) and a fully-diluted post-money valuation of $[______].

Please note that the complete Term Sheet is not filled as the provided information is not sufficient to fill all the blanks.
'''

distance = string_similarity(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 13750

set_distance = set_similarity(set(TermSheet_text), set(response.choices[0].message.content))
print("Jaccard distance:", set_distance)
# Jaccard distance: 0.1728395061728395

set1 = set(TermSheet_text.split())
set2 = set(response.choices[0].message.content.split())

similarity = jaccard_similarity(set1, set2)
print("Jaccard similarity:", similarity)
# Jaccard similarity: 0.20495495495495494

distance = levenshtein_distance(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 13750

response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "Given Term Sheet text content. Fill up the blanks with provided answer set. Don't modify any content in Termsheet content. Keep everything as it is and only add the values in blanks from given answer set. Don't add answers for the blanks you not find answer in set of provided answers."},
    {"role": "user", "content": f'{TermSheet_text}\n{Answerset}'},
  ]
)

print(response.choices[0].message.content)

'''
TERM SHEET
FOR SERIES A PREFERRED STOCK FINANCING OF
ABC pvt ltd, INC.
[__________, 20__]

This Term Sheet summarizes the principal terms of the Series A Preferred Stock Financing of ABC pvt ltd, Inc., a Delaware corporation (the “Company”).  In consideration of the time and expense devoted and to be devoted by the Investors with respect to this investment, the No Shop/Confidentiality provisions of this Term Sheet shall be binding obligations of the Company whether or not the financing is consummated.  No other legally binding obligations will be created until definitive agreements are executed and delivered by all parties.  This Term Sheet is not a commitment to invest, and is conditioned on the completion of the conditions to closing set forth below.  This Term Sheet shall be governed in all respects by the laws of Delaware.
Offering Terms


Security:
Series A Preferred Stock (the “Series A Preferred”).
Closing Date:
As soon as practicable following the Company’s acceptance of this Term Sheet and satisfaction of the conditions to closing (the “Closing”).
Conditions to Closing:
Standard conditions to Closing, including, among other things, satisfactory completion of financial and legal due diligence, qualification of the shares under applicable Blue Sky laws, the filing of a Certificate of Incorporation establishing the rights and preferences of the Series A Preferred, [obtaining CFIUS clearance and/or a statement from CFIUS that no further review is necessary,] [and an opinion of counsel to the Company].
Investors:
Investor No. 1:  [Ambani] shares ([__]%), $[600 dollar]
Investor No. 2:  [_______] shares ([__]%), $[_________]
[as well other investors mutually agreed upon by Investors and the Company]
Amount Raised:
$[1000 dollar], .
Pre-Money Valuation:
The price per share of the Series A Preferred (the “Original Purchase Price”) shall be the price determined on the basis of a fully-diluted pre-money valuation of $[500 dollar] (which pre-money valuation shall include an [unallocated and uncommitted] employee option pool representing [__]% of the fully-diluted post-money capitalization) and a fully-diluted post-money valuation of $[______].
'''
distance = string_similarity(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 13805

set_distance = set_similarity(set(TermSheet_text), set(response.choices[0].message.content))
print("Jaccard distance:", set_distance)
# Jaccard distance: 0.18518518518518517

set1 = set(TermSheet_text.split())
set2 = set(response.choices[0].message.content.split())

similarity = jaccard_similarity(set1, set2)
print("Jaccard similarity:", similarity)
# Jaccard similarity: 0.21136363636363636

distance = levenshtein_distance(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 13805

response = client.chat.completions.create(
  model="gpt-4-0125-preview",
  messages=[
    {"role": "system", "content": "You are a Term Sheet filling bot.\
    You got Term Sheet text, Available answers as input.\
    You need to fill the Term blanks inside Terms Sheet text with relevant available answers.\
    Do not modify or add any content with you own.\
    Only add the relevant available answers at place of blanks inside Term Sheet text and leave the blanks as it whose answers not provided."},
    {"role": "user", "content": f"Fill up the sheet given the answer of the following questions make sure to get filled with correct details:\
    {TermSheet_text}\n{Answerset}"}
  ]
)

print(response.choices[0].message.content)

'''
TERM SHEET
FOR SERIES A PREFERRED STOCK FINANCING OF
ABC pvt ltd, INC.
[__________, 20__]

This Term Sheet summarizes the principal terms of the Series A Preferred Stock Financing of ABC pvt ltd, Inc., a Delaware corporation (the “Company”).  In consideration of the time and expense devoted and to be devoted by the Investors with respect to this investment, the No Shop/Confidentiality provisions of this Term Sheet shall be binding obligations of the Company whether or not the financing is consummated.  No other legally binding obligations will be created until definitive agreements are executed and delivered by all parties.  This Term Sheet is not a commitment to invest, and is conditioned on the completion of the conditions to closing set forth below.  This Term Sheet shall be governed in all respects by the laws of Delaware.
Offering Terms


Security:
Series A Preferred Stock (the “Series A Preferred”).
Closing Date:
As soon as practicable following the Company’s acceptance of this Term Sheet and satisfaction of the conditions to closing (the “Closing”).  
Conditions to Closing:
Standard conditions to Closing, including, among other things, satisfactory completion of financial and legal due diligence, qualification of the shares under applicable Blue Sky laws, the filing of a Certificate of Incorporation establishing the rights and preferences of the Series A Preferred, [obtaining CFIUS clearance and/or a statement from CFIUS that no further review is necessary,] [and an opinion of counsel to the Company].
Investors:
Investor No. 1:  Ambani shares ([__]%), $600 dollar
Investor No. 2:  [_______] shares ([__]%), $[_________]
[as well other investors mutually agreed upon by Investors and the Company]
Amount Raised:
$1000 dollar, .
Pre-Money Valuation:
The price per share of the Series A Preferred (the “Original Purchase Price”) shall be the price determined on the basis of a fully-diluted pre-money valuation of $500 dollar (which pre-money valuation shall include an [unallocated and uncommitted] employee option pool representing [__]% of the fully-diluted post-money capitalization) and a fully-diluted post-money valuation of $[______].  
CHARTER
Dividends:
[Dividends will be paid on the Series A Preferred on an as-converted basis when, as, and if paid on the Common Stock.]
Liquidation Preference:
In the event of any liquidation, dissolution or winding up of the Company, the proceeds shall be paid as follows:
[First pay the Original Purchase Price [plus [accrued and] declared and unpaid dividends] on each share of Series A Preferred (or, if greater, the amount that the Series A Preferred would receive on an as-converted basis).  The balance of any proceeds shall be distributed pro rata to holders of Common Stock.]
A merger or consolidation (other than one in which stockholders of the Company own a majority by voting power of the outstanding shares of the surviving or acquiring corporation) or a sale, lease, transfer, exclusive license or other disposition of all or substantially all of the assets of the Company will be treated as a liquidation event (a “Deemed Liquidation Event”), thereby triggering payment of the liquidation preferences described above unless the holders of [25]% of the Series A Preferred elect otherwise (the “Requisite Holders”).  [The Investors’ entitlement to their liquidation preference shall not be abrogated or diminished in the event part of the consideration is subject to escrow or indemnity holdback in connection with a Deemed Liquidation Event.]
Voting Rights:
The Series A Preferred shall vote together with the Common Stock on an as-converted basis, and not as a separate class, except (i) so long as 50% of the shares of Series A Preferred issued in the transaction are outstanding, the Series A Preferred as a separate class shall be entitled to elect 2 members of the Board of Directors ([each a] “Preferred Director”), (ii) as required by law, and (iii) as provided in “Protective Provisions” below.  The Company’s Charter will provide that the number of authorized shares of Common Stock may be increased or decreased with the approval of a majority of the Preferred and Common Stock, voting together as a single class, and without a separate class vote by the Common Stock.
Protective Provisions: 
So long as 50% shares of Series A Preferred issued in the transaction are outstanding, in addition to any other vote or approval required under the Company’s Charter or Bylaws, the Company will not, without the written consent of the Requisite Holders, either directly or by amendment, merger, consolidation, recapitalization, reclassification, or otherwise: 
(i) liquidate, dissolve or wind-up the affairs of the Company or effect any Deemed Liquidation Event; (ii) amend, alter, or repeal any provision of the Charter or Bylaws [in a manner adverse to the Series A Preferred Stock]; (iii) create or authorize the creation of or issue any other security convertible into or exercisable for any equity security unless the same ranks junior to the Series A Preferred with respect to its rights, preferences and privileges, or increase the authorized number of shares of Series A Preferred; (iv) sell, issue, sponsor, create or distribute any digital tokens, cryptocurrency or other blockchain-based assets without approval of the Board of Directors[, including the Investor Directors]; (v) purchase or redeem or pay any dividend on any capital stock prior to the Series A Preferred, other than stock repurchased at cost from former employees and consultants in connection with the cessation of their service, [or as otherwise approved by the Board of Directors[, including the approval of [at least one] Preferred Director]; or (vi) [adopt, amend, terminate or repeal any equity (or equity-linked) compensation plan or amend or waive any of the terms of any option or other grant pursuant to any such plan; (vii)] create or authorize the creation of any debt security[, if the aggregate indebtedness of the Corporation and its subsidiaries for borrowed money following such action would exceed $ 250,000 [other than equipment leases, bank lines of credit or trade payables incurred in the ordinary course] [unless such debt security has received the prior approval of the Board of Directors, including the approval of [at least one] Preferred Director; [or](viii) create or hold capital stock in any subsidiary that is not wholly-owned, or dispose of any subsidiary stock or all or substantially all of any subsidiary assets; [or (ix) increase or decrease the authorized number of directors constituting the Board of Directors or change the number of votes entitled to be cast by any director or directors on any matter].
Optional Conversion:
The Series A Preferred initially converts 1:1 to Common Stock at any time at option of holder, subject to adjustments for stock dividends, splits, combinations and similar events and as described below under “Anti-dilution Provisions.”
Anti-dilution Provisions:
In the event that the Company issues additional securities at a purchase price less than the current Series A Preferred conversion price, such conversion price shall be adjusted in accordance with the following formula:
CP2 = CP1 * (A+B) / (A+C)
Where: 
CP2 	=	Series A Conversion Price in effect immediately after new issue
CP1	=	Series A Conversion Price in effect immediately prior to new issue
A	=	Number of shares of Common Stock deemed to be outstanding immediately prior to new issue (includes all shares of outstanding common stock, all shares of outstanding preferred stock on an as-converted basis, and all outstanding options on an as-exercised basis; and does not include any convertible securities converting into this round of financing)
B	=	Aggregate consideration received by the Company with respect to the new issue divided by CP1
C	=	Number of shares of stock issued in the subject transaction


The foregoing shall be subject to customary exceptions, including, without limitation, the following:
(i) securities issuable upon conversion of any of the Series A Preferred, or as a dividend or distribution on the Series __ Preferred; (ii) securities issued upon the conversion of any debenture, warrant, option, or other convertible security; (iii) Common Stock issuable upon a stock split, stock dividend, or any subdivision of shares of Common Stock; (iv) shares of Common Stock (or options to purchase such shares of Common Stock) issued or issuable to employees or directors of, or consultants to, the Company pursuant to any plan approved by the Company’s Board of Directors [including at least [one] Preferred Director(s)], and other customary exceptions. 
Mandatory Conversion:
Each share of Series A Preferred will automatically be converted into Common Stock at the then applicable conversion rate in the event of the closing of a firm commitment underwritten public offering [with a price of 2 times the Original Purchase Price] (subject to adjustments for stock dividends, splits, combinations and similar events) and [gross] proceeds to the Company, or (ii) upon the written consent of the Requisite Holders. 
[Pay-to-Play:
Unless the Requisite Holders elect otherwise, on any subsequent [down] round all holders of Series A Preferred Stock are required to purchase their pro rata share of the securities set aside by the Board of Directors for purchase by such holders.  [A proportionate amount/all] of the shares of Series A Preferred of any holder failing to do so will automatically convert to Common Stock and lose corresponding preferred stock rights, such as the right to a Board seat if applicable.
[Redemption Rights: 
Unless prohibited by applicable law governing distributions to stockholders, the Series A Preferred shall be redeemable at the option of the Requisite Holders commencing any time after the five (5) year anniversary of the Closing at a price equal to the Original Purchase Price [plus all accrued/declared but unpaid dividends].  Redemption shall occur in three equal annual portions.  Upon a redemption request from the holders of the required percentage of the Series A Preferred, all Series A Preferred shares shall be redeemed [(except for any Series A holders who affirmatively opt-out)]. 
STOCK PURCHASE AGREEMENT
Representations and Warranties:
Standard representations and warranties by the Company customary for its size and industry.  [Representations and warranties regarding CFIUS.]
[Regulatory Covenants (CFIUS):
Investors and the Company shall use reasonable best efforts to submit the proposed transaction to the Committee on Foreign Investment in the United States (“CFIUS”) and obtain CFIUS clearance or a statement from CFIUS that no further review is necessary with respect to the parties’ [notice/declaration]].
INVESTORS’ RIGHTS AGREEMENT
Registrable Securities:
All shares of Common Stock issuable upon conversion of the Series A Preferred and any other Common Stock held by the Investors will be deemed “Registrable Securities.” All details of such registration of securities will be laid out in the Definitive Agreements.
Non-Competition Agreements: 
Founders and key employee will enter into a [one] year non-competition agreement in a form reasonably acceptable to the Investors.
Non-Disclosure, Non-Solicitation and Developments Agreement:
Each current, future and former founder, employee and consultant will enter into a non-disclosure, non-solicitation and proprietary rights assignment agreement in a form reasonably acceptable to the Investors.  
Employee Stock Options:
All [future] employee options to vest as follows:  [25% after one year, with remaining vesting monthly over next 36 months].
RIGHT OF FIRST REFUSAL/CO-SALE AGREEMENT
Right of First Refusal/
Right of Co-Sale (Take-Me-Along):
Company first and Investors second will have a right of first refusal with respect to any shares of capital stock of the Company proposed to be transferred by current and future employees holding 1% or more of Company Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options), with a right of oversubscription for Investors of shares unsubscribed by the other Investors.  Before any such person may sell Common Stock, he will give the Investors an opportunity to participate in such sale on a basis proportionate to the amount of securities held by the seller and those held by the participating Investors. 
VOTING AGREEMENT
Board of Directors:
At the Closing, the Board of Directors shall consist of [______] members comprised of (i) [name] as [the representative designated by [Ambani], as the lead Investor, (ii) [name] as the representative designated by the remaining Investors, (iii) [name] as the representative designated by the Common Stockholders, (iv) the person then serving as the Chief Executive Officer of the Company, and (v) [___] person(s) who are not employed by the Company and who are mutually acceptable [to the other directors].
[Drag Along:
Holders of Preferred Stock and all current and future holders of greater than [1]% of Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options) shall be required to enter into an agreement with the Investors that provides that such stockholders will vote their shares in favor of a Deemed Liquidation Event or transaction in which 50% or more of the voting power of the Company is transferred and which is approved by [the Board of Directors] the Requisite Holders [and holders of a majority of the shares of Common Stock then held by employees of the Company (collectively with the Requisite Holders, the “Electing Holders”), so long as the liability of each stockholder in such transaction is several (and not joint) and does not exceed the stockholder’s pro rata portion of any claim and the consideration to be paid to the stockholders in such transaction will be allocated as if the consideration were the proceeds to be distributed to the Company’s stockholders in a liquidation under the Company’s then-current Charter, subject to customary limitations.]] 
OTHER MATTERS
[Founders’ Stock:


Buyback right/vesting for 5% for first [12 months] after Closing; thereafter, right lapses in equal monthly increments over following 48 months.]  
[Existing Preferred Stock:
The terms set forth above for the Series [A] Preferred Stock are subject to a review of the rights, preferences and restrictions for the existing Preferred Stock. Any changes necessary to conform the existing Preferred Stock to this term sheet will be made at the Closing.]
No-Shop/Confidentiality:
The Company and the Investors agree to work in good faith expeditiously towards the Closing. The Company and the founders agree that they will not, for a period of 6 months from the date these terms are accepted, take any action to solicit, initiate, encourage or assist the submission of any proposal, negotiation or offer from any person or entity other than the Investors relating to the sale or issuance, of any of the capital stock of the Company [or the acquisition, sale, lease, license or other disposition of the Company or any material part of the stock or assets of the Company] and shall notify the Investors promptly of any inquiries by any third parties in regards to the foregoing.  The Company will not disclose the terms of this Term Sheet to any person other than employees, stockholders, members of the Board of Directors and the Company’s accountants and attorneys and other potential Investors, as lead Investor, without the written consent of the Investors (which shall not be unreasonably withheld, conditioned or delayed).  
Expiration:
This Term Sheet expires in 15 days from the date of this document if not accepted by the Company by that date.  

[Signature Page Follows]
EXECUTED this [__] day of [_________], 20[__].

[Signature Blocks]
'''
distance = string_similarity(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 146

set_distance = set_similarity(set(TermSheet_text), set(response.choices[0].message.content))
print("Jaccard distance:", set_distance)
# Jaccard distance: 0.037037037037037035

set1 = set(TermSheet_text.split())
set2 = set(response.choices[0].message.content.split())

similarity = jaccard_similarity(set1, set2)
print("Jaccard similarity:", similarity)
# Jaccard similarity: 0.9739229024943311

distance = levenshtein_distance(TermSheet_text, response.choices[0].message.content)
print("Levenshtein distance:", distance)
# Levenshtein distance: 146

gpt3portalPrompt1 = '''
Fill up the sheet given the answer of the following questions make sure to get filled with correct details(Prompt with sheet content same time):
'''
response = '''
TERM SHEET
FOR SERIES A PREFERRED STOCK FINANCING OF
ABC Pvt Ltd
[__________, 20__]

This Term Sheet summarizes the principal terms of the Series A Preferred Stock Financing of ABC Pvt Ltd, a Delaware corporation (the “Company”). In consideration of the time and expense devoted and to be devoted by the Investors with respect to this investment, the No Shop/Confidentiality provisions of this Term Sheet shall be binding obligations of the Company whether or not the financing is consummated. No other legally binding obligations will be created until definitive agreements are executed and delivered by all parties. This Term Sheet is not a commitment to invest, and is conditioned on the completion of the conditions to closing set forth below. This Term Sheet shall be governed in all respects by the laws of Delaware.
Offering Terms

Security:
Series A Preferred Stock (the “Series A Preferred”).
Closing Date:
As soon as practicable following the Company’s acceptance of this Term Sheet and satisfaction of the conditions to closing (the “Closing”).
Conditions to Closing:
Standard conditions to Closing, including, among other things, satisfactory completion of financial and legal due diligence, qualification of the shares under applicable Blue Sky laws, the filing of a Certificate of Incorporation establishing the rights and preferences of the Series A Preferred, [obtaining CFIUS clearance and/or a statement from CFIUS that no further review is necessary,] [and an opinion of counsel to the Company].
Investors:
Lead Investor: Ambani - 600 shares (60%), $600
Investor No. 2: [_______] shares ([__]%), $[_________]
[as well other investors mutually agreed upon by Investors and the Company]
Amount Raised: $1000, .
Pre-Money Valuation:
The price per share of the Series A Preferred (the “Original Purchase Price”) shall be the price determined on the basis of a fully-diluted pre-money valuation of $500 (which pre-money valuation shall include an [unallocated and uncommitted] employee option pool representing [__]% of the fully-diluted post-money capitalization) and a fully-diluted post-money valuation of $2000.  
CHARTER
Dividends:
[Dividends will be paid on the Series A Preferred on an as-converted basis when, as, and if paid on the Common Stock.]
Liquidation Preference:
In the event of any liquidation, dissolution or winding up of the Company, the proceeds shall be paid as follows:
[First pay the Original Purchase Price [plus [accrued and] declared and unpaid dividends] on each share of Series A Preferred (or, if greater, the amount that the Series A Preferred would receive on an as-converted basis). The balance of any proceeds shall be distributed pro rata to holders of Common Stock.]
A merger or consolidation (other than one in which stockholders of the Company own a majority by voting power of the outstanding shares of the surviving or acquiring corporation) or a sale, lease, transfer, exclusive license or other disposition of all or substantially all of the assets of the Company will be treated as a liquidation event (a “Deemed Liquidation Event”), thereby triggering payment of the liquidation preferences described above unless the holders of [25]% of the Series A Preferred elect otherwise (the “Requisite Holders”). [The Investors’ entitlement to their liquidation preference shall not be abrogated or diminished in the event part of the consideration is subject to escrow or indemnity holdback in connection with a Deemed Liquidation Event.]
Voting Rights:
The Series A Preferred shall vote together with the Common Stock on an as-converted basis, and not as a separate class, except (i) so long as 50% of the shares of Series A Preferred issued in the transaction are outstanding, the Series A Preferred as a separate class shall be entitled to elect 2 members of the Board of Directors ([each a] “Preferred Director”), (ii) as required by law, and (iii) as provided in “Protective Provisions” below. The Company’s Charter will provide that the number of authorized shares of Common Stock may be increased or decreased with the approval of a majority of the Preferred and Common Stock, voting together as a single class, and without a separate class vote by the Common Stock.
Protective Provisions:
So long as 50% shares of Series A Preferred issued in the transaction are outstanding, in addition to any other vote or approval required under the Company’s Charter or Bylaws, the Company will not, without the written consent of the Requisite Holders, either directly or by amendment, merger, consolidation, recapitalization, reclassification, or otherwise:
(i) liquidate, dissolve or wind-up the affairs of the Company or effect any Deemed Liquidation Event; (ii) amend, alter, or repeal any provision of the Charter or Bylaws [in a manner adverse to the Series A Preferred Stock]; (iii) create or authorize the creation of or issue any other security convertible into or exercisable for any equity security unless the same ranks junior to the Series A Preferred with respect to its rights, preferences and privileges, or increase the authorized number of shares of Series A Preferred; (iv) sell, issue, sponsor, create or distribute any digital tokens, cryptocurrency or other blockchain-based assets without approval of the Board of Directors[, including the Investor Directors]; (v) purchase or redeem or pay any dividend on any capital stock prior to the Series A Preferred, other than stock repurchased at cost from former employees and consultants in connection with the cessation of their service, [or as otherwise approved by the Board of Directors[, including the approval of [at least one] Preferred Director]; or (vi) [adopt, amend, terminate or repeal any equity (or equity-linked) compensation plan or amend or waive any of the terms of any option or other grant pursuant to any such plan; (vii)] create or authorize the creation of any debt security[, if the aggregate indebtedness of the Corporation and its subsidiaries for borrowed money following such action would exceed $ 250,000 [other than equipment leases, bank lines of credit or trade payables incurred in the ordinary course] [unless such debt security has received the prior approval of the Board of Directors, including the approval of [at least one] Preferred Director; [or](viii) create or hold capital stock in any subsidiary that is not wholly-owned, or dispose of any subsidiary stock or all or substantially all of any subsidiary assets; [or (ix) increase or decrease the authorized number of directors constituting the Board of Directors or change the number of votes entitled to be cast by any director or directors on any matter].
Optional Conversion:
The Series A Preferred initially converts 1:1 to Common Stock at any time at option of holder, subject to adjustments for stock dividends, splits, combinations and similar events and as described below under “Anti-dilution Provisions.”
Anti-dilution Provisions:
In the event that the Company issues additional securities at a purchase price less than the current Series A Preferred conversion price, such conversion price shall be adjusted in accordance with the following formula:
CP2 = CP1 * (A+B) / (A+C)
Where:
CP2 = Series _ Conversion Price in effect immediately after new issue
CP1 = Series _ Conversion Price in effect immediately prior to new issue
A = Number of shares of Common Stock deemed to be outstanding immediately prior to new issue (includes all shares of

 outstanding common stock, all shares of outstanding preferred stock on an as-converted basis, and all outstanding options on an as-exercised basis; and does not include any convertible securities converting into this round of financing)
B = Aggregate consideration received by the Company with respect to the new issue divided by CP1
C = Number of shares of stock issued in the subject transaction
The foregoing shall be subject to customary exceptions, including, without limitation, the following:
(i) securities issuable upon conversion of any of the Series A Preferred, or as a dividend or distribution on the Series A Preferred; (ii) securities issued upon the conversion of any debenture, warrant, option, or other convertible security; (iii) Common Stock issuable upon a stock split, stock dividend, or any subdivision of shares of Common Stock; (iv) shares of Common Stock (or options to purchase such shares of Common Stock) issued or issuable to employees or directors of, or consultants to, the Company pursuant to any plan approved by the Company’s Board of Directors [including at least [one] Preferred Director(s)], and other customary exceptions.
Mandatory Conversion:
Each share of Series A Preferred will automatically be converted into Common Stock at the then applicable conversion rate in the event of the closing of a firm commitment underwritten public offering [with a price of 2 times the Original Purchase Price] (subject to adjustments for stock dividends, splits, combinations and similar events) and [gross] proceeds to the Company, or (ii) upon the written consent of the Requisite Holders.
[Pay-to-Play:
Unless the Requisite Holders elect otherwise, on any subsequent [down] round all holders of Series A Preferred Stock are required to purchase their pro rata share of the securities set aside by the Board of Directors for purchase by such holders. [A proportionate amount/all] of the shares of Series A Preferred of any holder failing to do so will automatically convert to Common Stock and lose corresponding preferred stock rights, such as the right to a Board seat if applicable.
[Redemption Rights:
Unless prohibited by applicable law governing distributions to stockholders, the Series A Preferred shall be redeemable at the option of the Requisite Holders commencing any time after the five (5) year anniversary of the Closing at a price equal to the Original Purchase Price [plus all accrued/declared but unpaid dividends]. Redemption shall occur in three equal annual portions. Upon a redemption request from the holders of the required percentage of the Series A Preferred, all Series A Preferred shares shall be redeemed [(except for any Series A holders who affirmatively opt-out)].
STOCK PURCHASE AGREEMENT
Representations and Warranties:
Standard representations and warranties by the Company customary for its size and industry. [Representations and warranties regarding CFIUS.]
[Regulatory Covenants (CFIUS):
Investors and the Company shall use reasonable best efforts to submit the proposed transaction to the Committee on Foreign Investment in the United States (“CFIUS”) and obtain CFIUS clearance or a statement from CFIUS that no further review is necessary with respect to the parties’ [notice/declaration]].
INVESTORS’ RIGHTS AGREEMENT
Registrable Securities:
All shares of Common Stock issuable upon conversion of the Series A Preferred and any other Common Stock held by the Investors will be deemed “Registrable Securities.” All details of such registration of securities will be laid out in the Definitive Agreements.
Non-Competition Agreements:
Founders and key employee will enter into a [one] year non-competition agreement in a form reasonably acceptable to the Investors.
Non-Disclosure, Non-Solicitation and Developments Agreement:
Each current, future and former founder, employee and consultant will enter into a non-disclosure, non-solicitation and proprietary rights assignment agreement in a form reasonably acceptable to the Investors.
Employee Stock Options:
All [future] employee options to vest as follows: [25% after one year, with remaining vesting monthly over next 36 months].
RIGHT OF FIRST REFUSAL/CO-SALE AGREEMENT
Right of First Refusal/
Right of Co-Sale (Take-Me-Along):
Company first and Investors second will have a right of first refusal with respect to any shares of capital stock of the Company proposed to be transferred by current and future employees holding 1% or more of Company Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options), with a right of oversubscription for Investors of shares unsubscribed by the other Investors. Before any such person may sell Common Stock, he will give the Investors an opportunity to participate in such sale on a basis proportionate to the amount of securities held by the seller and those held by the participating Investors.
VOTING AGREEMENT
Board of Directors:
At the Closing, the Board of Directors shall consist of [______] members comprised of (i) [name] as [the representative designated by [<<Investor name>>], as the lead Investor, (ii) [name] as the representative designated by the remaining Investors, (iii) [name] as the representative designated by the Common Stockholders, (iv) the person then serving as the Chief Executive Officer of the Company, and (v) [___] person(s) who are not employed by the Company and who are mutually acceptable [to the other directors].
[Drag Along:
Holders of Preferred Stock and all current and future holders of greater than [1]% of Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options) shall be required to enter into an agreement with the Investors that provides that such stockholders will vote their shares in favor of a Deemed Liquidation Event or transaction in which 50% or more of the voting power of the Company is transferred and which is approved by [the Board of Directors] the Requisite Holders [and holders of a majority of the shares of Common Stock then held by employees of the Company (collectively with the Requisite Holders, the “Electing Holders”), so long as the liability of each stockholder in such transaction is several (and not joint) and does not exceed the stockholder’s pro rata portion of any claim and the consideration to be paid to the stockholders in such transaction will be allocated as if the consideration were the proceeds to be distributed to the Company’s stockholders in a liquidation under the Company’s then-current Charter, subject to customary limitations.]]
OTHER MATTERS
[Founders’ Stock:
Buyback right/vesting for 5% for first [12 months] after Closing; thereafter, right lapses in equal monthly increments over following 48 months.]
[Existing Preferred Stock:
The terms set forth above for the Series [_] Preferred Stock are subject to a review of the rights, preferences and restrictions for the existing Preferred Stock. Any changes necessary to conform the existing Preferred Stock to this term sheet will be made at the Closing.]
No-Shop/Confidentiality:
The Company and the Investors agree to work in good faith expeditiously towards the Closing. The Company and the founders agree that they will not, for a period of 6 months from the date these terms are accepted, take any action to solicit, initiate, encourage or assist the submission of any proposal, negotiation or offer from any person or entity other than the Investors relating to the sale or issuance, of any of the capital stock of the Company [or the acquisition, sale, lease, license or other

 disposition of the Company or any material part of the stock or assets of the Company] and shall notify the Investors promptly of any inquiries by any third parties in regards to the foregoing. The Company will not disclose the terms of this Term Sheet to any person other than employees, stockholders, members of the Board of Directors and the Company’s accountants and attorneys and other potential Investors, as lead Investor, without the written consent of the Investors (which shall not be unreasonably withheld, conditioned or delayed).
Expiration:
This Term Sheet expires in 15 days from the date of this document if not accepted by the Company by that date.

[Signature Page Follows]
EXECUTED this [__] day of [_________], 20[__].

[Signature Blocks]
'''
distance = string_similarity(TermSheet_text, response)
print("Levenshtein distance:", distance)
# Levenshtein distance: 195

set_distance = set_similarity(set(TermSheet_text), set(response)
print("Jaccard distance:", set_distance)
# Jaccard distance: 0.024691358024691357

set1 = set(TermSheet_text.split())
set2 = set(response)

similarity = jaccard_similarity(set1, set2)
print("Jaccard similarity:", similarity)
# Jaccard similarity: 0.01279317697228145

distance = levenshtein_distance(TermSheet_text, response)
print("Levenshtein distance:", distance)
# Levenshtein distance: 195

gpt3portalPrompt2 = '''
{
Team Sheet Text
}
Above is a given Term Sheet form , you need to fill that form at positions enclosed inside square braces with given answers below 
Answers:{Provided Answers}
'''
response = '''
[TERM SHEET
FOR SERIES A PREFERRED STOCK FINANCING OF
ABC Pvt Ltd,
[April 9, 2024]

This Term Sheet summarizes the principal terms of the Series A Preferred Stock Financing of ABC Pvt Ltd, a Delaware corporation (the “Company”). In consideration of the time and expense devoted and to be devoted by the Investors with respect to this investment, the No Shop/Confidentiality provisions of this Term Sheet shall be binding obligations of the Company whether or not the financing is consummated. No other legally binding obligations will be created until definitive agreements are executed and delivered by all parties. This Term Sheet is not a commitment to invest and is conditioned on the completion of the conditions to closing set forth below. This Term Sheet shall be governed in all respects by the laws of Delaware. Offering Terms

Security: Series A Preferred Stock (the “Series A Preferred”).
Closing Date: As soon as practicable following the Company’s acceptance of this Term Sheet and satisfaction of the conditions to closing (the “Closing”).
 Conditions to Closing: Standard conditions to Closing, including, among other things, satisfactory completion of financial and legal due diligence, qualification of the shares under applicable Blue Sky laws, the filing of a Certificate of Incorporation establishing the rights and preferences of the Series A Preferred, [obtaining CFIUS clearance and/or a statement from CFIUS that no further review is necessary,] [and an opinion of counsel to the Company]. 

Investors: Investor No. 1: Ambani, shares (60%), $600 
                 Investor No. 2: [_______] shares ([__]%), $[_________]
                 [as well other investors mutually agreed upon by Investors and the Company] Amount Raised: $1000
Pre-Money Valuation: The price per share of the Series A Preferred (the “Original Purchase Price”) shall be the price determined on the basis of a fully-diluted pre-money valuation of $500 (which pre-money valuation shall include an [unallocated and uncommitted] employee option pool representing [__]% of the fully-diluted post-money capitalization) and a fully-diluted post-money valuation of $[______]. CHARTER Dividends: [Dividends will be paid on the Series A Preferred on an as-converted basis when, as, and if paid on the Common Stock.] Liquidation Preference: In the event of any liquidation, dissolution, or winding up of the Company, the proceeds shall be paid as follows: [First pay the Original Purchase Price [plus [accrued and] declared and unpaid dividends] on each share of Series A Preferred (or, if greater, the amount that the Series A Preferred would receive on an as-converted basis). The balance of any proceeds shall be distributed pro rata to holders of Common Stock.] A merger or consolidation (other than one in which stockholders of the Company own a majority by voting power of the outstanding shares of the surviving or acquiring corporation) or a sale, lease, transfer, exclusive license, or other disposition of all or substantially all of the assets of the Company will be treated as a liquidation event (a “Deemed Liquidation Event”), thereby triggering payment of the liquidation preferences described above unless the holders of [25]% of the Series A Preferred elect otherwise (the “Requisite Holders”). [The Investors’ entitlement to their liquidation preference shall not be abrogated or diminished in the event part of the consideration is subject to escrow or indemnity holdback in connection with a Deemed Liquidation Event.] Voting Rights: The Series A Preferred shall vote together with the Common Stock on an as-converted basis and not as a separate class, except (i) so long as 50% of the shares of Series A Preferred issued in the transaction are outstanding, the Series A Preferred as a separate class shall be entitled to elect 2 members of the Board of Directors ([each a] “Preferred Director”), (ii) as required by law, and (iii) as provided in “Protective Provisions” below. The Company’s Charter will provide that the number of authorized shares of Common Stock may be increased or decreased with the approval of a majority of the Preferred and Common Stock, voting together as a single class, and without a separate class vote by the Common Stock. Protective Provisions: So long as 50% shares of Series A Preferred issued in the transaction are outstanding, in addition to any other vote or approval required under the Company’s Charter or Bylaws, the Company will not, without the written consent of the Requisite Holders, either directly or by amendment, merger, consolidation, recapitalization, reclassification, or otherwise: (i) liquidate, dissolve or wind-up the affairs of the Company or effect any Deemed Liquidation Event; (ii) amend, alter, or repeal any provision of the Charter or Bylaws [in a manner adverse to the Series A Preferred Stock]; (iii) create or authorize the creation of or issue any other security convertible into or exercisable for any equity security unless the same ranks junior to the Series A Preferred with respect to its rights, preferences, and privileges, or increase the authorized number of shares of Series A Preferred; (iv) sell, issue, sponsor, create or distribute any digital tokens, cryptocurrency or other blockchain-based assets without approval of the Board of Directors[, including the Investor Directors]; (v) purchase or redeem or pay any dividend on any capital stock prior to the Series A Preferred, other than stock repurchased at cost from former employees and consultants in connection with the cessation of their service, [or as otherwise approved by the Board of Directors[, including the approval of [at least one] Preferred Director]; or (vi) [adopt, amend, terminate or repeal any equity (or equity-linked) compensation plan or amend or waive any of the terms of any option or other grant pursuant to any such plan; (vii)] create or authorize the creation of any debt security[, if the aggregate indebtedness of the Corporation and its subsidiaries for borrowed money following such action would exceed   [other than equipment leases, bank lines of credit or trade payables incurred in the ordinary course] [unless such debt security has received the prior approval of the Board of Directors, including the approval of [at least one] Preferred Director; [or](viii) create or hold capital stock in any subsidiary that is not wholly-owned, or dispose of any subsidiary stock or all or substantially all of any subsidiary assets; [or (ix) increase or decrease the authorized number of directors constituting the Board of Directors or change the number of votes entitled to be cast by any director or directors on any matter]. Optional Conversion: The Series A Preferred initially converts 1:1 to Common Stock at any time at the option of the holder, subject to adjustments for stock dividends, splits, combinations, and similar events and as described below under “Anti-dilution Provisions.” Anti-dilution Provisions: In the event that the Company issues additional securities at a purchase price less than the current Series A Preferred conversion price, such conversion price shall be adjusted in accordance with the following formula: CP2 = CP1 * (A+B) / (A+C) Where: CP2 = Series A Conversion Price in effect immediately after new issue CP1 = Series A Conversion Price in effect immediately prior to new issue A = Number of shares of Common Stock deemed to be outstanding immediately prior to new issue (includes all shares of outstanding common stock, all shares of outstanding

 preferred stock on an as-converted basis, and all outstanding options on an as-exercised basis; and does not include any convertible securities converting into this round of financing) B = Aggregate consideration received by the Company with respect to the new issue divided by CP1 C = Number of shares of stock issued in the subject transaction The foregoing shall be subject to customary exceptions, including, without limitation, the following: (i) securities issuable upon conversion of any of the Series A Preferred, or as a dividend or distribution on the Series A Preferred; (ii) securities issued upon the conversion of any debenture, warrant, option, or other convertible security; (iii) Common Stock issuable upon a stock split, stock dividend, or any subdivision of shares of Common Stock; (iv) shares of Common Stock (or options to purchase such shares of Common Stock) issued or issuable to employees or directors of, or consultants to, the Company pursuant to any plan approved by the Company’s Board of Directors [including at least [one] Preferred Director(s)], and other customary exceptions. Mandatory Conversion: Each share of Series A Preferred will automatically be converted into Common Stock at the then applicable conversion rate in the event of the closing of a firm commitment underwritten public offering [with a price of 2 times the Original Purchase Price] (subject to adjustments for stock dividends, splits, combinations, and similar events) and [gross] proceeds to the Company, or (ii) upon the written consent of the Requisite Holders. [Pay-to-Play: Unless the Requisite Holders elect otherwise, on any subsequent [down] round all holders of Series A Preferred Stock are required to purchase their pro rata share of the securities set aside by the Board of Directors for purchase by such holders. [A proportionate amount/all] of the shares of Series A Preferred of any holder failing to do so will automatically convert to Common Stock and lose corresponding preferred stock rights, such as the right to a Board seat if applicable. [Redemption Rights: Unless prohibited by applicable law governing distributions to stockholders, the Series A Preferred shall be redeemable at the option of the Requisite Holders commencing any time after the five (5) year anniversary of the Closing at a price equal to the Original Purchase Price [plus all accrued/declared but unpaid dividends]. Redemption shall occur in three equal annual portions. Upon a redemption request from the holders of the required percentage of the Series A Preferred, all Series A Preferred shares shall be redeemed [(except for any Series A holders who affirmatively opt-out)]. STOCK PURCHASE AGREEMENT Representations and Warranties: Standard representations and warranties by the Company customary for its size and industry. [Representations and warranties regarding CFIUS.] [Regulatory Covenants (CFIUS): Investors and the Company shall use reasonable best efforts to submit the proposed transaction to the Committee on Foreign Investment in the United States (“CFIUS”) and obtain CFIUS clearance or a statement from CFIUS that no further review is necessary with respect to the parties’ [notice/declaration]]. INVESTORS’ RIGHTS AGREEMENT Registrable Securities: All shares of Common Stock issuable upon conversion of the Series A Preferred and any other Common Stock held by the Investors will be deemed “Registrable Securities.” All details of such registration of securities will be laid out in the Definitive Agreements. Non-Competition Agreements: Founders and key employees will enter into a [one] year non-competition agreement in a form reasonably acceptable to the Investors. Non-Disclosure, Non-Solicitation, and Developments Agreement: Each current, future, and former founder, employee, and consultant will enter into a non-disclosure, non-solicitation, and proprietary rights assignment agreement in a form reasonably acceptable to the Investors. Employee Stock Options: All [future] employee options to vest as follows: [25% after one year, with remaining vesting monthly over the next 36 months]. RIGHT OF FIRST REFUSAL/CO-SALE AGREEMENT Right of First Refusal/ Right of Co-Sale (Take-Me-Along): The Company first and Investors second will have a right of first refusal with respect to any shares of capital stock of the Company proposed to be transferred by current and future employees holding 1% or more of Company Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options), with a right of oversubscription for Investors of shares unsubscribed by the other Investors. Before any such person may sell Common Stock, he will give the Investors an opportunity to participate in such sale on a basis proportionate to the amount of securities held by the seller and those held by the participating Investors. VOTING AGREEMENT Board of Directors: At the Closing, the Board of Directors shall consist of [______] members comprised of (i) [Ambani] as [the representative designated by [<<Investor name>>], as the lead Investor, (ii) [name] as the representative designated by the remaining Investors, (iii) [name] as the representative designated by the Common Stockholders, (iv) the person then serving as the Chief Executive Officer of the Company, and (v) [___] person(s) who are not employed by the Company and who are mutually acceptable [to the other directors]. [Drag Along: Holders of Preferred Stock and all current and future holders of greater than [1]% of Common Stock (assuming conversion of Preferred Stock and whether then held or subject to the exercise of options) shall be required to enter into an agreement with the Investors that provides that such stockholders will vote their shares in favor of a Deemed Liquidation Event or transaction in which 50% or more of the voting power of the Company is transferred and which is approved by [the Board of Directors] the Requisite Holders [and holders of a majority of the shares of Common Stock then held by employees of the Company (collectively with the Requisite Holders, the “Electing Holders”), so long as the liability of each stockholder in such transaction is several (and not joint) and does not exceed the stockholder’s pro rata portion of any claim and the consideration to be paid to the stockholders in such transaction will be allocated as if the consideration were the proceeds to be distributed to the Company’s stockholders in a liquidation under the Company’s then-current Charter, subject to customary limitations.]] OTHER MATTERS [Founders’ Stock: Buyback right/vesting for 5% for first [12 months] after Closing; thereafter, the right lapses in equal monthly increments over the following 48 months.] [Existing Preferred Stock: The terms set forth above for the Series [_] Preferred Stock are subject to a review of the rights, preferences, and restrictions for the existing Preferred Stock. Any changes necessary to conform the existing Preferred Stock to this term sheet will be made at the Closing.] No-Shop/Confidentiality: The Company and the Investors agree to work in good faith expeditiously towards the Closing. The Company and the founders agree that they will not, for a period of 6 months from the date these terms are accepted, take any action to solicit, initiate, encourage or assist the submission of any proposal, negotiation, or offer from any person or entity other than the Investors relating to the sale or issuance of any of the capital stock of the Company [or the acquisition, sale, lease, license, or other disposition of the Company or any material part of the

 stock or assets of the Company] and shall notify the Investors promptly of any inquiries by any third parties regarding the foregoing. The Company will not disclose the terms of this Term Sheet to any person other than employees, stockholders, members of the Board of Directors, and the Company’s accountants and attorneys and other potential Investors, as the lead Investor, without the written consent of the Investors (which shall not be unreasonably withheld, conditioned or delayed). Expiration: This Term Sheet expires in 15 days from the date of this document if not accepted by the Company by that date. [Signature Page Follows] EXECUTED this [__] day of [April], 2024.

[Signature Blocks]}
'''
distance = string_similarity(TermSheet_text, response)
print("Levenshtein distance:", distance)
# Levenshtein distance: 373

set_distance = set_similarity(set(TermSheet_text), set(response)
print("Jaccard distance:", set_distance)
# Jaccard distance: 0.04819277108433735

set1 = set(TermSheet_text.split())
set2 = set(response)

similarity = jaccard_similarity(set1, set2)
print("Jaccard similarity:", similarity)
# Jaccard similarity: 0.01276595744680851

distance = levenshtein_distance(TermSheet_text, response)
print("Levenshtein distance:", distance)
# Levenshtein distance: 373
