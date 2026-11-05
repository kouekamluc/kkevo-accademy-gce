"""Practice sets for A Level History, Lower Sixth (draft: check every fact against the lessons and textbooks)."""

from .dsl import *  # noqa: F403

COURSE = ("history", "lower-sixth")

M_CAM = "Cameroon 1884–1945"
M_EUR = "European Revolutions & Unifications"
M_IMP = "Imperialism & the First World War"
M_INT = "The Interwar Crises"

SETS = []

# ---------------------------------------------------------------------------
# 1. Treaties and borders
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_CAM, topic="Treaties and borders",
    title="The Germano-Douala Treaty and Cameroon's borders", lesson="germano-douala-treaty-and-borders",
    questions=[
        MC("On what date was the Germano-Douala Treaty signed?", [
            C("10 July 1919", why="This is the Milner-Simon declaration dividing Kamerun between Britain and France."),
            C("14 July 1884", why="This is the date the German flag was raised, two days after the treaty was signed."),
            C("12 July 1884", correct=True),
            C("4 November 1911", why="This is the Franco-German treaty that created Neukamerun."),
        ], steps=[S("Separate the two July dates", text="The treaty was signed on 12 July 1884; Nachtigal raised the German flag on 14 July 1884.")],
           concept="Germano-Douala Treaty", skill="Recall",
           hint="Do not confuse the signing of the treaty with the raising of the flag."),
        MC("Which of these was a condition in the Kings' Memorandum?", [
            C("The Duala should keep their role as middlemen in the trade with the interior", correct=True),
            C("Germany should build a railway from Douala to Yaoundé", why="The Douala–Yaoundé railway was extended under French rule; it was not a Duala condition."),
            C("The Duala should be given French citizenship", why="Citizenship was part of the later French ideal of assimilation, not the 1884 conditions."),
            C("Britain should share control of the coast", why="The Memorandum was attached to a treaty with German firms; it did not ask for British involvement."),
        ], steps=[S("Recall the Memorandum", text="It asked that Duala land should not be taken, that customs and marriages be respected, and that the Duala keep their middleman role.")],
           concept="Kings' Memorandum", skill="Recall",
           hint="Think about what the Duala feared European traders would take from them."),
        MC("Which factor best explains why the Duala kings were willing to sign a treaty with the Germans?", [
            C("Britain had refused to trade with them", why="Britain hesitated over protection; it did not refuse trade."),
            C("The League of Nations advised them to accept German protection", why="The League was created after the First World War."),
            C("Germany had already conquered the interior", why="German conquest of the interior came after 1884."),
            C("Their authority was weakening and European traders threatened their middleman monopoly", correct=True),
        ], steps=[S("Problems of the Duala rulers", text="Weakening authority, rivalry between houses (Bell, Akwa, Deido) and European traders wanting direct trade with the interior."),
                  S("Seeking a protector", text="Some had asked Britain for protection; when Britain hesitated, German traders took the chance.")],
           concept="Why the Duala kings signed", skill="Reasoning",
           hint="Look for problems inside Duala society and in their trade."),
        MC("An Afrocentric reading of the 1884 treaty would most likely stress that", [
            C("the Duala were simply objects of European rivalry", why="This is how the Duala appear in the Eurocentric reading."),
            C("the Duala kings were active negotiators who chose a protector and wrote conditions into the Memorandum", correct=True),
            C("the treaty had no effect on Cameroon's history", why="Neither reading claims this; the treaty began German Kamerun."),
            C("Bismarck acquired protectorates for trade, domestic politics and diplomacy", why="This is the Eurocentric reading, which focuses on German motives."),
        ], steps=[S("Eurocentric", text="Focuses on Germany and Bismarck; the Duala are objects of European rivalry."),
                  S("Afrocentric", text="Focuses on Duala choices: active negotiators who bargained through the Memorandum, later broken by Germany.")],
           concept="Interpretations of the treaty", skill="Interpretation",
           hint="Afrocentric means putting African actions at the centre."),
        MC("What does the case of Lock Priso of Hickory Town show about the treaty?", [
            C("That Britain controlled Hickory Town", why="German forces, not British, attacked Hickory Town in December 1884."),
            C("That Germany respected the Memorandum", why="The attack on Hickory Town and later policy show the opposite."),
            C("That all Duala supported German rule", why="Lock Priso refused to sign, so this is the opposite."),
            C("That the treaty divided Duala society from the start", correct=True),
        ], steps=[S("Evidence", text="Lock Priso refused to sign, and German forces attacked Hickory Town (Bonabéri) in December 1884."),
                  S("Conclusion", text="The Duala did not act as one group; the treaty divided them.")],
           concept="Resistance to the treaty", skill="Reasoning",
           hint="Did every Duala ruler accept the treaty?"),
        MC("Which event most clearly shows Germany breaking the Kings' Memorandum?", [
            C("The raising of the German flag on 14 July 1884", why="The flag-raising followed the treaty itself and did not break its conditions."),
            C("The 1885 convention fixing the border with Gabon", why="This was a border agreement with France, not a breach of Duala conditions."),
            C("The plan to expropriate Duala land on the Joss plateau and the execution of Rudolf Duala Manga Bell in 1914", correct=True),
            C("The arrival of the Pallottine Fathers", why="Missionary work was not covered by the Memorandum's conditions on land and trade."),
        ], steps=[S("The condition", text="The Memorandum asked that Duala land should not be taken."),
                  S("The breach", text="The colonial government planned to expropriate land on the Joss plateau; Rudolf Duala Manga Bell led protests and was executed on 8 August 1914.")],
           concept="Broken promises", skill="Reasoning",
           hint="Which condition concerned land?"),
        MC("What did France gain from the Franco-German treaty of 4 November 1911?", [
            C("German acceptance of a French protectorate in Morocco", correct=True),
            C("Neukamerun", why="Germany gained Neukamerun; France ceded it."),
            C("The Bakassi peninsula", why="Bakassi was placed on the German side by the 1913 Anglo-German agreement."),
            C("Control of Douala", why="Douala remained German until the First World War."),
        ], steps=[S("Context", text="After the Agadir (second Moroccan) crisis, France ceded parts of French Equatorial Africa (Neukamerun) to Germany."),
                  S("In return", text="Germany accepted a French protectorate in Morocco.")],
           concept="Franco-German treaty of 1911", skill="Recall",
           hint="The treaty ended a crisis in North Africa."),
        MC("Which statement best supports the view that Kamerun's borders were largely decided by events outside Africa?", [
            C("The Duala kings wrote conditions into the Kings' Memorandum", why="This is evidence of African agency at the coast, not outside events."),
            C("The 1911 border changes were a by-product of the Moroccan crisis", correct=True),
            C("Lock Priso refused to sign the treaty", why="This is local African resistance."),
            C("Duala leaders sent petitions about land", why="This is African action, not a European decision."),
        ], steps=[S("Outside Africa", text="The 1911 treaty followed the Moroccan crisis; the 1919 partition followed the First World War and was confirmed by the League."),
                  S("Inside Africa", text="Coastal treaties, local resistance and the 1914–1916 campaign. Judgement: outlines mostly decided in European capitals.")],
           concept="Making of Kamerun's borders", skill="Interpretation",
           hint="Look for an option that links a border change to a European crisis."),
    ]))

# ---------------------------------------------------------------------------
# 2. Comparative colonial rule
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_CAM, topic="Comparative colonial rule",
    title="German, British and French rule compared", lesson="comparative-colonial-rule-in-cameroon",
    questions=[
        MC("Which German governor (1895–1907) encouraged large plantation companies around Mount Cameroon?", [
            C("Gustav Nachtigal", why="Nachtigal was the consul-general who raised the German flag in 1884."),
            C("Eugen Zintgraff", why="Zintgraff led expeditions into the Grassfields; he was not governor."),
            C("Jesko von Puttkamer", correct=True),
            C("Frederick Lugard", why="Lugard is linked with British indirect rule in Nigeria."),
        ], steps=[S("Recall", text="Governor Jesko von Puttkamer (1895–1907) encouraged plantations around Mount Cameroon, which took fertile Bakweri land.")],
           concept="German imperial policy", skill="Recall",
           hint="Think of the governor linked with the loss of Bakweri land."),
        MC("What was indirect rule?", [
            C("Governing through existing African rulers as Native Authorities under European supervision", correct=True),
            C("Making Africans French in culture, language and law", why="That is the French ideal of assimilation."),
            C("Punishing subjects without trial", why="That describes the French indigénat."),
            C("Ruling through League of Nations officials", why="The League supervised the mandates but did not govern them."),
        ], steps=[S("Definition", text="The colonial power governs through existing rulers and institutions, called Native Authorities, supervised by European officers; linked to Lugard in Nigeria.")],
           concept="Indirect rule", skill="Concept",
           hint="The word indirect suggests rule through someone else."),
        MC("How was the British Cameroons administered between the wars?", [
            C("Jointly with France", why="There was no joint Anglo-French administration after 1916."),
            C("From Yaoundé", why="Yaoundé was the capital of French Cameroun."),
            C("As a separate colony with its own governor", why="It had no separate governor at this time."),
            C("As part of Nigeria, with northern and southern parts linked to different provinces", correct=True),
        ], steps=[S("Recall", text="Britain administered its two strips as part of Nigeria: the north with the Northern Provinces, the south with the Southern (later Eastern) Provinces.")],
           concept="British indirect rule in the Cameroons", skill="Recall",
           hint="Decisions were often taken in Lagos or Enugu."),
        MC("Which feature belongs to French rule rather than British rule?", [
            C("Decisions taken in Lagos or Enugu", why="These were British centres in Nigeria."),
            C("The indigénat and prestation", correct=True),
            C("Native Authorities collecting tax and running local courts", why="Native Authorities were the basis of British indirect rule."),
            C("Selling German plantations back to German owners", why="This happened in the British Cameroons in the 1920s."),
        ], steps=[S("French features", text="Subjects under the indigénat (punishment without trial) had to perform compulsory labour (prestation); chiefs acted as agents of French officials.")],
           concept="French assimilation and association", skill="Concept",
           hint="Look for the French legal and labour systems for subjects."),
        MC("Why do historians say the move from assimilation to association in French Cameroun was mainly a recognition of what was already happening?", [
            C("Because France gave all Cameroonians citizenship in 1922", why="In practice very few Africans achieved citizen status."),
            C("Because France adopted British indirect rule", why="French rule stayed more direct and centralised than British rule."),
            C("Because the League forced France to change", why="League supervision was weak and did not decide French policy."),
            C("Because very few Cameroonians ever became French citizens, and France already ruled through appointed chiefs", correct=True),
        ], steps=[S("Theory", text="Assimilation was the official ideal of making Africans French."),
                  S("Practice", text="Few became citizens; France ruled through appointed chiefs and the indigénat, which fits association.")],
           concept="Assimilation versus association", skill="Interpretation",
           hint="Compare the ideal with how many people actually became citizens."),
        MC("Which evidence best supports the claim that British rule in the Cameroons before 1945 was a policy of neglect?", [
            C("Native Authorities ran local courts", why="This shows some local government, which weakens the neglect claim."),
            C("France extended the railway from Douala to Yaoundé", why="This is evidence about French investment, not British neglect."),
            C("Few officials, little investment and decisions taken in Lagos or Enugu", correct=True),
            C("The Cameroon Development Corporation was founded in 1947", why="This is evidence against neglect, and it comes after 1945."),
        ], steps=[S("For the claim", text="Few officials, little investment, rule from Nigeria, plantations returned to German owners."),
                  S("Against", text="Native Authorities and the CDC (1947). Judgement: largely true for 1922–1945.")],
           concept="British neglect debate", skill="Interpretation",
           hint="Pick the evidence that describes how little Britain did."),
        MC("Which is a valid point of similarity between British and French rule in Cameroon?", [
            C("Both used African chiefs to collect tax and keep order", correct=True),
            C("Both invested equally in railways", why="France invested more in infrastructure; British rule is often called neglect."),
            C("Both ruled their territory as part of Nigeria", why="Only Britain ruled its share as part of Nigeria."),
            C("Both made most Africans citizens", why="Neither did; French citizenship was rare and Britain had no such policy."),
        ], steps=[S("Similarity", text="Both used chiefs to collect tax and keep order, though under France chiefs were more clearly administrative agents."),
                  S("Differences", text="Centralisation, law and labour, and the level of investment.")],
           concept="Comparing British and French rule", skill="Reasoning",
           hint="Think about who did the work of local administration in both systems."),
        MC("Many historians argue the three colonial systems were less different than their labels suggest. Which reason supports this?", [
            C("None used compulsory labour", why="All three colonial powers relied on compulsory labour in some form."),
            C("All three relied on chiefs, coercion and extraction", correct=True),
            C("All three were League mandates from 1884", why="German Kamerun was never a mandate; the mandates began in 1922."),
            C("All three applied assimilation fully", why="Assimilation was a French ideal and was rarely applied."),
        ], steps=[S("Labels", text="German conquest, British indirect rule, French assimilation and association."),
                  S("Practice", text="For most Cameroonians all three meant chiefs used as agents, coercion, taxation and extraction.")],
           concept="Theory versus practice", skill="Interpretation",
           hint="Think about the experience of ordinary people rather than the official policies."),
    ]))

# ---------------------------------------------------------------------------
# 3. Social and economic change
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_CAM, topic="Social and economic change",
    title="Social and economic change in colonial Cameroon", lesson="social-and-economic-change-colonial-cameroon",
    questions=[
        MC("Why did Victoria (now Limbe) grow in the colonial period?", [
            C("It was the German capital", why="Buea became the German capital."),
            C("It was the French capital", why="Yaoundé became the French capital after the war."),
            C("It grew with the plantations around Mount Cameroon", correct=True),
            C("It was the start of the railways", why="Douala was the main port and the start of the railways."),
        ], steps=[S("Recall", text="Douala: port and railways. Victoria: plantations around Mount Cameroon. Buea: German capital. Yaoundé: French capital.")],
           concept="Urbanization", skill="Recall",
           hint="Think of the economic activity near Mount Cameroon."),
        MC("What was the prestation in French Cameroun?", [
            C("Compulsory labour that subjects had to perform for the administration each year", correct=True),
            C("A petition to the League of Nations", why="Petitions were sent by Duala leaders; the prestation was imposed by France."),
            C("A French school certificate", why="It was a labour obligation, not an education qualification."),
            C("A tax paid in cocoa", why="It was paid in work, not crops."),
        ], steps=[S("Recall", text="Under France the prestation required subjects to work for the administration each year; the railway extension from Douala to Yaoundé used forced labour with high mortality.")],
           concept="Forced labour", skill="Recall",
           hint="It was a form of labour tax."),
        MC("Which statement about forced labour in colonial Cameroon is correct?", [
            C("It ended when France arrived in 1916", why="France used prestation and forced labour on the railway."),
            C("It was used only for mission schools", why="It was used for plantations, porterage, roads and railways."),
            C("Only Germany used it", why="All three colonial powers relied on compulsory labour."),
            C("All three colonial powers relied on compulsory labour", correct=True),
        ], steps=[S("Compare", text="Germany: plantations and porterage. France: prestation and the railway. Britain: plantation labour drawing migrants from the Grassfields and Nigeria.")],
           concept="Forced labour", skill="Concept",
           hint="Consider Germany, France and Britain in turn."),
        MC("Which mission took over Baptist work in Cameroon from 1886?", [
            C("Alfred Saker's mission", why="Saker was the English Baptist whose work was taken over."),
            C("The Basel Mission", correct=True),
            C("The Pallottine Fathers", why="The Catholic Pallottines arrived in 1890 and did not take over Baptist work."),
            C("The American Presbyterians", why="They worked in the south but did not take over Baptist work."),
        ], steps=[S("Recall", text="Under Germany, the Protestant Basel Mission took over Baptist work from 1886; the Catholic Pallottine Fathers arrived in 1890.")],
           concept="Mission education", skill="Recall",
           hint="It was a Protestant mission that arrived early in German rule."),
        MC("Which was a long-term political effect of mission education?", [
            C("It made all Cameroonians French citizens", why="Very few Africans became French citizens."),
            C("It stopped the growth of towns", why="Towns grew partly because they offered schools."),
            C("It ended forced labour", why="Forced labour continued under all three powers."),
            C("Mission-educated Cameroonians later formed much of the nationalist leadership", correct=True),
        ], steps=[S("Effects", text="Literacy, Christianity and practical skills; catechists, teachers and clerks; but also weakening of local religions and customs."),
                  S("Political effect", text="The educated class later led nationalist movements.")],
           concept="Effects of mission education", skill="Reasoning",
           hint="Think about who the future political leaders were."),
        MC("Why did the French encourage the founding of Jeucafra in 1938?", [
            C("To unite the British and French zones", why="French policy did not seek reunification."),
            C("To organise forced labour", why="Forced labour was organised through the administration and chiefs."),
            C("To show Cameroonians preferred France when Nazi Germany demanded its former colonies", correct=True),
            C("To prepare Cameroon for independence", why="France had no independence plan in 1938."),
        ], steps=[S("Immediate cause", text="Nazi Germany demanded the return of its former colonies, including Cameroon."),
                  S("French response", text="France encouraged Jeucafra (1938) to show loyalty to France; Paul Soppo Priso was a leading figure.")],
           concept="Jeucafra", skill="Reasoning",
           hint="Think about what Germany was demanding in the late 1930s."),
        MC("Why is it a mistake to describe Jeucafra as nationalist from the start?", [
            C("It was founded with French encouragement as a pro-French body, though it later gave experience of organisation", correct=True),
            C("It was founded by Germany", why="It was France, not Germany, that encouraged its founding."),
            C("It was founded only after 1960", why="It was founded in 1938."),
            C("It had no Cameroonian members", why="Cameroonians such as Paul Soppo Priso led it."),
        ], steps=[S("Origin", text="Sponsored by France to counter German claims."),
                  S("Later role", text="It gave Cameroonians experience of organisation and debate and was reorganised as Unicafra after 1945.")],
           concept="Jeucafra", skill="Interpretation",
           hint="Consider who sponsored it and why."),
        MC("A historian argues that Cameroonians used schools, towns and the press to turn colonial tools into weapons of protest. Which interpretation is this?", [
            C("The exploitation view", why="The exploitation view stresses forced labour, land seizure and low wages."),
            C("The agency view", correct=True),
            C("The Eurocentric view", why="A Eurocentric reading puts European actions, not Cameroonian choices, at the centre."),
            C("The modernisation view", why="The modernisation view stresses new opportunities and the creation of an educated class."),
        ], steps=[S("Three views", text="Modernisation: opportunities. Exploitation: costs borne by most Cameroonians. Agency: Cameroonians used colonial tools for their own ends.")],
           concept="Interpreting colonial change", skill="Interpretation",
           hint="Which view stresses Cameroonians' own actions?"),
    ]))

# ---------------------------------------------------------------------------
# 4. 1848 revolutions
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_EUR, topic="1848 revolutions",
    title="The revolutions of 1848", lesson="revolutions-of-1848",
    questions=[
        MC("Which was a short-term economic cause of the 1848 revolutions?", [
            C("The growth of the middle classes", why="This was a long-term social cause."),
            C("Resentment of the Congress of Vienna settlement", why="This was a long-term political cause dating from 1815."),
            C("Poor harvests and the potato blight of 1845–1847", correct=True),
            C("The publication of the Communist Manifesto", why="It appeared in 1848 and had little immediate influence."),
        ], steps=[S("Long-term", text="Opposition to the Vienna settlement and Metternich, growth of the middle classes, spread of liberal and nationalist ideas."),
                  S("Short-term", text="Poor harvests and potato blight, high food prices, then an industrial slump and unemployment.")],
           concept="Causes of the 1848 revolutions", skill="Reasoning",
           hint="Short-term causes came in the years just before 1848."),
        MC("Who were the main supporters of liberalism in 1848?", [
            C("The educated middle classes", correct=True),
            C("The monarchs and their armies", why="Monarchs used loyal armies to crush the revolutions."),
            C("Unemployed workers seeking the right to work", why="The right to work was a socialist aim."),
            C("Russian troops", why="Russia helped crush the Hungarian revolution."),
        ], steps=[S("Definition", text="Liberalism sought constitutions, elected parliaments, the rule of law and freedoms of speech, press and property; its main supporters were the educated middle classes.")],
           concept="Liberalism, socialism and nationalism", skill="Concept",
           hint="Think of lawyers, professors and students."),
        MC("What happened in Paris in the June Days of 1848?", [
            C("The Second Republic introduced universal male suffrage", why="This came with the declaration of the Republic after February."),
            C("King Louis-Philippe abdicated", why="This happened in February 1848."),
            C("Louis-Napoleon was elected president", why="This happened in December 1848."),
            C("Paris workers rose after the National Workshops were closed and were crushed by the army", correct=True),
        ], steps=[S("Sequence", text="February: Louis-Philippe abdicates, Second Republic. June: National Workshops closed, workers rise and are crushed. December: Louis-Napoleon elected president.")],
           concept="The 1848 revolution in France", skill="Recall",
           hint="Think about what happened to the scheme that gave work to the unemployed."),
        MC("Why did the Frankfurt Parliament fail to create a united Germany?", [
            C("Bismarck dissolved it", why="Bismarck came to power only in 1862."),
            C("Frederick William IV refused the crown it offered him in April 1849", correct=True),
            C("Austria joined and took control", why="The Parliament divided over including Austria; Austria did not take it over."),
            C("Napoleon III invaded Germany", why="Napoleon III was not yet emperor and did not invade."),
        ], steps=[S("Reasoning", text="Without the Prussian king's acceptance and army, the Parliament had no power to enforce its constitution, and it collapsed.")],
           concept="The Frankfurt Parliament", skill="Reasoning",
           hint="Who did the Parliament need to accept its offer?"),
        MC("The debate in the Frankfurt Parliament over greater Germany and lesser Germany was about", [
            C("whether Germany should be a republic or a monarchy", why="The greater and lesser labels referred to the borders, not the form of government."),
            C("whether to include Alsace and Lorraine", why="These were taken from France in 1871, much later."),
            C("whether to end serfdom", why="Serfdom was ended in the Austrian Empire; this was not the Frankfurt debate."),
            C("whether Germany should include or exclude Austria", correct=True),
        ], steps=[S("Recall", text="Greater Germany would include Austria; lesser Germany would exclude it.")],
           concept="The Frankfurt Parliament", skill="Concept",
           hint="It was a question about which lands a united Germany should contain."),
        MC("How did the Habsburgs recover control of the Austrian Empire?", [
            C("By calling in French troops", why="French troops crushed the Roman Republic, not revolts in the Austrian Empire."),
            C("By granting independence to Hungary", why="The Hungarian revolution under Kossuth was crushed in 1849."),
            C("By playing nationalities against each other and using force, with Russian help in Hungary", correct=True),
            C("By accepting the Frankfurt constitution", why="The Habsburgs did not accept it."),
        ], steps=[S("Recall", text="Prague bombarded (June 1848), Vienna retaken (October), Hungary crushed with Russian troops (1849); the Habsburgs exploited divisions between nationalities.")],
           concept="Counter-revolution", skill="Recall",
           hint="Think about the many peoples of the empire and a foreign ally."),
        MC("Lewis Namier described 1848 as a revolution of the intellectuals. What was he stressing?", [
            C("The weakness and idealism of middle-class leaders", correct=True),
            C("That economic hunger was the only cause", why="Namier's phrase points to the leaders, not to hunger."),
            C("That Germany missed a liberal path", why="That is A.J.P. Taylor's view of a turning point that failed to turn."),
            C("That the revolutions produced lasting changes", why="Other historians stress lasting changes, such as the end of serfdom."),
        ], steps=[S("Namier", text="A revolution of the intellectuals: weak, idealistic middle-class leaders."),
                  S("Taylor", text="German history reached a turning point and failed to turn.")],
           concept="Historiography of 1848", skill="Interpretation",
           hint="Who led the assemblies such as Frankfurt?"),
        MC("Which evidence would best challenge the claim that 1848 achieved nothing?", [
            C("The June Days were crushed by the army", why="This is evidence of failure."),
            C("Serfdom ended in the Austrian Empire and French men kept universal suffrage", correct=True),
            C("Russian troops crushed Hungary", why="This is evidence of failure."),
            C("Frederick William IV refused the German crown", why="This is evidence of failure, not of lasting change."),
        ], steps=[S("Balance", text="Most revolutions were defeated by 1849, but some changes lasted: the end of serfdom in the Austrian Empire and universal male suffrage in France.")],
           concept="Results of 1848", skill="Interpretation",
           hint="Look for a change that survived the counter-revolution."),
    ]))

# ---------------------------------------------------------------------------
# 5. Italian and German unification
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_EUR, topic="Italian and German unification",
    title="The unification of Italy and Germany", lesson="italian-and-german-unification",
    questions=[
        MC("What is Realpolitik?", [
            C("The Italian movement for national revival", why="That is the Risorgimento."),
            C("Government through elected parliaments and the rule of law", why="That describes liberalism."),
            C("Politics based on practical calculation of power and interest rather than ideals", correct=True),
            C("The German customs union", why="That is the Zollverein."),
        ], steps=[S("Definition", text="Realpolitik is politics based on power and interest, associated with Bismarck and Cavour.")],
           concept="Realpolitik", skill="Concept",
           hint="Real here means practical, not idealistic."),
        MC("Why did Cavour send Piedmontese troops to the Crimean War?", [
            C("To gain a seat at the peace conference and the goodwill of Britain and France", correct=True),
            C("To defend the Pope in Rome", why="France protected the Pope; this was not Cavour's aim in the Crimea."),
            C("To help Prussia defeat Austria", why="Italy allied with Prussia in 1866, after Cavour's death."),
            C("To conquer Sicily and Naples", why="Garibaldi conquered Sicily and Naples in 1860."),
        ], steps=[S("Recall", text="Cavour modernised Piedmont and joined the Crimean War to win diplomatic standing with Britain and France.")],
           concept="Cavour's diplomacy", skill="Reasoning",
           hint="Think diplomacy, not territory."),
        MC("What did Napoleon III promise Cavour at Plombières in 1858?", [
            C("Rome", why="France protected the Pope in Rome."),
            C("Venetia immediately", why="Venetia stayed Austrian until 1866."),
            C("Recognition of Garibaldi", why="Garibaldi's expedition came later, in 1860."),
            C("Military help against Austria, in return for Nice and Savoy", correct=True),
        ], steps=[S("Recall", text="At Plombières France agreed to help Piedmont against Austria; in 1859 they won at Magenta and Solferino.")],
           concept="Italian unification", skill="Recall",
           hint="It prepared the war of 1859."),
        MC("Which statement about Italian unification is correct?", [
            C("Italy was complete when the Kingdom was proclaimed in 1861", why="Venetia joined in 1866 and Rome in 1870."),
            C("Venetia was gained in 1866 by allying with Prussia, and Rome in 1870 when French troops withdrew", correct=True),
            C("Piedmont gained Venetia after the 1859 war", why="In 1859 Piedmont gained Lombardy, but not Venetia."),
            C("Garibaldi kept Naples as an independent state", why="Garibaldi handed his conquests to Victor Emmanuel II."),
        ], steps=[S("Stages", text="1859: Lombardy. 1860: central states and the south. March 1861: Kingdom of Italy. 1866: Venetia. 1870: Rome.")],
           concept="Stages of Italian unification", skill="Recall",
           hint="Unification was not complete in a single year."),
        MC("Which battle ended Austrian influence in German affairs?", [
            C("Solferino, 1859", why="Solferino was a French and Piedmontese victory in Italy."),
            C("Sedan, 1870", why="Sedan was a defeat of France, not Austria."),
            C("The Danish war of 1864", why="In 1864 Austria fought alongside Prussia."),
            C("Königgrätz (Sadowa), 1866", correct=True),
        ], steps=[S("Recall", text="After Königgrätz Austria was excluded from German affairs and the North German Confederation was formed in 1867 under Prussia.")],
           concept="German unification", skill="Recall",
           hint="It was a short war in 1866."),
        MC("What role did the Ems telegram play in German unification?", [
            C("It ended the war with Denmark", why="The Ems telegram belongs to the 1870 crisis with France."),
            C("It offered the German crown to Frederick William IV", why="That offer was made by the Frankfurt Parliament in 1849."),
            C("Bismarck's edited version helped lead France to declare war in 1870", correct=True),
            C("It created the Zollverein", why="The Zollverein was set up in 1834."),
        ], steps=[S("Context", text="A dispute over a Hohenzollern candidate for the Spanish throne."),
                  S("Effect", text="Bismarck's edited telegram led France to declare war; the southern states joined Prussia; the Empire was proclaimed on 18 January 1871.")],
           concept="Franco-Prussian War", skill="Reasoning",
           hint="Think about how the war of 1870 began."),
        MC("A.J.P. Taylor and many later historians view Bismarck mainly as", [
            C("an opportunist who reacted to events and kept several options open", correct=True),
            C("a figure less important than coal and iron", why="This is the structural view associated with Keynes and economic historians."),
            C("a liberal revolutionary", why="Bismarck practised Realpolitik and opposed revolution from below."),
            C("a master planner who followed a sequence of three wars", why="This is the view of older nationalist historians and Bismarck's memoirs."),
        ], steps=[S("Three views", text="Master planner (nationalist historians, memoirs); opportunist (Taylor); structural forces (Keynes, economic historians).")],
           concept="Did Bismarck have a master plan?", skill="Interpretation",
           hint="Taylor doubted Bismarck's own later account."),
        MC("Which effect did German unification have on the European balance of power?", [
            C("Austria turned its attention to Italy", why="Austria turned towards the Balkans, where it competed with Russia."),
            C("Germany became the dominant continental power and France wanted Alsace-Lorraine back", correct=True),
            C("The 1815 balance was restored", why="The 1815 balance was replaced by a system dominated by Germany."),
            C("France became the strongest continental power", why="Germany became the strongest; France was humiliated."),
        ], steps=[S("Effects", text="Germany dominant; France hostile over Alsace-Lorraine; Austria turned to the Balkans; Bismarck tried to isolate France through alliances.")],
           concept="Effects on the balance of power", skill="Reasoning",
           hint="Think about the winner and the loser of 1870–1871."),
    ]))

# ---------------------------------------------------------------------------
# 6. The Scramble for Africa
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_IMP, topic="The Scramble for Africa",
    title="The Scramble for Africa: interpretations", lesson="scramble-for-africa-interpretations",
    questions=[
        MC("Which African states remained independent by 1914?", [
            C("Kamerun and Togo", why="Both became German protectorates in 1884."),
            C("Liberia and the Congo Free State", why="The Congo Free State was Leopold II's, recognised at Berlin."),
            C("Ethiopia and Liberia", correct=True),
            C("Egypt and Ethiopia", why="Britain occupied Egypt in 1882."),
        ], steps=[S("Recall", text="By 1914 almost all of Africa was under European rule; only Ethiopia and Liberia stayed independent.")],
           concept="Scramble for Africa", skill="Recall",
           hint="One of them defeated Italy at Adwa in 1896."),
        MC("What did the Berlin Conference of 1884–1885 do?", [
            C("Set rules for claiming African coasts, such as effective occupation, and recognised the Congo Free State", correct=True),
            C("Gave Africans representation in European parliaments", why="No Africans were present at the conference."),
            C("Ended the South African War", why="The South African War was fought in 1899–1902."),
            C("Drew all the borders of Africa", why="Most borders were fixed later by bilateral agreements."),
        ], steps=[S("Recall", text="Chaired by Bismarck, it set rules such as effective occupation and recognised Leopold II's Congo Free State. No Africans attended.")],
           concept="Berlin Conference", skill="Recall",
           hint="It set rules for the Scramble rather than dividing the map."),
        MC("Which historian argued that imperialism was a necessary stage of monopoly capitalism?", [
            C("Ronald Robinson", why="Robinson, with Gallagher, developed the peripheral interpretation."),
            C("J.A. Hobson", why="Hobson, a liberal, saw imperialism as a distortion that reform could cure."),
            C("D.K. Fieldhouse", why="Fieldhouse criticised the economic interpretation."),
            C("Lenin", correct=True),
        ], steps=[S("Hobson and Lenin", text="Hobson (1902): surplus capital and financiers. Lenin (1916): imperialism as the highest stage of capitalism.")],
           concept="Economic and Marxist interpretation", skill="Interpretation",
           hint="He wrote Imperialism, the Highest Stage of Capitalism."),
        MC("What was D.K. Fieldhouse's criticism of the economic interpretation?", [
            C("Bismarck opposed colonies throughout his career", why="Bismarck made colonial moves in 1884."),
            C("Relatively little European investment went to tropical Africa, and much of the Scramble came before the period Lenin described", correct=True),
            C("Africans were not involved at all", why="This is not Fieldhouse's argument; Afrocentric historians stress African agency."),
            C("Egypt in 1882 was irrelevant", why="Fieldhouse's critique concerned investment and timing, not Egypt."),
        ], steps=[S("Critique", text="Little capital went to tropical Africa; much partition predated monopoly capitalism."),
                  S("Reply", text="Supporters say hopes of future profit, not actual investment, mattered.")],
           concept="Critique of the economic interpretation", skill="Interpretation",
           hint="Think about where European money was actually invested."),
        MC("According to Robinson and Gallagher, what event triggered the Scramble?", [
            C("The battle of Adwa in 1896", why="Adwa came well after the Scramble began."),
            C("The Fashoda crisis of 1898", why="Fashoda was a later Anglo-French clash."),
            C("The Berlin Conference", why="The conference came after the Scramble had begun."),
            C("Britain's occupation of Egypt in 1882, to protect the route to India", correct=True),
        ], steps=[S("Peripheral theory", text="In Africa and the Victorians (1961), crises on the periphery drew Europeans in; Egypt in 1882 was the trigger.")],
           concept="Peripheral interpretation", skill="Interpretation",
           hint="Think about the Suez Canal."),
        MC("Which school of interpretation stresses national prestige, great-power rivalry and Bismarck's diplomacy?", [
            C("The peripheral school", why="It stresses crises in Africa itself."),
            C("The Marxist school", why="It stresses capitalism and investment."),
            C("The Eurocentric school", correct=True),
            C("The Afrocentric school", why="It stresses African choices and resistance."),
        ], steps=[S("Four schools", text="Economic/Marxist: European capitalism. Eurocentric: European politics and diplomacy. Peripheral: crises in Africa. Afrocentric: African societies and choices.")],
           concept="Eurocentric interpretation", skill="Interpretation",
           hint="Where does this school locate the causes: in Europe or in Africa?"),
        MC("Which historians are linked with the Afrocentric interpretation in the lesson?", [
            C("J.F. Ade Ajayi and the authors of the UNESCO General History of Africa", correct=True),
            C("Robinson and Gallagher", why="They developed the peripheral interpretation."),
            C("Taylor and Namier", why="They are known for other debates, such as 1848 and Bismarck."),
            C("Hobson and Lenin", why="They put forward economic explanations."),
        ], steps=[S("Afrocentric school", text="Stresses African agency: rulers negotiated, collaborated, traded and resisted. A.G. Hopkins linked the West African Scramble to a crisis in trade after the end of the slave trade.")],
           concept="Afrocentric interpretation", skill="Interpretation",
           hint="Think of African historians and a major African history project."),
        MC("Which piece of evidence best supports the view that Africans were not passive victims of the Scramble?", [
            C("Hobson's argument about surplus capital", why="This is an economic explanation focused on Europe."),
            C("Ethiopia's victory over Italy at Adwa in 1896", correct=True),
            C("Britain's occupation of Egypt in 1882", why="This is a European action used by the peripheral school."),
            C("No Africans attended the Berlin Conference", why="This shows Africans were excluded, supporting the opposite view."),
        ], steps=[S("For", text="Duala treaties in 1884, collaboration and resistance, Adwa in 1896."),
                  S("Against", text="European military technology and the Berlin rules limited African power. Judgement: Africans shaped timing and form, not the overall outcome.")],
           concept="African agency", skill="Reasoning",
           hint="Look for an example of successful African action."),
    ]))

# ---------------------------------------------------------------------------
# 7. The First World War
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_IMP, topic="The First World War",
    title="The First World War: causes, peace and mandates", lesson="first-world-war-causes-and-peace",
    questions=[
        MC("Which powers formed the Triple Alliance of 1882?", [
            C("France, Russia and Serbia", why="France and Russia allied in 1894; this was not the Triple Alliance."),
            C("Britain, France and Russia", why="These three formed the Triple Entente by 1907."),
            C("Germany, Austria-Hungary and Italy", correct=True),
            C("Germany, Austria-Hungary and Russia", why="Russia allied with France in 1894."),
        ], steps=[S("Two blocs", text="Triple Alliance (1882): Germany, Austria-Hungary, Italy. Triple Entente: France and Russia (1894), Britain with France (1904) and with Russia (1907).")],
           concept="Alliance system", skill="Recall",
           hint="One of its members stayed neutral in 1914."),
        MC("Why is it a mistake to treat the alliance system as making war automatic in 1914?", [
            C("Because Italy stayed neutral in 1914 and Britain's entente was not a binding alliance", correct=True),
            C("Because Germany had no allies", why="Germany was allied to Austria-Hungary and Italy."),
            C("Because the war began in Africa", why="The war began in Europe after the July Crisis."),
            C("Because no alliances existed before 1914", why="The Triple Alliance dated from 1882 and the Franco-Russian alliance from 1894."),
        ], steps=[S("Evidence", text="Alliances did not force everyone into war: Italy stayed neutral, and Britain's ententes were agreements, not binding alliances.")],
           concept="Alliance system", skill="Reasoning",
           hint="Did every alliance partner join the war at once?"),
        MC("What was the blank cheque in July 1914?", [
            C("Austria-Hungary's ultimatum to Serbia", why="The ultimatum was sent on 23 July, after the German promise."),
            C("The reparations bill of 1921", why="Reparations were fixed after the war at 132 billion gold marks."),
            C("Britain's guarantee to Belgium", why="The blank cheque was a German promise, not a British one."),
            C("Germany's promise of full support to Austria-Hungary", correct=True),
        ], steps=[S("Sequence", text="28 June: Sarajevo assassination. Germany promises full support to Austria-Hungary. 23 July: ultimatum to Serbia. 28 July: Austria declares war.")],
           concept="July Crisis", skill="Recall",
           hint="It was a promise of support with no limits."),
        MC("Which order of events in the July Crisis is correct?", [
            C("Germany declares war on France, then on Russia", why="Germany declared war on Russia on 1 August and on France on 3 August."),
            C("Austria-Hungary declares war on Serbia, Russia mobilises, Germany declares war on Russia", correct=True),
            C("Germany invades Belgium, then the archduke is assassinated", why="The assassination on 28 June started the crisis."),
            C("Britain declares war, Russia mobilises, Austria declares war on Serbia", why="Britain declared war last, on 4 August."),
        ], steps=[S("Order", text="28 July: Austria-Hungary declares war on Serbia. Russia mobilises. 1 August: Germany declares war on Russia. 3 August: on France. 4 August: Britain declares war.")],
           concept="July Crisis", skill="Recall",
           hint="Start with the country whose heir was assassinated."),
        MC("What did Fritz Fischer argue in Griff nach der Weltmacht (1961)?", [
            C("Responsibility was spread across several governments, like sleepwalkers", why="This is Christopher Clark's argument (2012)."),
            C("Mobilisation timetables were the key cause", why="This is associated with A.J.P. Taylor."),
            C("All powers slid into war together, trapped by alliances", why="This is the shared-responsibility view that Fischer challenged."),
            C("Germany's leaders deliberately sought European and world power and bore the main responsibility", correct=True),
        ], steps=[S("Interpretations", text="Versailles verdict: Germany. 1920s–1950s: shared responsibility. Fischer (1961): Germany's deliberate aims. Clark (2012): spread across governments.")],
           concept="Fischer thesis", skill="Interpretation",
           hint="His argument caused intense controversy in West Germany in the 1960s."),
        MC("Which historian's work The Sleepwalkers (2012) spread responsibility for the war across several governments?", [
            C("Fritz Fischer", why="Fischer placed the main responsibility on Germany."),
            C("A.J.P. Taylor", why="Taylor stressed mobilisation timetables."),
            C("Christopher Clark", correct=True),
            C("Margaret MacMillan", why="MacMillan is cited in the lesson on whether Versailles was harsh, not on causes."),
        ], steps=[S("Recall", text="Christopher Clark's The Sleepwalkers (2012) spread responsibility across several governments.")],
           concept="Recent interpretations", skill="Interpretation",
           hint="Think of the most recent view in the lesson."),
        MC("Which was a term of the Treaty of Versailles (1919)?", [
            C("Germany's army was limited to 100,000 men", correct=True),
            C("Germany kept its colonies as mandates", why="Germany lost all its colonies, which became mandates under other powers."),
            C("Germany gained Alsace-Lorraine", why="Germany lost Alsace-Lorraine."),
            C("Reparations were fixed at 132 billion gold marks in the treaty itself", why="The reparations figure was fixed later, in 1921."),
        ], steps=[S("Terms", text="Loss of Alsace-Lorraine and other territory, army limited to 100,000 men, Rhineland demilitarised, Article 231, loss of all colonies.")],
           concept="Treaty of Versailles", skill="Recall",
           hint="Think about military restrictions."),
        MC("What type of League mandate was Cameroon, and how is the system interpreted?", [
            C("Class C; it was ruled as part of South West Africa", why="Class C included South West Africa and Pacific islands, not Cameroon."),
            C("Class B; critics call it annexation in disguise, while defenders stress the supervision and petition rights later used by nationalists", correct=True),
            C("Class B; all historians agree it was true international government", why="The system is debated; critics see it as annexation in disguise."),
            C("Class A; critics call it a step to immediate independence", why="Class A applied to Middle Eastern territories; Cameroon was class B."),
        ], steps=[S("Status", text="Cameroon was a class B mandate divided between France and Britain, confirmed in 1922."),
                  S("Debate", text="Critics: annexation in disguise. Defenders: international supervision and petition rights helped nationalists after 1945.")],
           concept="Mandate system", skill="Interpretation",
           hint="Cameroon and Togo were in the same class of mandate."),
    ]))

# ---------------------------------------------------------------------------
# 8. Fascism and Nazism
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_INT, topic="Fascism and Nazism",
    title="The rise of Fascism and Nazism", lesson="rise-of-fascism-and-nazism",
    questions=[
        MC("What did Italian nationalists mean by a mutilated victory?", [
            C("The socialists had won the 1919 strikes", why="The two red years refer to strikes; the mutilated victory refers to the peace."),
            C("Italy had lost the First World War", why="Italy was on the winning side in 1918."),
            C("Italy won the war but did not gain all the territory it had been promised", correct=True),
            C("Mussolini's March on Rome had failed", why="The March on Rome led to Mussolini's appointment."),
        ], steps=[S("Recall", text="Italy was on the winning side but did not receive all the territory promised, so nationalists called it a mutilated victory.")],
           concept="Rise of Mussolini", skill="Concept",
           hint="It refers to the outcome of the peace settlement for Italy."),
        MC("Why was Mussolini appointed prime minister in October 1922?", [
            C("King Victor Emmanuel III refused to declare martial law during the March on Rome and appointed him", correct=True),
            C("Hindenburg appointed him", why="Hindenburg was the German president who appointed Hitler."),
            C("The Acerbo Law gave him power", why="The Acerbo Law came in 1923, after he was already prime minister."),
            C("The Fascists won a majority in a free election", why="The Fascists were a small parliamentary group in 1922."),
        ], steps=[S("Context", text="Fear of socialism after the two red years made elites and the middle classes support the Fascists."),
                  S("Decision", text="The king refused to use the army and appointed Mussolini.")],
           concept="Rise of Mussolini", skill="Reasoning",
           hint="Think about the role of the king."),
        MC("What did Article 48 of the Weimar constitution allow?", [
            C("A bonus of seats for the leading party", why="That was Italy's Acerbo Law of 1923."),
            C("The rescheduling of reparations", why="That was the Dawes Plan of 1924."),
            C("The government to make laws without the Reichstag", why="That was the Enabling Act of March 1933."),
            C("The president to rule by emergency decree", correct=True),
        ], steps=[S("Recall", text="Article 48 gave the president emergency powers; from 1930 chancellors ruled by presidential decree.")],
           concept="Weaknesses of Weimar", skill="Recall",
           hint="The power belonged to the president, not the chancellor."),
        MC("Which list puts these events in the correct order?", [
            C("Munich Putsch, Kapp Putsch, March on Rome", why="The Kapp Putsch (1920) came before the Munich Putsch (1923)."),
            C("Kapp Putsch, March on Rome, Munich Putsch", correct=True),
            C("March on Rome, Kapp Putsch, Munich Putsch", why="The Kapp Putsch (1920) came before the March on Rome (1922)."),
            C("Kapp Putsch, Munich Putsch, March on Rome", why="The March on Rome (1922) came before the Munich Putsch (1923)."),
        ], steps=[S("Dates", text="Kapp Putsch 1920; March on Rome October 1922; Munich (Beer Hall) Putsch November 1923.")],
           concept="Interwar chronology", skill="Recall",
           hint="One of these took place in Italy, between the two German putsches."),
        MC("What happened to the Nazi vote in the elections of 1932?", [
            C("It rose to a majority in November 1932", why="The Nazis never won a majority in a free election; their vote fell in November."),
            C("It stayed at 18 percent", why="18 percent was the September 1930 result."),
            C("It fell steadily from 1930", why="It rose sharply from 1930 to July 1932."),
            C("It rose to about 37 percent in July 1932, then fell to about 33 percent in November", correct=True),
        ], steps=[S("Figures", text="September 1930: 18 percent. July 1932: about 37 percent, largest party. November 1932: about 33 percent.")],
           concept="Nazi breakthrough", skill="Recall",
           hint="The Nazis became the largest party, but their vote did not keep rising."),
        MC("Which interpretation stresses that Hitler was brought to power by conservative elites rather than by a majority vote?", [
            C("The Sonderweg view", why="The Sonderweg view stresses long-term weak democratic traditions."),
            C("The economic crisis view", why="This view stresses the Depression turning the Nazis into a mass movement."),
            C("The view of Ian Kershaw and others on elite intrigue", correct=True),
            C("The appeal and propaganda view", why="This stresses Nazi organisation and Hitler's attraction for voters."),
        ], steps=[S("Evidence", text="Papen and others around Hindenburg believed they could control Hitler; he was appointed chancellor on 30 January 1933."),
                  S("Interpretation", text="Kershaw and others stress elite intrigue.")],
           concept="Seized or handed power?", skill="Interpretation",
           hint="Think about who appointed Hitler and why."),
        MC("Which event let Hitler's government make laws without the Reichstag?", [
            C("The Enabling Act of March 1933", correct=True),
            C("Hindenburg's death", why="After Hindenburg's death in August 1934 Hitler became Führer."),
            C("The Reichstag fire", why="The fire (February 1933) was used to suspend civil rights."),
            C("The Night of the Long Knives", why="This (June 1934) killed the SA leadership."),
        ], steps=[S("Steps to dictatorship", text="Reichstag fire (Feb 1933), Enabling Act (March 1933), ban on other parties, Night of the Long Knives (June 1934), Führer (August 1934).")],
           concept="Consolidation of Nazi power", skill="Recall",
           hint="Its name tells you it enabled the government to act alone."),
        MC("Which is a valid difference between the ways Mussolini and Hitler came to power?", [
            C("Only Hitler used violence", why="Fascist squads attacked socialists; both used violence."),
            C("The Nazis were the largest party before Hitler's appointment, while the Fascists were a small parliamentary group", correct=True),
            C("Mussolini built his dictatorship faster than Hitler", why="Hitler consolidated power within 18 months; Mussolini took several years."),
            C("Only Mussolini had help from elites", why="Both had elite help: the king in 1922, Hindenburg and Papen in 1933."),
        ], steps=[S("Similarities", text="Crisis, fear of communism, violence and elite help."),
                  S("Differences", text="Hitler had greater electoral support and moved faster to dictatorship.")],
           concept="Comparing Fascism and Nazism", skill="Reasoning",
           hint="Compare their electoral strength when they were appointed."),
    ]))

# ---------------------------------------------------------------------------
# 9. Appeasement
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_INT, topic="Appeasement",
    title="Anglo-French appeasement, 1931–1939", lesson="anglo-french-appeasement",
    questions=[
        MC("Which British prime minister is most linked with appeasement?", [
            C("Edouard Daladier", why="Daladier was the French leader at Munich."),
            C("Lloyd George", why="Lloyd George represented Britain at the Paris Peace Conference in 1919."),
            C("Neville Chamberlain", correct=True),
            C("Winston Churchill", why="Churchill's memoirs condemned the appeasers."),
        ], steps=[S("Recall", text="Appeasement is linked above all to Neville Chamberlain, prime minister 1937–1940.")],
           concept="Appeasement", skill="Recall",
           hint="He signed the Munich Agreement for Britain."),
        MC("What was the Hoare-Laval Pact?", [
            C("A British and French plan to give Italy much of Abyssinia", correct=True),
            C("An agreement accepting German naval expansion", why="That was the Anglo-German Naval Agreement of 1935."),
            C("The guarantee to Poland", why="Britain and France guaranteed Poland on 31 March 1939."),
            C("The agreement on the Sudetenland", why="That was the Munich Agreement of September 1938."),
        ], steps=[S("Recall", text="It was a British and French plan to give Italy much of Abyssinia; it caused outrage when it leaked in December 1935.")],
           concept="Crises of the 1930s", skill="Recall",
           hint="It concerned Italy's invasion of 1935."),
        MC("How did Britain and France respond to the German reoccupation of the Rhineland in March 1936?", [
            C("They imposed oil sanctions", why="Sanctions were imposed on Italy over Abyssinia, and did not include oil."),
            C("They occupied the Ruhr", why="France occupied the Ruhr in 1923."),
            C("They declared war", why="They declared war only in September 1939, after the invasion of Poland."),
            C("They did not respond with force", correct=True),
        ], steps=[S("Recall", text="The reoccupation broke Versailles and Locarno, but Britain and France did not respond with force."),
                  S("Reasons", text="Many British people felt Germany was moving into its own territory; Britain was not ready and was distracted by Abyssinia; France would not act alone.")],
           concept="Remilitarisation of the Rhineland", skill="Recall",
           hint="Appeasement meant avoiding war."),
        MC("What was agreed at Munich on 29–30 September 1938?", [
            C("Germany would annex Austria", why="The Anschluss happened in March 1938, without such an agreement."),
            C("Germany would take the Sudetenland", correct=True),
            C("Britain would guarantee Poland", why="The guarantee to Poland came on 31 March 1939."),
            C("Germany and the USSR would not attack each other", why="That was the Nazi-Soviet Pact of 23 August 1939."),
        ], steps=[S("Recall", text="Chamberlain, Daladier, Hitler and Mussolini agreed that Germany would take the Sudetenland; Czechoslovakia was not invited.")],
           concept="Munich Agreement", skill="Recall",
           hint="Hitler demanded part of Czechoslovakia."),
        MC("Which was a British motive for appeasement?", [
            C("A wish to help Franco win in Spain", why="Britain followed non-intervention; Germany and Italy helped Franco."),
            C("Britain's alliance with Germany", why="Britain had no alliance with Germany."),
            C("Confidence that its rearmament was complete", why="Rearmament was slow and costly; military chiefs warned against fighting several enemies."),
            C("Fear of another mass war and of bombing of cities", correct=True),
        ], steps=[S("Motives", text="Memory of 1914–1918 and fear of bombing; military and economic weakness; empire and dominions; a view that some German grievances were fair.")],
           concept="Why Britain appeased", skill="Reasoning",
           hint="Think about the memory of 1914–1918."),
        MC("Why did French appeasement often follow British policy?", [
            C("France had no army", why="France had the larger army, but relied on the defensive Maginot Line."),
            C("France had no treaty links in Central Europe", why="France had treaty links with Czechoslovakia."),
            C("France relied on the Maginot Line, was politically divided, and would not act without Britain", correct=True),
            C("France had a strong economy and wanted to save money", why="France faced economic difficulties; that weakened it rather than giving it confidence."),
        ], steps=[S("French position", text="A defensive doctrine (Maginot Line), political division (e.g. Popular Front 1936–1938), economic difficulties and unwillingness to act without Britain.")],
           concept="French appeasement", skill="Reasoning",
           hint="Think about French military doctrine and its dependence on an ally."),
        MC("The book Guilty Men (1940), written under the pen-name Cato, represents which interpretation of appeasement?", [
            C("Orthodox", correct=True),
            C("Marxist", why="Marxist (Hobson, Lenin) is a school in the Scramble for Africa debate, not one of the three appeasement schools."),
            C("Revisionist", why="Revisionists, from the 1960s, stressed the real constraints on Chamberlain."),
            C("Post-revisionist", why="Post-revisionists such as R.A.C. Parker (1993) argued Chamberlain had alternatives."),
        ], steps=[S("Three schools", text="Orthodox: Guilty Men and Churchill condemned appeasers. Revisionist: constraints (Charmley). Post-revisionist: Parker, alternatives existed.")],
           concept="Historiography of appeasement", skill="Interpretation",
           hint="It was the first and harshest view, written soon after war began."),
        MC("What did R.A.C. Parker argue in 1993?", [
            C("Hitler was an opportunist and the war arose from mistakes on all sides", why="This is A.J.P. Taylor's argument in 1961."),
            C("Chamberlain had alternatives, such as a closer alliance with France and the USSR, but chose not to pursue them", correct=True),
            C("Chamberlain was weak and foolish, with no excuse", why="This is the orthodox view of Guilty Men and Churchill."),
            C("Chamberlain had no real choice because of constraints", why="This is the revisionist view; Charmley defended Chamberlain strongly."),
        ], steps=[S("Post-revisionism", text="Parker accepted the constraints were real, but argued alternatives existed and Chamberlain chose appeasement.")],
           concept="Historiography of appeasement", skill="Interpretation",
           hint="Parker's school comes after the revisionists."),
    ]))
