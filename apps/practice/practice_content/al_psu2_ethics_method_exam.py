"""Practice sets for A Level Philosophy (0790), Upper Sixth: Moral, Social & Political Philosophy (7 sets), Philosophical Methodology: Paper 3 Mastery (2 sets)
and Examination (3 exam-lesson sets), plus 'Paper 1 mock exam A' (50 multiple-choice questions, two per Upper Sixth topic), 'Paper 2 practice paper A'
(auto-markable parts on essay planning, key arguments and text analysis, numbered as the three sections of Paper 2) and 'Paper 3 practice paper A'
(logic problems verified by brute force, text-commentary and dissertation method, systematic philosophy). Essays cannot be marked automatically, so these
sets test understanding, argument analysis, method and logic. All passages and examples are invented for practice; no real quotations. Timings of the
mocks are KKEVO practice settings.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("philosophy", "upper-sixth")

M_MORAL = "Moral, Social & Political Philosophy"
M_METH = "Philosophical Methodology: Paper 3 Mastery"
M_EXAM = "Examination"

SETS = []


def K(prompt, right, wrongs, step, hint, concept, skill="Concept", feedback=""):
    """Question spec: the right option first, then three (text, why) wrong options. Positions are assigned by build()."""
    assert len(wrongs) == 3, prompt
    assert len(concept) <= 80, concept
    return {"prompt": prompt, "right": right, "wrongs": wrongs, "step": step, "hint": hint, "concept": concept, "skill": skill, "feedback": feedback}


def build(specs, seed):
    n = len(specs)
    pos = [i % 4 for i in range(n)]
    random.Random(seed).shuffle(pos)
    out = []
    for sp, p in zip(specs, pos):
        opts = [C(w, why=y) for w, y in sp["wrongs"]]
        opts.insert(p, C(sp["right"], correct=True))
        steps = [S("Reasoning", text=s) for s in ([sp["step"]] if isinstance(sp["step"], str) else sp["step"])]
        out.append(MC(sp["prompt"], opts, steps, concept=sp["concept"], skill=sp["skill"], hint=sp["hint"], feedback=sp["feedback"]))
    return out


def SET(module, topic, title, lesson, specs, seed, **kw):
    assert len(specs) == 8, title
    SETS.append(practice_set(module=module, topic=topic, title=title, lesson=lesson, questions=build(specs, seed), **kw))

# ================================================================== 1. Freedom and determinism
SET(M_MORAL, "Freedom and determinism", "Freedom and determinism: positions and arguments", "psu2-freedom-determinism", [
    K("Determinism is the thesis that:", "every event, including human choices, is the necessary result of earlier causes and natural laws", [
        ("some events have no cause at all", "That describes indeterminism, the opposite thesis."),
        ("outcomes occur whatever we choose", "That is fatalism; determinism makes choices part of the causes."),
        ("people are forced to act against their wishes", "Determinism does not claim that wishes are overridden; it says wishes are themselves caused.")],
      "Determinism says every event, human choices included, follows necessarily from earlier causes plus laws of nature.", "Which word links choices to earlier causes?", "Definition of determinism", "Recall"),
    K("A philosopher says: 'Determinism is true, and freedom needs the power to have done otherwise, so no one is truly free.' This is:", "hard determinism", [
        ("libertarianism", "Libertarians deny that determinism is true of human choice."),
        ("compatibilism", "Compatibilists deny that freedom needs the power to do otherwise in the strong sense."),
        ("fatalism", "Fatalism concerns outcomes fixed whatever we choose, not the two claims given.")],
      "Two claims: determinism is true and freedom needs the power to do otherwise. Together they deny freedom: hard determinism.", "Which position accepts determinism and denies freedom?", "Hard determinism", "Concept"),
    K("Which statement best expresses the compatibilist view of freedom?", "Freedom is acting from your own desires and reasons without being forced or blocked", [
        ("Freedom is the power of an uncaused choice", "That is the libertarian view."),
        ("Freedom is an illusion produced by ignorance of causes", "That is close to the hard determinist (Spinoza) view."),
        ("Freedom means that the future is already fixed", "That is fatalism, which is not a view about freedom as such.")],
      "Compatibilists (Hobbes, Hume) define freedom as absence of constraint, acting from one's own reasons, which can exist in a caused world.", "Which view says freedom and determinism can both be true?", "Compatibilism", "Concept"),
    K("The standard objection to libertarianism that an uncaused choice would be random is an objection that:", "an uncaused event seems a matter of chance, not an action the agent controls", [
        ("science has proved determinism", "The objection does not rest on a claim that science has proved determinism."),
        ("people never feel free", "People generally do feel free; that is the libertarian's evidence."),
        ("the law cannot punish anyone", "The objection concerns control over choices, not the legal system.")],
      "If a choice has no cause, critics say it is a chance event, no more 'mine' than a determined one.", "Think of what 'uncaused' suggests about control.", "Objection to libertarianism", "Reasoning"),
    K("Which of these correctly distinguishes determinism from fatalism?", "Determinism treats your choices as causes; fatalism says outcomes happen whatever you choose", [
        ("Determinism says outcomes do not happen; fatalism says they do", "Both are claims about how outcomes are fixed, not about whether they occur."),
        ("They are two names for the same thesis", "They differ on whether choices make a difference."),
        ("Fatalism needs natural laws; determinism does not", "It is determinism that appeals to causes and natural laws.")],
      "A determinist can say that revising raises the chance of passing, because revising is a cause. A fatalist says revising is pointless.", "Ask whether the choice itself matters in each view.", "Determinism and fatalism", "Concept"),
    K("A hard determinist says we cannot be responsible. Which premise do compatibilists most directly reject?", "Responsibility requires the power to have done otherwise, given the same past", [
        ("Every event has a cause", "Compatibilists accept determinism; they do not reject this premise."),
        ("We did not choose our upbringing", "Compatibilists agree that we did not choose it."),
        ("Courts punish offenders", "This is not a premise of the hard determinist's argument.")],
      "The compatibilist reply is that responsibility needs only that the act came from the agent's own reasons.", "Which premise ties responsibility to alternatives?", "Compatibilist reply to hard determinism", "Reasoning"),
    K("The law excuses a person who acts under duress. This practice most directly supports the view that responsibility requires:", "freedom from outside force and acting from one's own reasons", [
        ("the denial of determinism", "Courts do not need to decide on determinism to excuse duress."),
        ("an act that is uncaused", "Excusing duress does not say that free acts are uncaused."),
        ("fatalism about the outcome", "The excuse concerns force on the agent, not fixed outcomes.")],
      "Excuses (duress, sleepwalking, insanity) show that we hold people responsible when acts come from their own reasons, a point used by compatibilists.", "What is missing in an act done under duress?", "Excuses and responsibility", "Application"),
    K("Sartre's claim that a person is 'condemned to be free' most nearly means that:", "there is no fixed nature that decides for us, so we cannot excuse ourselves", [
        ("freedom is a punishment imposed by the state", "Sartre's point is philosophical, not about legal punishment."),
        ("all choices are decided by earlier causes", "That would be determinism, which Sartre rejects for human existence."),
        ("only some people are free", "For Sartre every person is free, though some deny it (bad faith).")],
      "For Sartre existence precedes essence, so we must choose and cannot blame a fixed nature.", "Which idea links Sartre's freedom with responsibility?", "Existentialist freedom", "Concept"),
], seed=201)

# ================================================================== 2. Conscience and duty
SET(M_MORAL, "Conscience and duty", "Conscience, Kant and duty", "psu2-conscience-duty", [
    K("For Kant, the only thing good without limit is:", "a good will", [
        ("happiness", "Happiness can be used badly or undeserved; it is not good without limit."),
        ("intelligence", "Intelligence, like other talents, can serve bad ends."),
        ("pleasure", "Pleasure is the aim of hedonism, not Kant's unconditional good.")],
      "Kant begins his ethics with the good will, which is good in itself.", "Which thing depends on nothing else for its goodness?", "Good will", "Recall"),
    K("Which is a categorical imperative?", "Keep your promises, whatever you want or fear", [
        ("If you want a good reputation, keep your promises", "This is conditional on a wish: hypothetical."),
        ("Keep promises when it is profitable", "This depends on profit: hypothetical."),
        ("Keep promises when people are watching", "This depends on being observed, so it is not a command binding in itself.")],
      "A categorical imperative commands without an 'if'.", "Look for the command that does not depend on a wish.", "Categorical imperative", "Concept"),
    K("A trader considers the maxim 'I will give false weights when it increases my profit.' Applying the universal law formula, the maxim fails because:", "if everyone followed it, buyers would stop trusting weights and the practice would collapse", [
        ("it makes some people unhappy", "That is a utilitarian reason, not Kant's contradiction test."),
        ("the law forbids it", "The test does not rest on what the law says."),
        ("God commands honesty", "The formula is a test by reason, not by an appeal to a command.")],
      "Universalised, false weighing destroys the trust on which it depends: a contradiction in conception.", "What happens to the practice if everyone does it?", "Universal law formula", "Application"),
    K("Treating an employee only as a tool for profit, ignoring his agreement and needs, violates which Kantian idea?", "Treating persons as ends and never merely as means", [
        ("Treating all pleasures as equal", "That is a Benthamite idea, unrelated to the formula."),
        ("Following the rule of the majority", "Kant's formulas are not about majority rule."),
        ("Acting on inclination", "The formula is about how persons are treated, not about inclination.")],
      "The humanity formula forbids using persons merely as means.", "Which formula speaks of persons and ends?", "Humanity formula", "Application"),
    K("W. D. Ross's prima facie duties help to deal with which problem in Kant's ethics?", "Conflicts between duties such as keeping a promise and helping someone in need", [
        ("The lack of any concept of duty", "Kant has a strong concept of duty; the problem is conflicts."),
        ("The claim that happiness is the only good", "That is utilitarianism, not Kant."),
        ("The impossibility of knowing the moral law", "Ross does not address that problem.")],
      "Prima facie duties hold unless overridden; judgement decides which is stronger.", "Why does Ross speak of duties that can be overridden?", "Prima facie duties", "Concept"),
    K("Freud explained conscience as:", "the superego, formed by internalised commands of parents and society", [
        ("a divine voice", "Some traditions say this; Freud's account is psychological."),
        ("the id's drive for pleasure", "The id is the pleasure-seeking part; conscience is linked to the superego."),
        ("pure reason applying the moral law", "That is closer to Kant than to Freud.")],
      "In Freud's model conscience arises from the superego.", "Which part of the mind is linked to conscience?", "Freud on conscience", "Recall"),
    K("A nurse gives a wrong dose because the hospital's printed chart, which she had no reason to doubt, was wrong. Her ignorance is best called:", "invincible, so her responsibility is much reduced", [
        ("vincible, so she is fully responsible", "She could not reasonably have known; vincible ignorance could have been overcome."),
        ("voluntary, because she acted", "The act was voluntary, but the ignorance concerns knowledge, not will."),
        ("irrelevant to responsibility", "Knowledge is one of the conditions of a moral act.")],
      "Invincible ignorance cannot be overcome by ordinary care and so excuses.", "Could a careful person have found out?", "Invincible ignorance", "Application"),
    K("Which pair are the two conditions usually stated for a fully responsible moral act?", "Knowledge and freedom of will", [
        ("Pleasure and profit", "These are not conditions of responsibility."),
        ("Tradition and obedience", "These are not conditions of responsibility."),
        ("Luck and intention", "Luck is not a condition; intention is part of will, but 'knowledge and freedom' is the standard pair.")],
      "A person is responsible for what they knowingly and freely do.", "What must the agent understand and be able to choose?", "Conditions of a moral act", "Recall"),
], seed=202)

# ================================================================== 3. Utilitarianism
SET(M_MORAL, "Utilitarianism", "Utilitarianism: calculus, quality and objections", "psu2-utilitarianism", [
    K("Utilitarianism is called consequentialist because it:", "judges the rightness of acts by their results", [
        ("judges acts by the motive behind them", "That is the Kantian focus on the will."),
        ("judges acts by whether they follow divine law", "That is a divine-command view."),
        ("judges acts by the character of the agent", "That is virtue ethics.")],
      "A consequentialist theory says the morality of an act depends on its consequences.", "What does 'consequence' mean?", "Consequentialism", "Recall"),
    K("Which feature of Bentham's calculus concerns how many people are affected by a pleasure or pain?", "Extent", [
        ("Intensity", "Intensity is how strong the feeling is."),
        ("Duration", "Duration is how long it lasts."),
        ("Purity", "Purity is whether the pleasure is mixed with pain.")],
      "Bentham's seven features: intensity, duration, certainty, nearness, fecundity, purity, extent.", "Which word is about spread?", "Bentham's calculus", "Recall"),
    K("A committee compares options: A gives net +20, B gives net +32 and C gives net +22 (invented scores). A Benthamite chooses:", "B, because it has the largest net total", [
        ("A, because it is the cheapest", "Cost is not part of the scores given."),
        ("C, because it helps the most people", "The decision is by net total, not by number of beneficiaries alone."),
        ("none, because the scores are invented", "The question asks for what the method recommends given the scores.")],
      "Net totals: A 20, B 32, C 22; B is largest.", "Compare the three net totals.", "Applying the calculus", "Calculation"),
    K("Mill differs from Bentham mainly in holding that pleasures differ in:", "quality as well as quantity", [
        ("quantity only", "That is Bentham's position."),
        ("their effects on God", "Mill's distinction is not theological."),
        ("their legal status", "Mill's distinction is about the value of kinds of pleasure.")],
      "Mill said higher (mental) pleasures are worth more than lower (bodily) ones.", "Which philosopher added a second dimension to pleasure?", "Higher and lower pleasures", "Concept"),
    K("A rule utilitarian objects to punishing an innocent person to calm a riot because:", "a rule allowing it would reduce overall happiness by destroying trust in justice", [
        ("the act has a bad motive", "For a consequentialist the motive does not decide."),
        ("it breaks a categorical imperative", "That is Kant's reasoning."),
        ("Mill banned all punishment", "Mill defended punishment in some cases; the objection is about the rule.")],
      "Rule utilitarians judge rules by the happiness they bring if generally followed.", "Which kind of utilitarianism judges rules?", "Rule utilitarianism", "Reasoning"),
    K("Which objection says that utilitarianism may permit sacrificing an innocent person if the total happiness is larger?", "The objection from justice and rights", [
        ("The objection from measurement", "That concerns comparing pleasures, not sacrificing an individual."),
        ("The objection from egoism", "That is about selfishness, not sacrifice for the total."),
        ("The objection from tradition", "That is not a standard objection to utilitarianism.")],
      "The scapegoat case is the standard justice objection.", "Which objection is about individuals and fairness?", "Objection from justice", "Concept"),
    K("Which statement about utilitarianism is mistaken?", "It says each person should do whatever makes themselves happiest", [
        ("It counts everyone's happiness equally", "This is correct: it is impartial."),
        ("It judges by consequences", "This is correct."),
        ("It was developed by Bentham and Mill", "This is correct.")],
      "Utilitarianism concerns the happiness of all affected, not only the agent's own: the theory of personal advantage is egoism.", "Which option confuses it with another theory?", "Utilitarianism versus egoism", "Reasoning"),
    K("Mill's harm principle says that liberty may be limited against a person's will only to:", "prevent harm to others", [
        ("make the person happier", "Mill rejected paternalism of this kind."),
        ("please the majority", "Majority preference alone is not a ground."),
        ("keep tradition", "Tradition alone is not a ground.")],
      "In On Liberty the only reason for interfering with a person's liberty is to prevent harm to others.", "Whose harm counts?", "Harm principle", "Recall"),
], seed=203)

# ================================================================== 4. Justice
SET(M_MORAL, "Justice", "Justice: Rawls, Nozick and rival views", "psu2-justice", [
    K("Distributive justice is concerned with:", "how goods, burdens and opportunities are shared in a society", [
        ("repairing a wrong done to a victim", "That is corrective justice."),
        ("punishing the guilty only", "Punishment is one part of corrective justice."),
        ("the rule of the majority", "This is a feature of democracy, not a kind of justice.")],
      "Distributive justice: sharing; corrective justice: repairing wrongs.", "Which kind is about sharing?", "Distributive and corrective justice", "Recall"),
    K("Behind Rawls's veil of ignorance the people choosing principles do not know:", "their own social position and talents", [
        ("that resources are scarce", "They know general facts like scarcity."),
        ("that people have different ideas of the good", "They know this general fact."),
        ("general facts about human psychology", "They know general psychology.")],
      "The veil hides particular facts about oneself so that the choice is unbiased.", "What would bias a chooser?", "Veil of ignorance", "Concept"),
    K("The difference principle permits inequalities only if they:", "work to the benefit of the least advantaged", [
        ("increase the total wealth of the richest", "That would not satisfy the principle."),
        ("are chosen by majority vote", "A vote does not decide: the benefit to the worst off does."),
        ("reward talent and effort in all cases", "Reward for talent is justified only if it also helps the least advantaged.")],
      "Second principle (b): inequalities must benefit the least advantaged.", "Whose position decides?", "Difference principle", "Concept"),
    K("Why does Rawls argue that people behind the veil would protect the position of the least advantaged?", "because they do not know whether they will be in that position", [
        ("because they are generous by nature", "Rawls's argument does not rest on generosity."),
        ("because the law requires it", "The principles are chosen before any law."),
        ("because wealth is unimportant", "The argument is about risk and fairness.")],
      "Not knowing their place, cautious choosers guard against the worst outcome.", "What does ignorance of one's place imply about risk?", "Rawls's argument", "Reasoning"),
    K("Nozick's objection to Rawls is that:", "a distribution is just if it arose from just acquisition and free transfer, whatever its pattern", [
        ("everyone should receive equal shares", "That is not Nozick's view."),
        ("the state should own all property", "Nozick defended strong property rights."),
        ("justice is whatever produces most happiness", "That is the utilitarian view.")],
      "Entitlement theory: justice depends on history of holdings, not pattern.", "Which writer defends a process, not pattern, theory?", "Entitlement theory", "Concept"),
    K("A school gives its 20 scholarships to the poorest applicants who also reach a minimum standard. This criterion most resembles:", "a mix of need and merit that could suit a Rawlsian concern for the worst off", [
        ("a pure lottery", "A lottery ignores need and merit."),
        ("a pure entitlement rule", "Entitlement concerns the history of holdings, not need."),
        ("a rule of equal shares", "Equal shares would not use a need criterion.")],
      "Giving priority to need within fair opportunity echoes Rawls's concern for the worst off.", "Which criterion does the rule use?", "Applying justice criteria", "Application"),
    K("Which criticism of Rawls is associated with communitarians?", "He pictures persons as individuals without community ties, whereas real persons belong to communities", [
        ("He ignores liberty completely", "His first principle protects liberty."),
        ("He relies on a veil that gives too much information", "The veil removes information."),
        ("He defends absolute equality of income", "The difference principle allows inequalities.")],
      "Sandel and other communitarians say Rawls's chooser is 'unencumbered' by communal ties.", "Which criticism mentions communities?", "Communitarian critique", "Concept"),
    K("Aristotle's formula that equals should be treated equally and unequals unequally in proportion to relevant difference raises which question?", "On what basis are people relevantly different (merit, need, contribution, birth)?", [
        ("Whether all people are equal in every way", "The formula allows differences; the question is which differences count."),
        ("Whether justice is necessary at all", "The formula assumes justice matters."),
        ("Whether the state should exist", "The formula concerns fair treatment, not the existence of the state.")],
      "The formula is empty until we say which differences are relevant.", "What must be specified in the formula?", "Aristotle on justice", "Reasoning"),
], seed=204)

# ================================================================== 5. The state, law and power
SET(M_MORAL, "The state, law and power", "The state, law and power: obedience and legitimacy", "psu2-state-law-power", [
    K("Which statement best distinguishes authority from power?", "Authority is power accepted as rightful; power is the ability to compel", [
        ("Power is legal and authority is illegal", "Neither word means legal or illegal as such."),
        ("They are two words for the same thing", "A bandit has power without authority."),
        ("Authority needs force; power needs consent", "The reverse is nearer the truth.")],
      "Authority adds legitimacy to power.", "Which word includes the idea of rightful command?", "Power and authority", "Concept"),
    K("Weber's well-known definition describes the state as the body that:", "successfully claims a monopoly of the legitimate use of force in a territory", [
        ("owns all property in a country", "That is not Weber's definition."),
        ("expresses the general will of all", "That is Rousseau's idea of legitimate authority."),
        ("keeps people in a state of nature", "The state of nature is the condition before government.")],
      "Weber: the state claims a monopoly of legitimate force.", "Which two words matter: monopoly and what else?", "Weber's definition of the state", "Recall"),
    K("According to Hobbes, why do people give up their liberty to a sovereign?", "to escape the insecurity of a state of nature, a war of all against all", [
        ("because the sovereign is chosen by God in every case", "Hobbes's argument is about security, not divine choice."),
        ("because the general will requires it", "That is Rousseau's reasoning."),
        ("because property is a natural right", "That is closer to Locke's reasoning.")],
      "Hobbes: without a common power life is insecure, so reason leads to an absolute sovereign.", "What is the alternative to government for Hobbes?", "Hobbes on the state", "Recall"),
    K("Locke differs from Hobbes in holding that a government that violates people's rights:", "may be resisted and replaced", [
        ("must always be obeyed", "That is closer to Hobbes."),
        ("is the same as natural law", "A government that violates rights breaks natural law."),
        ("is protected by the general will", "That is Rousseau's concept, and not Locke's answer here.")],
      "For Locke, government is a trust; if it breaks the trust, the people may replace it.", "Whose view leaves room for resistance?", "Locke on resistance", "Concept"),
    K("A legal positivist would say that a properly enacted law is valid:", "whether or not it is morally just", [
        ("only if it is morally just", "That is the natural-law view."),
        ("only if the majority supports it", "Popularity is not the positivist test."),
        ("only if a priest approves it", "Religious approval is not the test.")],
      "Positivism separates the question of validity from the question of justice.", "Does validity depend on morality in positivism?", "Legal positivism", "Concept"),
    K("A natural-law thinker in the tradition of Aquinas would say that a law commanding grave injustice:", "lacks the full force of law and may be refused", [
        ("is fully binding because it was enacted", "That is the positivist view of validity."),
        ("is binding only if it pleases the majority", "That is not the natural-law test."),
        ("is outside the study of morality", "Natural law is about morality in law.")],
      "Natural law judges human laws by moral principles.", "Which test of law does natural law use?", "Natural law", "Application"),
    K("Rousseau claims that obeying the law can be obeying oneself because:", "the law expresses the general will in which each citizen takes part", [
        ("the sovereign is always wise", "That is not Rousseau's claim."),
        ("law is always just", "He does not say that every law is just."),
        ("citizens fear punishment", "Fear is not the basis of Rousseau's argument.")],
      "Under the general will citizens are both authors and subjects of the law.", "Who makes the law in Rousseau's ideal?", "Rousseau and the general will", "Reasoning"),
    K("The claim that law protects freedom by preventing others from interfering with me is most closely linked with the distinction between:", "negative and positive freedom", [
        ("distributive and corrective justice", "That distinction concerns justice, not freedom."),
        ("act and rule utilitarianism", "That distinction concerns consequences."),
        ("invincible and vincible ignorance", "That distinction concerns knowledge.")],
      "Negative freedom: absence of interference; positive freedom: capacity for self-direction.", "Which pair of words is about two kinds of freedom?", "Law and freedom", "Reasoning"),
], seed=205)

# ================================================================== 6. Human rights, democracy and violence
SET(M_MORAL, "Human rights, democracy and violence", "Rights, democracy and violence: arguments and examples", "psu2-rights-democracy-violence", [
    K("Human rights are said to be universal. This means they:", "belong to every person simply as a human being", [
        ("are granted by each national government", "That would make them dependent on governments."),
        ("apply only to citizens of democratic states", "Universal means for all persons."),
        ("can be removed by a majority vote", "Rights are meant to limit majorities.")],
      "Universal rights belong to all humans, regardless of nationality or status.", "Who has the right according to the idea?", "Universality of rights", "Concept"),
    K("The Universal Declaration of Human Rights was adopted by the United Nations in:", "1948", [
        ("1919", "1919 is the year of the Treaty of Versailles."),
        ("1963", "1963 is associated with the founding of the Organisation of African Unity."),
        ("1981", "1981 is the year of the African Charter on Human and Peoples' Rights.")],
      "The UDHR was adopted in 1948, after the Second World War.", "Think of the years just after the Second World War.", "Universal Declaration of Human Rights", "Recall"),
    K("Cultural relativism about rights says that:", "moral standards belong to cultures, so no culture may impose its rights on another", [
        ("rights are the same in all cultures", "That is universalism."),
        ("rights do not matter to any culture", "Relativism does not say that rights do not matter."),
        ("the state decides what is right in all cases", "That is a different view of authority.")],
      "Relativism ties standards to particular cultures.", "Which word names the unit that decides standards?", "Cultural relativism", "Concept"),
    K("Which describes consensual democracy in the African tradition?", "Decisions are reached by discussion until agreement", [
        ("The winning group takes all decisions", "That is majority rule."),
        ("A single ruler decides", "That is autocracy."),
        ("Decisions are made by a lottery", "That is not consensual democracy.")],
      "Consensual democracy seeks agreement through deliberation.", "What is the end of the discussion?", "Consensus democracy", "Concept"),
    K("One weakness of representative democracy is that:", "a majority may harm a minority unless rights are protected", [
        ("it cannot work in a large state", "It is designed to work in large states."),
        ("it forbids elections", "Elections are central to it."),
        ("it requires everyone to agree", "That describes consensus, not representation.")],
      "Majority tyranny is a standard criticism.", "Whose interests may be overridden?", "Limits of representative democracy", "Reasoning"),
    K("Gandhi's non-violent resistance rests on the idea that:", "means and ends are linked, so violent means damage the justice they aim at", [
        ("violence is always more effective", "He argued the contrary."),
        ("governments cannot be resisted", "He organised resistance."),
        ("law should never be disobeyed", "Civil disobedience was part of his method.")],
      "For Gandhi, the means shape the end.", "Which two words are linked in his argument?", "Non-violence", "Concept"),
    K("A speaker argues: 'If we allow one peaceful protest, soon there will be riots, so ban all protest.' This is weak mainly because it:", "claims an inevitable chain of events without evidence for each step", [
        ("appeals to a respected authority", "No authority is cited."),
        ("uses numbers carelessly", "No figures are given."),
        ("supports non-violence", "The speaker supports a ban on protest, not non-violence.")],
      "This is a slippery slope argument; the chain is asserted, not shown.", "Which link is supported by evidence?", "Slippery slope argument", "Reasoning"),
    K("The 1961 turn of the African National Congress to armed struggle is cited in discussions of violence because it shows that:", "thinkers disagree about whether non-violence is enough when peaceful methods are closed", [
        ("armed struggle was never debated", "It was debated widely."),
        ("non-violence has never succeeded", "Non-violence has succeeded in some campaigns."),
        ("violence is accepted in all circumstances", "The example does not show that.")],
      "The case illustrates the dilemma of last resort.", "Which dilemma does the example raise?", "Violence and last resort", "Application"),
], seed=206)

# ================================================================== 7. Globalization
SET(M_MORAL, "Globalization", "Globalization: dimensions, arguments and justice", "psu2-globalization", [
    K("Globalization is best defined as:", "growing interconnection and interdependence of societies through flows of goods, capital, people, information and culture", [
        ("the end of all national differences", "Globalization does not abolish differences."),
        ("trade between two neighbouring countries", "It is worldwide, not limited to two countries."),
        ("the policy of one powerful state", "It is a process, not one state's policy.")],
      "Globalization means growing worldwide interdependence.", "Which word captures worldwide connection?", "Definition of globalization", "Recall"),
    K("Which are the three dimensions of globalization named in the lesson?", "Economic, political and cultural", [
        ("Military, religious and legal", "These are not the three named dimensions."),
        ("Local, regional and national", "These are levels, not dimensions."),
        ("Past, present and future", "These are times, not dimensions.")],
      "Economic (trade, finance), political (international rules) and cultural (media, language).", "Think of trade, treaties and television.", "Dimensions of globalization", "Recall"),
    K("A cocoa farmer sells to a world market and loses income when the world price falls. This best illustrates the argument that globalization can:", "increase dependence on prices set far away", [
        ("promote cultural exchange", "The example concerns income, not culture."),
        ("spread medical knowledge", "The example is not about medicine."),
        ("strengthen local control of markets", "The example shows less control, not more.")],
      "Dependency arguments stress vulnerability to external prices.", "Who sets the price?", "Dependency", "Application"),
    K("Cosmopolitanism is the view that:", "all human beings belong to one moral community", [
        ("only fellow citizens matter morally", "That is nationalism."),
        ("all cultures should become identical", "Cosmopolitanism does not demand identical cultures."),
        ("trade is always harmful", "That is not a cosmopolitan thesis.")],
      "Cosmopolitanism: citizens of the world.", "What does 'cosmos' suggest?", "Cosmopolitanism", "Concept"),
    K("Which is an argument sometimes given against globalization?", "It may crowd out local languages and customs", [
        ("It allows faster spread of medicines", "That is a benefit."),
        ("It allows cooperation against pandemics", "That is a benefit."),
        ("It allows farmers to reach more buyers", "That is a benefit.")],
      "Cultural homogenisation is a standard criticism.", "Three options are advantages.", "Cultural homogenisation", "Concept"),
    K("Singer's pond argument claims that:", "if we can prevent something very bad at small cost to ourselves, we ought to, even for distant strangers", [
        ("distance weakens every moral duty", "Singer argues that distance does not matter morally."),
        ("charity is never a duty", "Singer says it is a duty."),
        ("only governments have duties", "His argument concerns individuals.")],
      "A drowning child near us and a child far away are morally alike in need.", "What does the pond example compare?", "Duties to distant strangers", "Concept"),
    K("A common objection to Singer's argument is that it:", "is too demanding and ignores special duties to those close to us", [
        ("denies that suffering is bad", "The argument assumes suffering is bad."),
        ("requires everyone to be selfish", "It requires the opposite."),
        ("depends on a particular religion", "It does not.")],
      "Demandingness and special duties are the standard objections.", "Which feature of the demand is criticised?", "Objections to Singer", "Reasoning"),
    K("Rawls's The Law of Peoples proposes between societies:", "a duty of assistance to burdened societies, but not a global difference principle", [
        ("no duties at all", "He proposed a duty of assistance."),
        ("a world state", "He did not propose a world state."),
        ("equal incomes in all countries", "He rejected a global difference principle.")],
      "Rawls limited global justice to a duty of assistance until societies can organise just institutions.", "How wide are the duties he proposes?", "Global justice", "Recall"),
], seed=207)

# ================================================================== 8. The philosophical dissertation
SET(M_METH, "The philosophical dissertation", "The dissertation: problematic, dialectic and conclusion", "psu2-dissertation", [
    K("What is the problematic in the introduction of a dissertation?", "the central difficulty of the question, stated as a question or tension", [
        ("the final answer to the question", "The answer comes later, in the synthesis and conclusion."),
        ("a list of philosophers who wrote on the topic", "A list of names is not a problem."),
        ("a definition of every word in the question", "Definitions concern key concepts; the problematic shows why the question is difficult.")],
      "The problematic sets up the movement of the essay.", "Why would a thoughtful person find the question hard?", "Problematic", "Recall"),
    K("Which sequence gives the five paragraphs in the correct order?", "Introduction, thesis, antithesis, synthesis, conclusion", [
        ("Introduction, antithesis, thesis, conclusion, synthesis", "The thesis comes before the antithesis; the conclusion comes last."),
        ("Thesis, introduction, synthesis, antithesis, conclusion", "The introduction comes first."),
        ("Introduction, thesis, synthesis, antithesis, conclusion", "The synthesis answers both thesis and antithesis, so it follows them.")],
      "The dialectic moves from a first answer to its challenge to a reconciliation.", "Which paragraph answers both earlier ones?", "Structure of the dissertation", "Recall"),
    K("A good antithesis is best described as:", "the strongest objection or rival view to the thesis, ideally showing a weakness inside it", [
        ("a paragraph on another philosopher who says something unrelated", "An antithesis must challenge the thesis."),
        ("a repeat of the thesis in other words", "That adds no challenge."),
        ("the conclusion of the essay", "The conclusion comes after the synthesis.")],
      "The report urges internal critique, which tests a thinker's own premises.", "What must an antithesis do to the thesis?", "Antithesis", "Concept"),
    K("A synthesis is best described as:", "a reasoned position that resolves the tension by a distinction or new condition", [
        ("a summary of everything read", "A synthesis resolves; it does not summarise."),
        ("a new topic unrelated to the question", "It must stay with the problem."),
        ("a copy of the antithesis", "That would abandon the dialectic.")],
      "Synthesis keeps what is sound in both views.", "Think of 'putting together'.", "Synthesis", "Concept"),
    K("Which part belongs to the conclusion?", "Personal judgement and an opening to a further question", [
        ("A new argument not yet discussed", "A conclusion should not add a new argument."),
        ("The definition of the key concepts", "That belongs in the introduction."),
        ("The first topic sentence of the thesis", "That belongs in the thesis paragraph.")],
      "The conclusion recalls, judges and opens.", "What do you give at the end?", "Conclusion", "Recall"),
    K("A candidate answers 'To what extent is X true?' with 'Yes, completely' and no qualification. The main fault is that:", "the phrase asks for a judgement with limits, which the answer does not give", [
        ("the answer is too long", "Length is not the problem."),
        ("the candidate defined too many terms", "Definitions are required, not a fault."),
        ("the candidate quoted a philosopher", "Naming a philosopher is encouraged.")],
      "'To what extent' asks where the claim holds and where it does not.", "What does 'extent' suggest?", "Command words", "Application"),
    K("Why does the Board's report discourage answers that survey whole periods of history instead of arguing about individual thinkers?", "they tend to become narration rather than philosophising", [
        ("because history is not part of philosophy at all", "The report does not say that; it says narration replaces argument."),
        ("because examiners dislike long answers", "Length is not the issue."),
        ("because broad questions are never set", "The report discusses the broad questions that were set.")],
      "The report says broad questions invite narration and suggests focusing on individual philosophers.", "What do candidates do with broad questions?", "Avoiding narration", "Reasoning"),
    K("For the question 'Is it ever right to disobey the law?', which is the best synthesis?", "Civil disobedience, public and non-violent, may be justified against grave injustice after legal remedies have failed", [
        ("Everyone must always obey the law", "That repeats the thesis (obey)."),
        ("Everyone may break any law they dislike", "That drops the thesis and loses the case for order."),
        ("Laws are written by humans", "That is background, not a resolution.")],
      "The synthesis distinguishes conditions under which disobedience is justified.", "Which option reconciles obedience and conscience?", "Writing a synthesis", "Application"),
], seed=208)

# ================================================================== 9. The commentary on a philosophical text
SET(M_METH, "The commentary on a philosophical text", "The commentary: theme, thesis, structure and critique", "psu2-commentary", [
    K("Read this invented passage. 'A person who never says no is not polite; he is only afraid. Politeness is a choice made among options, and a person who has no option to refuse has no chance to be polite. Therefore children must be allowed to refuse, so that when they agree their agreement means something.' Its theme is:", "politeness, choice and refusal", [
        ("the history of schools", "The passage does not discuss school history."),
        ("the nature of fear in animals", "Fear appears only as a contrast."),
        ("the rules of grammar", "The passage is not about grammar.")],
      "The theme is the general subject: politeness, choice and refusal.", "What is the passage about in general?", "Identifying the theme", "Interpretation"),
    K("The thesis of the same passage is best stated as:", "real politeness requires the freedom to refuse, so children should be allowed to say no", [
        ("fear is an interesting emotion", "That is not the author's claim."),
        ("children should never obey", "The passage does not say that."),
        ("politeness is the same as obedience", "The author denies this.")],
      "The thesis is the author's answer to the problem: politeness needs choice.", "What does the 'therefore' sentence conclude?", "Identifying the thesis", "Interpretation"),
    K("In the same passage, which word signals the conclusion of the argument?", "Therefore", [
        ("Not", "'Not' is a negation, not a signal of conclusion."),
        ("Only", "'Only' limits a claim; it does not mark a conclusion."),
        ("Among", "'Among' relates options; it does not mark a conclusion.")],
      "Connectives such as 'therefore' show the movement of reasoning.", "Which word introduces what follows from the reasons?", "Logical connectives", "Interpretation"),
    K("Which is the correct order of the steps of a commentary?", "Situate, theme, problem, thesis, structure, critique and judgement", [
        ("Thesis, theme, critique, structure, situate, problem", "The order goes from situating to judging."),
        ("Critique, situate, theme, thesis, problem, structure", "Critique comes after the text has been understood."),
        ("Problem, judgement, theme, situate, thesis, structure", "Judgement comes last.")],
      "Read, understand, reconstruct, then criticise.", "Which step comes last?", "Steps of the commentary", "Recall"),
    K("An internal critique of a text examines:", "consistency, validity, hidden assumptions and the strength of examples inside the text", [
        ("only what other philosophers have said", "That is external critique."),
        ("the author's personal life", "That is not a philosophical critique of the argument."),
        ("whether the text is long enough", "Length is not the point.")],
      "Internal critique tests the argument on its own terms.", "Which critique stays inside the text?", "Internal critique", "Concept"),
    K("A weakness of the stone analogy in Passage A of the lesson ('moved from outside as a stone is moved by a hand') is that:", "a frightened person still chooses to comply, whereas a stone does not choose", [
        ("stones cannot be moved", "Stones can be moved; that is the analogy's point."),
        ("analogies are never allowed in philosophy", "Analogies are allowed; they can be assessed."),
        ("the passage mentions a school", "That is not a weakness of the analogy.")],
      "The analogy exaggerates by ignoring the agent's choice.", "Who makes a choice in each half of the analogy?", "Evaluating an analogy", "Reasoning"),
    K("Which sentence is a good external critique of Passage A (obedience without questioning makes only subjects)?", "Hobbes would reply that order depends on obedience, so constant questioning may threaten peace", [
        ("The passage has seven lines", "That says nothing about the argument."),
        ("The author uses the word 'stone'", "That is an observation, not a critique."),
        ("The passage is written in prose", "That is not a critique.")],
      "External critique brings another thinker's view to bear.", "Which option uses a rival view?", "External critique", "Application"),
    K("A common fault in a commentary is:", "paraphrasing the text line by line instead of reconstructing its argument", [
        ("giving the thesis in one sentence", "A clear thesis sentence is good."),
        ("referring to lines of the text", "Anchoring points in lines is recommended."),
        ("giving a personal judgement at the end", "A judgement is expected.")],
      "A commentary groups lines into parts and explains the movement of thought.", "What does a paraphrase fail to show?", "Faults in a commentary", "Recall"),
], seed=209)

# ================================================================== 10. Paper 1 strategy
SET(M_EXAM, "Paper 1", "Paper 1 strategy: reading stems and eliminating options", "psu2-paper-1-strategy", [
    K("According to the Board's 2023 report, Paper 1 covered:", "the entire syllabus", [
        ("only the Lower Sixth modules", "The report says the whole syllabus was covered."),
        ("only African philosophy", "The paper is not limited to one module."),
        ("only logic", "Logic is part of a wider paper.")],
      "The report says Paper 1 covered the whole syllabus (50 multiple-choice questions).", "Which option mentions every module?", "Paper 1 coverage", "Recall"),
    K("You see the stem 'Which of the following is MOST clearly a hypothetical imperative?' What should you do first?", "Underline 'most clearly' and recall the definition: a command that depends on a wish", [
        ("Choose the longest option", "Length is not a reason."),
        ("Choose the option with a philosopher's name", "A name does not make it correct."),
        ("Skip the paper", "That is not an option.")],
      "Read the command word and the concept before looking at the options.", "What does the stem require?", "Reading the stem", "Application"),
    K("Which kind of wrong option is a true statement that does not answer the question?", "The true-but-irrelevant option", [
        ("The neighbour", "A neighbour names a close but different concept or thinker."),
        ("The extreme", "An extreme overstates with 'always' or 'never'."),
        ("The half-true option", "A half-true option is partly false.")],
      "A true statement can still be wrong for this stem.", "What does the option say compared with what is asked?", "Distractor types", "Concept"),
    K("Why does the report advise preparing individual philosophers rather than groups?", "a question about one thinker may not be answered by a statement true of a whole school", [
        ("because groups of thinkers never share any ideas", "Groups can share ideas; the point is precision."),
        ("because examiners dislike names of schools", "The advice concerns precision, not likes."),
        ("because only individual thinkers appear in logic", "Logic questions are about terms and rules.")],
      "Statements true of a school may not hold for the named individual.", "Think of the difference between a school and one thinker.", "Individual philosophers", "Reasoning"),
    K("If you can eliminate one of four options, your chance of choosing correctly by guessing among the rest is:", "one in three", [
        ("one in four", "That is the chance with no elimination."),
        ("one in two", "That would require eliminating two options."),
        ("certain", "Elimination does not make the answer certain.")],
      "Three options remain, so the chance is 1/3.", "Count the remaining options.", "Guessing and elimination", "Calculation"),
    K("From 'All S are P' the inference 'All non-P are non-S' is called:", "contraposition", [
        ("obversion", "Obversion would give 'No S are non-P'."),
        ("conversion", "Conversion would give 'Some P are S'."),
        ("subalternation", "Subalternation would give 'Some S are P'.")],
      "Contraposition replaces each term by its complement and swaps them.", "Which immediate inference uses complements of both terms?", "Immediate inferences", "Recall"),
    K("A stem reads: 'Which philosopher defended entitlement theory of justice?' Options: Rawls, Aristotle, Nozick, Bentham. Which kind of wrong option is 'Rawls'?", "The neighbour: a close thinker in the same debate", [
        ("The extreme", "It does not use absolute words."),
        ("The true-but-irrelevant option", "It names a thinker; it is not a general true statement."),
        ("The half-true option", "It has no true and false halves.")],
      "Rawls is the thinker most often set against Nozick: a neighbour.", "Which thinker is in the same debate?", "Distractor types", "Analysis"),
    K("Which revision plan best fits a paper that covers the whole syllabus?", "A one-page sheet for each module, with terms, thinkers and objections, plus regular logic practice", [
        ("Study only the modules you like", "The report warns against skipping areas of the syllabus."),
        ("Study only logic", "The paper covers every module."),
        ("Memorise past answers", "Understanding of terms is needed.")],
      "Module-by-module revision matches whole-syllabus coverage.", "Which plan leaves no module out?", "Revision planning", "Application"),
], seed=210)

# ================================================================== 11. Paper 2 strategy
SET(M_EXAM, "Paper 2", "Paper 2 strategy: intent, five paragraphs and faults", "psu2-paper-2-strategy", [
    K("The Board's 2023 report describes Paper 2 as having which three sections?", "Western philosophy, African philosophy and textual analysis", [
        ("Logic, ethics and aesthetics", "Logic is mainly in Paper 3."),
        ("Ancient, medieval and modern philosophy", "These are periods, not sections."),
        ("Epistemology, metaphysics and politics", "These are branches, not the sections named.")],
      "The report lists Section 1 Western philosophy, Section 2 African philosophy, Section 3 textual analysis.", "Which sections include a text?", "Sections of Paper 2", "Recall"),
    K("In a question on Tempels's vital force, a candidate writes mostly about whether witchcraft exists. The main fault is:", "failing to answer the intent of the question", [
        ("writing too many paragraphs", "The number of paragraphs is not the fault."),
        ("using a philosopher's name", "Names are welcome."),
        ("defining terms", "Definitions are required.")],
      "The report describes this exact fault: the question was about the vital force.", "What was the question really about?", "Answering the intent", "Application"),
    K("In the Board's marking criteria, which paragraphs are each credited for a topic statement, explanation, justification, reference or example, and clincher?", "Thesis, antithesis and synthesis", [
        ("Introduction and conclusion", "These have different components."),
        ("Only the thesis", "The same parts are credited in the antithesis and synthesis."),
        ("Only the conclusion", "The conclusion has recall, judgement and opening.")],
      "The three body paragraphs share the same set of parts.", "Which paragraphs argue?", "Marking criteria", "Recall"),
    K("The marking criteria describe the answer as five paragraphs. At most about how long is each paragraph?", "ten lines", [
        ("three lines", "That is too short."),
        ("thirty lines", "The paper allows two pages for the whole essay."),
        ("one page", "The whole essay is limited to two pages.")],
      "Each paragraph has a maximum of about ten lines (two pages in all).", "Five paragraphs fit in two pages.", "Length of paragraphs", "Recall"),
    K("The report advises giving priority to which kind of criticism of a philosopher?", "Internal criticism, testing the thinker's own premises", [
        ("Only criticism by modern authors", "Internal criticism is preferred, not only modern."),
        ("Only praise", "A critique is expected."),
        ("Only a list of names", "A list of names is not critical thinking.")],
      "The report emphasises internal critique over external critique alone.", "Which critique uses the thinker's own premises?", "Internal critique", "Concept"),
    K("A question asks: 'To what extent can African philosophy be called communal?' Which plan fits best?", "Thesis: ethnophilosophy as communal thought; antithesis: critical individual works; synthesis: both communal sources and individual critical work", [
        ("A history of all African philosophers in order", "That is narration, not an argument."),
        ("A single paragraph saying yes", "The question asks 'to what extent', so a judgement with limits."),
        ("A list of Western philosophers", "The question concerns African philosophy.")],
      "A dialectical plan answers 'to what extent'.", "Which plan has thesis, antithesis and synthesis?", "Essay planning", "Application"),
    K("What does the report say about the text questions in the textual analysis section?", "Sub-questions could serve as clues, so use them to shape the answer", [
        ("They are always unanswerable", "The report says the texts were within reach."),
        ("They need no method", "The report asks for strict methodology."),
        ("They should be answered in French only", "The report does not say that.")],
      "The report says questions c, d and e served as clues.", "Which feature of the questions helps the candidate?", "Textual analysis", "Recall"),
    K("A candidate leaves out the antithesis paragraph to finish on time. The most likely result is:", "loss of the marks credited to that paragraph and a weaker argument", [
        ("no effect, since the thesis carries all marks", "Each paragraph carries credited marks."),
        ("extra marks for brevity", "Brevity is not rewarded."),
        ("automatic failure of the paper", "The result is loss of marks for the paragraph, not automatic failure.")],
      "Marks are given paragraph by paragraph, item by item.", "How is credit awarded?", "Time management", "Reasoning"),
], seed=211)

# ================================================================== 12. Paper 3 strategy
SET(M_EXAM, "Paper 3", "Paper 3 strategy: logic steps and symbolisation", "psu2-paper-3-strategy", [
    K("The report advises that symbolisation should begin with:", "paraphrase or analysis in ordinary language, then building up in symbols", [
        ("writing the final formula at once", "The report says to analyse first."),
        ("drawing a truth table", "A truth table is for testing formulas, not for first steps in symbolising."),
        ("naming a philosopher", "Names are not part of symbolisation.")],
      "Paraphrase first, then build up in the object-language.", "What does the report say comes first?", "Symbolisation method", "Recall"),
    K("The syllogism 'All farmers are traders; all traders are taxpayers; so all taxpayers are farmers' is in:", "figure 4 and mood AAA", [
        ("figure 1 and mood AAA", "In figure 1 the middle term is subject of the major premise and predicate of the minor."),
        ("figure 2 and mood EIO", "All three statements are A statements."),
        ("figure 3 and mood IAI", "All three statements are A statements.")],
      "Major premise P-M (farmers-traders), minor premise M-S (traders-taxpayers): figure 4; all A.", "Where does the middle term 'traders' stand in each premise?", "Figure and mood", "Application"),
    K("The same syllogism is invalid. The fallacy is:", "illicit minor", [
        ("undistributed middle", "The middle 'traders' is distributed in the minor premise."),
        ("illicit major", "The major term 'farmers' is not distributed in the conclusion."),
        ("exclusive premises", "No premise is negative.")],
      "'Taxpayers' is distributed in the conclusion (subject of an A) but not in the minor premise (predicate of an A).", "Which term is distributed in the conclusion but not in its premise?", "Illicit minor", "Reasoning"),
    K("How many rows of the truth table for (p ⊃ q) · (q ⊃ r) are true?", "4", [
        ("2", "Two true rows is the count for the biconditional (p ⊃ q) · (q ⊃ p); this formula has three variables."),
        ("3", "Count carefully each of the eight rows."),
        ("8", "Not every row is true; for instance p true, q false makes the first conjunct false.")],
      "Rows of (p, q, r) where both conditionals hold: TTT, FTT, FFT, FFF: four.", "List the eight rows and test both conditionals.", "Truth table rows", "Calculation"),
    K("The argument 'p ⊃ q; q; therefore p' is:", "invalid, shown by p false and q true", [
        ("valid, by modus ponens", "Modus ponens needs p, not q, as the second premise."),
        ("valid, by modus tollens", "Modus tollens needs ~q."),
        ("valid, because the premises are true", "Validity depends on the form, not on actual truth.")],
      "In row p false, q true both premises are true and the conclusion is false.", "Look for a row with true premises and a false conclusion.", "Validity of an argument", "Reasoning"),
    K("'Only graduates are eligible' (Ex: x is eligible; Gx: x is a graduate) is symbolised:", "(x)(Ex ⊃ Gx)", [
        ("(x)(Gx ⊃ Ex)", "That says all graduates are eligible."),
        ("(∃x)(Gx · Ex)", "That says some graduates are eligible."),
        ("(x)(Ex · Gx)", "That says everything is eligible and a graduate.")],
      "Paraphrase: for anything, if it is eligible then it is a graduate.", "Which property must everything eligible have?", "Quantifier symbolisation", "Application"),
    K("~(p · q) is equivalent to:", "~p ∨ ~q", [
        ("~p · ~q", "That is the negation of a disjunction, ~(p ∨ q)."),
        ("p ∨ q", "That is not equivalent."),
        ("~p ⊃ q", "That is p ∨ q.")],
      "De Morgan's law: the negation of a conjunction is the disjunction of the negations.", "Test the four rows.", "De Morgan's law", "Recall"),
    K("The report says that in a question on a fallacy candidates should:", "explain the fallacy in the context of the given argument, not in generalities", [
        ("give only the name of the fallacy", "The report asks for explanation in context."),
        ("ignore the argument", "The argument is the evidence."),
        ("write a history of logic", "That is irrelevant.")],
      "Name the fallacy and show where in the argument it occurs.", "What does 'in context' mean?", "Explaining fallacies", "Application"),
], seed=212)

# ================================================================== Paper 1 mock exam A (50 questions: two per Upper Sixth topic)
P1 = []


def Q(prompt, right, wrongs, step, hint, concept, skill="Concept"):
    P1.append(K(prompt, right, wrongs, step, hint, concept, skill))


# ---- African Philosophy
Q("The debate on African philosophy asks mainly whether:", "there is African thought that counts as philosophy in the strict, critical sense", [
    ("Africans can learn Western philosophy", "The debate is about the existence and nature of African philosophy, not about ability to learn."),
    ("philosophy began in Africa", "That is a different question."),
    ("African languages have grammar", "Not the subject of the debate.")],
  "The debate concerns the existence, nature and method of African philosophy.", "What is being disputed?", "The debate on African philosophy")
Q("The 'myth of unanimity' criticises the assumption that:", "all members of an African community think alike", [
    ("all philosophers agree on logic", "The phrase refers to communal thought, not to logic."),
    ("Africa has one language", "It is not about language."),
    ("all trends of African philosophy are equal", "It is about agreement within communities.")],
  "Critics of ethnophilosophy say that it assumes unanimous thought in a community.", "Who is assumed to agree?", "The debate on African philosophy")
Q("Which of these is NOT one of Odera Oruka's four trends of African philosophy?", "Scientific materialism", [
    ("Ethnophilosophy", "This is the first trend."),
    ("Philosophic sagacity", "This is Oruka's own trend."),
    ("Professional philosophy", "This is the fourth trend.")],
  "The four trends: ethnophilosophy, philosophic sagacity, nationalist-ideological and professional philosophy.", "Which name is not on the list?", "Odera Oruka's four trends")
Q("The philosophic sage, in Oruka's account, is a sage who:", "goes beyond communal wisdom and gives individual, critical thought", [
    ("only repeats the community's proverbs", "That describes the folk sage."),
    ("holds political office", "The distinction is not about office."),
    ("writes in a foreign language", "The distinction is not about language.")],
  "A folk sage embodies communal wisdom; a philosophic sage reasons critically.", "Which sage thinks critically?", "Odera Oruka's four trends")
Q("Tempels' 'vital force' refers to:", "a force animating all beings, flowing in a hierarchy from God to ancestors, humans and nature", [
    ("the physical strength of warriors", "It is a metaphysical idea of being, not physical strength."),
    ("the power of the state", "It is not political power."),
    ("a theory of witchcraft", "Candidates were reminded that the question concerned the force, not witchcraft.")],
  "In Tempels' account being is force; all beings participate in a hierarchy of vital force.", "What does 'force' mean for being?", "Ethnophilosophy: Tempels and Mbiti")
Q("Mbiti's terms Sasa and Zamani belong to his account of:", "the African concept of time", [
    ("the African concept of the state", "They are not political terms."),
    ("the vital force", "That is Tempels' idea."),
    ("the African economy", "They are not economic terms.")],
  "Sasa is the near present and recent past; Zamani is the long past.", "Which idea do these two words organise?", "Ethnophilosophy: Tempels and Mbiti")
Q("Nkrumah's Consciencism is best described as:", "an attempt to build a philosophical basis for African liberation and unity", [
    ("a study of the vital force", "That is Tempels."),
    ("a defence of Negritude by Senghor", "Negritude is Senghor's theme."),
    ("a book on formal logic", "It is not a logic text.")],
  "Nkrumah linked philosophy to ideology for decolonisation and unity.", "Which trend does it belong to?", "Nationalist-ideological philosophy")
Q("Ujamaa, the idea of familyhood, is associated with:", "Julius Nyerere", [
    ("Leopold Senghor", "Senghor is associated with Negritude."),
    ("Paulin Hountondji", "Hountondji is a critic of ethnophilosophy."),
    ("John Mbiti", "Mbiti is associated with religion and time.")],
  "Ujamaa was Nyerere's idea of African socialism based on community.", "Which leader is linked to Tanzania's approach?", "Nationalist-ideological philosophy")
Q("Marcien Towa is known in African philosophy as:", "a Cameroonian critic of ethnophilosophy who helped to found the professional trend", [
    ("the author of Bantu Philosophy", "That is Tempels."),
    ("the founder of Negritude", "That is Senghor with Cesaire and Damas."),
    ("a theorist of vital force", "That is Tempels.")],
  "Towa criticised ethnophilosophy and argued for critical, rigorous African philosophy.", "Which trend criticises ethnophilosophy?", "Professional philosophy")
Q("A mark of the professional trend of African philosophy is:", "critical, argued, individual philosophical work", [
    ("the recording of community beliefs without criticism", "That describes ethnophilosophy."),
    ("a political programme for independence", "That describes nationalist-ideological work."),
    ("sayings of folk sages", "That describes the first kind of sage philosophy.")],
  "Hountondji and Towa argued that philosophy needs critical individual reasoning in writing.", "Which feature is critical and individual?", "Professional philosophy")

# ---- 19th & 20th Century Contemporary Philosophy
Q("In Hegel's dialectic, Aufhebung means:", "cancelling, preserving and lifting to a higher level", [
    ("simply destroying the opposite", "It also preserves."),
    ("returning to the starting point", "It moves to a higher level."),
    ("choosing one side", "It combines in a higher unity.")],
  "Aufhebung (sublation) cancels, keeps and raises.", "Which word has three senses?", "Hegel")
Q("For Hegel, history is best understood as:", "the development of Spirit towards the realisation of freedom", [
    ("a random sequence of events", "Hegel saw rational development."),
    ("the struggle of economic classes", "That is Marx's reading."),
    ("a return of the same events", "That is closer to eternal recurrence, which is Nietzsche's.")],
  "History expresses the growth of freedom in Spirit.", "Which concept does Hegel link to history?", "Hegel")
Q("In Marx's base and superstructure model, the base is:", "the economic relations and forces of production", [
    ("law, politics and religion", "These form the superstructure."),
    ("the ideas of the ruling class", "Ideology belongs to the superstructure."),
    ("the state of nature", "That is a contract theory idea.")],
  "The economic base shapes the legal, political and cultural superstructure.", "Which part is economic?", "Marx")
Q("Which is NOT one of the four forms of alienation in Marx's early writings?", "Alienation from God", [
    ("Alienation from the product of labour", "This is the first form."),
    ("Alienation from species-being", "This is the third form."),
    ("Alienation from other people", "This is the fourth form.")],
  "The four are product, activity, species-being and other people.", "Which relation is not economic or social?", "Marx")
Q("Nietzsche's phrase about the 'death of God' mainly means that:", "belief in God has lost its hold on European culture, creating a risk of nihilism", [
    ("a god physically died", "It is a cultural diagnosis."),
    ("science proved God exists", "It does not mean that."),
    ("religion became compulsory", "It means the reverse.")],
  "The phrase is a diagnosis of cultural change and its risk of nihilism.", "Is it a claim about a being or about belief?", "Nietzsche")
Q("The 'overman' in Nietzsche refers to:", "a type of person who creates new values after traditional values lose force", [
    ("a ruler of a state", "It is not a political office."),
    ("an ancestor in tradition", "It is not about ancestors."),
    ("a scientist", "It is not about a profession.")],
  "The overman creates values and affirms life.", "What does the overman do with values?", "Nietzsche")
Q("In Freud's model, the superego is:", "the part of the mind linked to conscience and internalised norms", [
    ("the source of instinctive drives", "That is the id."),
    ("the part that mediates with reality", "That is the ego."),
    ("the conscious memory", "It is not simply conscious memory.")],
  "Id: drives; ego: reality; superego: norms and conscience.", "Which part of the mind is linked to conscience?", "Freud")
Q("In Freud's theory, repression is:", "pushing unacceptable wishes out of awareness into the unconscious", [
    ("deliberately remembering a wish", "That is the opposite."),
    ("expressing every drive", "That is not repression."),
    ("the use of logic in thought", "That is not repression.")],
  "Repression keeps unacceptable material out of conscious awareness.", "Where do repressed wishes go?", "Freud")
Q("In Husserl's phenomenology, 'intentionality' means that:", "consciousness is always consciousness of something", [
    ("every act is planned in advance", "It is not about planning."),
    ("only physical objects exist", "It is not a materialist claim."),
    ("knowledge is impossible", "It is not scepticism.")],
  "Intentionality is the directedness of consciousness.", "What is consciousness always directed at?", "Husserl's phenomenology")
Q("The epoche in Husserl is:", "suspending judgement about the existence of the world in order to describe experience as it appears", [
    ("proving that the world does not exist", "It suspends judgement; it does not deny."),
    ("measuring experience scientifically", "It is a philosophical method, not measurement."),
    ("a Hegelian dialectic", "It is Husserl's own method.")],
  "The epoche 'brackets' assumptions about the world.", "Does it deny the world or suspend judgement?", "Husserl's phenomenology")
Q("Sartre's slogan that existence precedes essence means that:", "a human being first exists and then defines what he or she is by choices", [
    ("humans are born with a fixed nature", "That is the view he opposes."),
    ("essence is more real than existence", "It states the opposite order."),
    ("nothing exists", "It is not nihilism about existence.")],
  "There is no fixed human nature; we make ourselves.", "Which comes first?", "Existentialism")
Q("In existentialism, 'bad faith' is:", "self-deception in which a person denies their own freedom", [
    ("loss of religious belief", "It is not about religion."),
    ("a legal offence", "It is a philosophical term."),
    ("a kind of fate", "It is a form of self-deception, not fate.")],
  "In Sartre, bad faith is the flight from freedom and responsibility.", "What does the person deny?", "Existentialism")

# ---- Epistemology & Philosophy of Science
Q("The traditional analysis of knowledge says that knowledge is:", "justified true belief", [
    ("true belief only", "A lucky guess could then count as knowledge."),
    ("justified belief only", "A justified belief may be false."),
    ("certain feeling", "Feeling is not the analysis.")],
  "Knowledge = belief + truth + justification.", "Which three conditions are listed?", "Knowledge, truth and justification")
Q("Gettier cases were designed to show that:", "justified true belief is not sufficient for knowledge", [
    ("beliefs need not be true", "They test the sufficiency of the three conditions."),
    ("knowledge is impossible", "They are not sceptical."),
    ("truth is a matter of opinion", "They do not argue that.")],
  "A belief can be justified and true by luck without being knowledge.", "What is shown about the three conditions?", "Knowledge, truth and justification")
Q("Induction is reasoning:", "from observed cases to a general conclusion that goes beyond them", [
    ("from general premises to a certain conclusion", "That is deduction."),
    ("from authority to conclusion", "Authority is not induction."),
    ("from a definition to a feeling", "Not induction.")],
  "Induction generalises from cases.", "In which direction does the reasoning go?", "The scientific method and induction")
Q("Hume's problem of induction is that:", "we cannot give a non-circular justification for assuming that the future will resemble the past", [
    ("science never uses observation", "Science uses observation."),
    ("all inductions are certain", "The problem is the opposite."),
    ("deduction is invalid", "The problem concerns induction.")],
  "Justifying induction by past success uses induction itself.", "What assumption lies behind induction?", "The scientific method and induction")
Q("For Popper, what makes a theory scientific is that it is:", "falsifiable: it forbids some possible observations", [
    ("proved true by repeated observation", "Popper rejected confirmation as the mark."),
    ("accepted by most scientists", "Popular acceptance is not the criterion."),
    ("written in mathematics", "Mathematical form is not the criterion.")],
  "Popper's demarcation criterion is falsifiability.", "Which word is Popper's key term?", "Bachelard, Popper and Kuhn")
Q("In Kuhn's account, a scientific revolution occurs when:", "anomalies accumulate and a new paradigm replaces the old one", [
    ("scientists agree to stop research", "That is not Kuhn's account."),
    ("one experiment refutes a theory permanently", "Kuhn rejects a purely simple falsification picture."),
    ("the government changes policy", "It is not political.")],
  "Normal science, crisis and revolution replace paradigms.", "What replaces what?", "Bachelard, Popper and Kuhn")
Q("Platonism in the philosophy of mathematics holds that:", "mathematical objects exist independently of human minds", [
    ("mathematics is a game with symbols", "That is formalism."),
    ("mathematics is a mental construction", "That is intuitionism."),
    ("mathematics comes only from experience", "That is empiricism.")],
  "Platonists treat mathematical truths as discovered.", "Do the objects depend on minds?", "The philosophy of mathematics")
Q("Godel's incompleteness theorems show, roughly, that:", "a consistent formal system strong enough for arithmetic contains true statements it cannot prove", [
    ("mathematics is inconsistent", "They do not show that."),
    ("arithmetic cannot be used", "Arithmetic remains usable."),
    ("every statement can be proved", "They show the opposite.")],
  "Any such consistent system is incomplete.", "What is left unprovable?", "The philosophy of mathematics")
Q("Vitalism is the view that:", "living things contain a special life force not reducible to physics and chemistry", [
    ("life is explained only by machines", "That is mechanism."),
    ("species never change", "It is not about species."),
    ("all medicine is harmful", "Not vitalism.")],
  "Vitalism posits a special vital principle.", "Which view opposes mechanism?", "Philosophy of biology and bioethics")
Q("A doctor who explains a treatment and respects a patient's free decision is respecting the bioethical principle of:", "autonomy", [
    ("non-maleficence", "That principle is about avoiding harm."),
    ("beneficence", "That principle is about doing good."),
    ("justice", "That principle is about fair distribution.")],
  "Autonomy is respect for a person's informed choice.", "Which principle is about self-governance?", "Philosophy of biology and bioethics")

# ---- Moral, Social & Political Philosophy
Q("Libertarianism about free will holds that:", "we are free, so determinism is false for human choice", [
    ("determinism is true and we are free anyway", "That is compatibilism."),
    ("we are not free because determinism is true", "That is hard determinism."),
    ("outcomes are fixed whatever we choose", "That is fatalism.")],
  "Libertarians deny determinism for choice.", "What do they say about determinism?", "Freedom and determinism")
Q("Which philosophers are classical compatibilists?", "Hobbes and Hume", [
    ("Spinoza and Sartre", "Spinoza is usually read as a determinist; Sartre defends radical freedom."),
    ("Kant and Rousseau", "These are not classed as the classical compatibilists."),
    ("Plato and Aristotle", "They are not the classical compatibilist pair.")],
  "Hobbes and Hume define freedom as absence of constraint.", "Which pair define freedom as acting on one's own reasons?", "Freedom and determinism")
Q("A categorical imperative differs from a hypothetical imperative in that it:", "commands without depending on any wish", [
    ("depends on what one wants", "That describes a hypothetical imperative."),
    ("is a rule of grammar", "It is a moral command."),
    ("is based on happiness", "Happiness is a hypothetical ground.")],
  "Kant's moral law binds regardless of wishes.", "Which imperative has no 'if'?", "Conscience and duty")
Q("Ignorance that a careful person could not have overcome is called:", "invincible ignorance", [
    ("vincible ignorance", "Vincible ignorance could have been overcome."),
    ("antecedent will", "Not a term for this."),
    ("prima facie duty", "A prima facie duty is a type of duty.")],
  "Invincible ignorance excuses; vincible ignorance excuses little.", "Could it have been overcome?", "Conscience and duty")
Q("Who developed the calculus of pleasure with seven features such as intensity and duration?", "Jeremy Bentham", [
    ("John Stuart Mill", "Mill added quality of pleasures."),
    ("Immanuel Kant", "Kant defended duty ethics."),
    ("John Rawls", "Rawls developed the theory of justice as fairness.")],
  "Bentham's calculus measures pleasures by seven features.", "Which philosopher is the founder?", "Utilitarianism")
Q("Mill's distinction between higher and lower pleasures concerns:", "the quality of pleasures", [
    ("the number of people affected", "That is extent."),
    ("the time of day", "Not relevant."),
    ("the cost of pleasures", "Not relevant.")],
  "Mill said pleasures of the mind are of higher quality.", "What does 'higher' refer to?", "Utilitarianism")
Q("The veil of ignorance is a device in the theory of:", "John Rawls", [
    ("Robert Nozick", "Nozick defended entitlement."),
    ("Jeremy Bentham", "Bentham defended utility."),
    ("Thomas Hobbes", "Hobbes used the state of nature.")],
  "Rawls uses the veil in the original position.", "Which writer's two principles are chosen behind it?", "Justice")
Q("Nozick argued that justice in holdings depends on:", "how the holdings were acquired and transferred", [
    ("whether the distribution is equal", "That is a pattern view he rejects."),
    ("the greatest happiness", "That is utilitarian."),
    ("the difference principle", "That is Rawls.")],
  "Entitlement theory looks at history, not pattern.", "What is decisive in Nozick's view?", "Justice")
Q("Weber's definition of the state stresses:", "a successful claim to the monopoly of legitimate force in a territory", [
    ("the ownership of all land", "Not Weber's definition."),
    ("the rule of the wealthy", "Not Weber's definition."),
    ("equal incomes", "Not Weber's definition.")],
  "Weber: monopoly of legitimate force.", "Which two words describe the force?", "The state, law and power")
Q("Natural law differs from legal positivism in holding that:", "a law must meet moral principles to have full authority", [
    ("a law is valid if properly enacted, whatever its content", "That is positivism."),
    ("law depends on majority opinion", "Not a natural-law claim."),
    ("law has no connection with force", "Not a natural-law claim.")],
  "Natural law ties law to morality.", "Which theory tests laws morally?", "The state, law and power")
Q("The Universal Declaration of Human Rights was adopted by the United Nations in:", "1948", [
    ("1919", "That is the year of the Treaty of Versailles."),
    ("1963", "That is associated with the founding of the OAU."),
    ("1981", "That is associated with the African Charter.")],
  "The UDHR was adopted in 1948.", "Which year follows the Second World War?", "Human rights, democracy and violence")
Q("The slippery slope argument against violence is weak because it:", "asserts an inevitable chain of events without showing each link", [
    ("uses religious authority", "Not the reason."),
    ("is based on exact figures", "Not the reason."),
    ("supports violence", "It argues against violence.")],
  "It predicts a disastrous series without evidence for each step.", "What is missing from the chain?", "Human rights, democracy and violence")
Q("Cosmopolitanism holds that:", "all human beings belong to one moral community", [
    ("only citizens of one nation matter morally", "That is nationalism."),
    ("cultures must be identical", "Not the thesis."),
    ("trade is always harmful", "Not the thesis.")],
  "The word means citizen of the world.", "What kind of community does it describe?", "Globalization")
Q("Which is an argument sometimes given against globalization?", "It may keep poorer countries dependent on exports of raw materials", [
    ("It spreads medical knowledge", "That is a benefit."),
    ("It enables cooperation on pandemics", "That is a benefit."),
    ("It allows cultural exchange", "That is a benefit.")],
  "Dependency theorists stress unequal trade.", "Three options are benefits.", "Globalization")

# ---- Philosophical Methodology: Paper 3 Mastery
Q("Which is the correct order of paragraphs in the philosophical dissertation?", "Introduction, thesis, antithesis, synthesis, conclusion", [
    ("Introduction, antithesis, thesis, synthesis, conclusion", "The thesis comes first."),
    ("Thesis, introduction, antithesis, conclusion, synthesis", "The introduction comes first."),
    ("Introduction, thesis, conclusion, antithesis, synthesis", "The conclusion comes last.")],
  "The dialectic runs from thesis to antithesis to synthesis.", "Which paragraph comes last?", "The philosophical dissertation")
Q("The problematic in the introduction of a dissertation is:", "the central difficulty of the question put as a question or tension", [
    ("the final answer", "The answer comes later."),
    ("a list of philosophers", "A list is not a problem."),
    ("a quotation", "Not required.")],
  "It shows why the question is hard.", "Is it an answer or a question?", "The philosophical dissertation")
Q("The first step in a commentary on a philosophical text is to:", "situate the text and its type", [
    ("write a personal judgement", "That is the last step."),
    ("give an external critique", "That comes after the structure."),
    ("copy the passage", "Copying is not a step.")],
  "A commentary begins by situating, then theme, problem, thesis, structure and critique.", "Which step comes first?", "The commentary on a philosophical text")
Q("An internal critique of a text examines:", "the consistency and strength of the reasoning inside the text", [
    ("only what rival philosophers have said", "That is external critique."),
    ("the length of the text", "Not a philosophical critique."),
    ("the author's biography only", "Not a critique of the argument.")],
  "Internal critique tests the argument on its own terms.", "Which critique stays inside the text?", "The commentary on a philosophical text")

assert len(P1) == 50, len(P1)
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="psu2-paper-1-strategy",
                         mock=True, time_limit_minutes=90, questions=build(P1, 301)))

# ================================================================== Paper 2 practice paper A (25 parts, numbered as the three sections of Paper 2)
P2 = []


def R(label, prompt, right, wrongs, step, hint, concept, skill="Reasoning"):
    P2.append(K(label + " " + prompt, right, wrongs, step, hint, concept, skill))


PASSAGE_B = ("Passage B (invented for practice; author and work are imaginary): 'Fair shares are not always equal shares. If a baker gives every customer "
             "the same loaf, the hungry man and the man who has just eaten both leave unsatisfied in different ways. Justice therefore asks us to look at "
             "need before it counts loaves. A rule that ignores need may look equal, but it treats unequal cases as if they were the same.' (Anselme Tabi, 'Bread and Fairness')")
PASSAGE_C = ("Passage C (invented for practice; author and work are imaginary): 'A country that buys and sells everywhere may grow rich for a season. But a farmer who "
             "sells to one distant buyer has given the price of his work to a stranger. Trade is good, as a river is good; yet a river with no banks floods the fields. "
             "Let us therefore trade, but with banks: stores, savings and many buyers.' (Odile Fotso, 'Rivers and Markets')")

# ---- Section 1: Western philosophy
R("Question 1(a). Essay: 'Is happiness the only goal of morality?'", "Which sentence is the best problematic?",
  "If morality aims only at happiness, can it still protect individuals and duties that seem to matter more than total happiness?", [
      ("Happiness is a very important word.", "This is a remark, not a problem."),
      ("Bentham was born in 1748.", "A fact about a philosopher is not a problem."),
      ("This essay will list all moral theories.", "A list of theories is not a problem.")],
  "A problematic puts the central difficulty as a question or tension.", "Which sentence shows a tension?", "The philosophical dissertation")
R("Question 1(b). Same essay.", "Which pair of thinkers best supports the thesis that happiness is the goal?", "Bentham and Mill", [
    ("Kant and Ross", "They defend duty, which is the antithesis."),
    ("Hobbes and Locke", "They are contract theorists."),
    ("Plato and Nozick", "Plato and Nozick are not the standard supporters of the happiness thesis.")],
  "Bentham and Mill defend the principle of utility.", "Which thinkers defend the greatest happiness?", "Utilitarianism", "Recall")
R("Question 1(c). Same essay.", "Which is the strongest antithesis?", "Kant: acts are right from duty and respect for persons, not from results, so some acts are wrong even if they raise happiness", [
    ("Bentham: pleasures should be measured by seven features", "That supports the thesis."),
    ("Mill: pleasures differ in quality", "That is a refinement of the thesis."),
    ("Happiness is pleasant", "That is not an objection.")],
  "An antithesis challenges the thesis; Kant's duty ethics challenges consequentialism.", "Which view says results do not decide?", "Conscience and duty")
R("Question 1(d). Same essay.", "Which is the best synthesis?", "Happiness is a central aim, but constrained by rights and duties (rule utilitarianism, Mill's harm principle, prima facie duties)", [
    ("Happiness is the only goal, as Bentham said", "That repeats the thesis."),
    ("Duty alone matters, as Kant said", "That repeats the antithesis."),
    ("Morality is impossible", "That abandons the question.")],
  "A synthesis keeps what is sound in both and sets conditions.", "Which answer joins both?", "The philosophical dissertation")
R("Question 1(e). Same essay.", "Which of these belongs in the conclusion?", "A reasoned personal judgement and an opening to a further question", [
    ("A new argument that was not discussed earlier", "A conclusion does not add a new argument."),
    ("The first definition of 'happiness'", "Definitions belong in the introduction."),
    ("A second thesis", "The conclusion does not start a new thesis.")],
  "The conclusion recalls, judges and opens.", "What is the last paragraph for?", "The philosophical dissertation", "Recall")
R("Question 2(a). Essay: 'Can a person be held responsible for caused acts?'", "Which key terms need definition in the introduction?", "Responsibility, free will and determinism", [
    ("Dialectic, synthesis and conclusion", "These are method terms, not key concepts of the question."),
    ("State, law and power", "These belong to another topic."),
    ("Veil, ignorance and position", "These belong to Rawls.")],
  "Define the key concepts of the question.", "Which words are in the question?", "Freedom and determinism", "Application")
R("Question 2(b). Same essay.", "Which position supplies the thesis that caused acts cannot be blamed?", "Hard determinism", [
    ("Libertarianism", "Libertarians deny that choices are fully caused."),
    ("Compatibilism", "Compatibilists say responsibility survives causation."),
    ("Fatalism", "Fatalism is not the usual name for this position.")],
  "Hard determinism denies responsibility given determinism.", "Which position accepts determinism and denies freedom?", "Freedom and determinism", "Recall")
R("Question 2(c). Same essay.", "Which reply best fits the antithesis?", "Compatibilism: acting from one's own reasons is enough for responsibility, even in a caused world", [
    ("Fatalism: nothing can be changed", "That does not answer the thesis."),
    ("Egoism: each person pursues own interest", "That is a different theory."),
    ("Relativism: all views are equal", "That is not a reply.")],
  "Compatibilists redefine freedom as acting on one's own reasons.", "Which reply keeps determinism but saves responsibility?", "Freedom and determinism")
R("Question 2(d). Same essay.", "Which is an internal critique of libertarianism?", "An uncaused choice would seem random and so not under the agent's control", [
    ("The author lived in the 18th century", "A fact about dates is not an internal critique."),
    ("Science uses mathematics", "Not relevant."),
    ("Courts hold trials", "Not relevant.")],
  "The randomness objection uses the libertarian's own assumption.", "Which objection uses the libertarian's premise?", "Freedom and determinism")
R("Question 2(e). Same essay.", "Which synthesis is best?", "The answer depends on what freedom means: if it means uncaused choice, determinism threatens responsibility; if it means self-governed action, it does not", [
    ("Everyone is always responsible", "That ignores the problem."),
    ("No one is ever responsible", "That repeats the thesis."),
    ("The question cannot be understood", "That abandons the question.")],
  "The synthesis makes a distinction between senses of freedom.", "Which answer distinguishes two senses?", "Freedom and determinism")

# ---- Section 2: African philosophy
R("Question 3(a). Essay: 'To what extent can African philosophy be called communal?'", "What is the intent of the question?", "To decide how far African philosophy is shared community thought rather than individual critical thought", [
    ("To list African philosophers", "A list does not answer 'to what extent'."),
    ("To prove that Africa has no philosophy", "The question does not assume that."),
    ("To describe Western philosophy", "The question concerns African philosophy.")],
  "'To what extent' asks for a judgement with limits.", "What does the question ask you to judge?", "The debate on African philosophy", "Application")
R("Question 3(b). Same essay.", "Which thinkers best illustrate the thesis (communal thought)?", "Tempels and Mbiti (ethnophilosophy)", [
    ("Towa and Hountondji", "They criticised ethnophilosophy: the antithesis."),
    ("Marx and Hegel", "They are not African philosophers."),
    ("Popper and Kuhn", "They are philosophers of science.")],
  "Ethnophilosophy presents the collective world view of a people.", "Which trend records community thought?", "Ethnophilosophy: Tempels and Mbiti", "Recall")
R("Question 3(c). Same essay.", "Which evidence best supports the antithesis (individual critical thought)?", "Oruka's philosophic sages and the professional trend of Towa and Hountondji", [
    ("The vital force hierarchy", "This supports communal thought."),
    ("Proverbs repeated by a folk sage", "The folk sage carries communal wisdom."),
    ("A single ritual", "This is not a critical argument.")],
  "Philosophic sages and professional philosophers show individual critical thinking.", "Which kind of sage thinks critically?", "Odera Oruka's four trends")
R("Question 3(d). Same essay.", "The 'myth of unanimity' is a criticism of the claim that:", "all members of a community share the same philosophy", [
    ("philosophy requires writing", "That is a different issue (the oral status)."),
    ("philosophy can only be African", "Not the criticism."),
    ("logic is universal", "Not the criticism.")],
  "Critics say that communities are not unanimous.", "Who is assumed to agree?", "The debate on African philosophy")
R("Question 4(a). Essay: 'Explain the idea of vital force in Tempels.'", "What is the intent of the question?", "To explain being as force animating all beings, not to discuss whether witchcraft exists", [
    ("To argue that witchcraft exists", "The question concerns the theory of being."),
    ("To explain Mbiti's concept of time", "That is a different thinker and concept."),
    ("To compare Hegel and Marx", "That is a different topic.")],
  "The vital force is a metaphysical idea of dynamic being.", "What does the force animate?", "Ethnophilosophy: Tempels and Mbiti", "Application")
R("Question 4(b). Same essay.", "In Tempels's hierarchy, which is the correct order from the origin of force downward?", "God, ancestors, living humans, rest of nature", [
    ("Rest of nature, humans, ancestors, God", "This reverses the order."),
    ("Humans, God, nature, ancestors", "This does not follow the hierarchy."),
    ("Ancestors, God, nature, humans", "God is the origin.")],
  "Force flows from God through ancestors and humans to the rest of nature.", "Where does force originate?", "Ethnophilosophy: Tempels and Mbiti", "Recall")
R("Question 4(c). Same essay.", "A critic of ethnophilosophy would say that Tempels's account:", "presents a European's description of Africans' collective thought as if all Africans held it", [
    ("is a model of logical argument", "That is not the critic's claim."),
    ("was written by a professional African philosopher", "Tempels was a Belgian missionary."),
    ("proves that philosophy is impossible", "Not the claim.")],
  "Towa and Hountondji criticised the ethnophilosophical method.", "Who wrote and for whom?", "Professional philosophy")
R("Question 4(d). Same essay.", "Mbiti's remark that Africans are deeply religious is used to support the idea that:", "religion permeates all parts of life in traditional African thought", [
    ("Africans have no philosophy", "That is the claim critics of the debate oppose."),
    ("religion has no role in society", "The reverse is claimed."),
    ("Africans are all monotheists in the same way", "Not what is claimed here.")],
  "For Mbiti religion permeates life and is the framework of thought.", "How widely does religion spread in life?", "Ethnophilosophy: Tempels and Mbiti")

# ---- Section 3: Textual analysis (invented passages)
R("Question 5(a). " + PASSAGE_B, "What is the theme?", "Justice, fairness and need", [
    ("Baking and cooking", "The baker is only an example."),
    ("Trade between countries", "Not the theme."),
    ("The rules of grammar", "Not the theme.")],
  "The baker example illustrates fairness and need.", "What general subject do the loaves illustrate?", "Justice", "Interpretation")
R("Question 5(b). Same passage B.", "Which sentence best states the thesis?", "Justice requires attention to relevant differences such as need, not identical shares", [
    ("Bread is more important than other foods", "Not the claim."),
    ("Everyone should receive an equal loaf", "The author denies this."),
    ("Hunger does not exist", "Not the claim.")],
  "The author argues that equal shares can be unjust.", "What does the 'therefore' sentence claim?", "Justice", "Interpretation")
R("Question 5(c). Same passage B.", "What is the function of the baker example?", "An illustration of how equal treatment can treat unequal cases as the same", [
    ("A proof by statistics", "No statistics are given."),
    ("An appeal to an authority", "No authority is cited."),
    ("A definition of justice", "It is an illustration, not a definition.")],
  "The example makes the abstract point concrete.", "What kind of reasoning uses a single case?", "The commentary on a philosophical text")
R("Question 5(d). Same passage B.", "Which is the best external critique?", "Nozick would reply that people may use their own bread as they choose, so need does not decide what is due", [
    ("The passage has three sentences", "This is not a critique."),
    ("The word 'bread' is repeated", "This is not a critique."),
    ("The passage is invented", "This is not a critique of the argument.")],
  "An external critique uses a rival view.", "Which option applies the entitlement theory?", "Justice", "Application")
R("Question 6(a). " + PASSAGE_C, "What kind of reasoning is the comparison with a river?", "An analogy", [
    ("A syllogism", "It is not in syllogistic form."),
    ("A statistical proof", "No statistics are given."),
    ("A definition", "It is not defining a term.")],
  "A river that needs banks is compared to trade that needs safeguards.", "Is the river a literal or a figurative comparison?", "The commentary on a philosophical text", "Interpretation")
R("Question 6(b). Same passage C.", "Which position on globalization does the author hold?", "A moderate view: trade is beneficial but needs safeguards against dependence", [
    ("Trade is always harmful", "The author says trade is good."),
    ("Trade needs no limits", "The author calls for banks, meaning limits."),
    ("Only local trade is moral", "Not claimed.")],
  "The author accepts trade and urges protections.", "Does the author accept or reject trade?", "Globalization", "Interpretation")
R("Question 6(c). Same passage C.", "Which is an internal critique?", "The analogy is incomplete: it does not say who builds the banks or how poor farmers could afford them", [
    ("The passage mentions a farmer", "This is a description, not a critique."),
    ("The author uses the word 'trade'", "Not a critique."),
    ("The passage is short", "Not a critique.")],
  "An internal critique finds a gap in the argument.", "What does the analogy leave unexplained?", "The commentary on a philosophical text")

assert len(P2) == 25, len(P2)
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="psu2-paper-2-strategy",
                         mock=True, time_limit_minutes=150, questions=build(P2, 302)))

# ================================================================== Paper 3 practice paper A (20 parts: logic, method, systematic philosophy)
P3 = []


def L(label, prompt, right, wrongs, step, hint, concept="Paper 3", skill="Reasoning"):
    P3.append(K(label + " " + prompt, right, wrongs, step, hint, concept, skill))


SYL1 = "No cats are dogs. Some pets are dogs. Therefore some pets are not cats."
SYL2 = "All doctors are graduates. Some graduates are not teachers. Therefore some doctors are not teachers."

# ---- Question 1: traditional logic
L("Question 1(a). Syllogism: " + SYL1, "What is the figure of this syllogism?", "Figure 2", [
    ("Figure 1", "In figure 1 the middle term is the subject of the major premise and the predicate of the minor premise."),
    ("Figure 3", "In figure 3 the middle term is the subject of both premises."),
    ("Figure 4", "In figure 4 the middle term is predicate of the major premise and subject of the minor.")],
  "S = pets, P = cats, M = dogs. Major premise: cats-dogs (P-M); minor premise: pets-dogs (S-M). The middle term is the predicate of both premises: figure 2.", "Where does 'dogs' stand in each premise?", skill="Application")
L("Question 1(b). Same syllogism.", "What is its mood?", "EIO", [
    ("EAO", "The minor premise is particular affirmative (I), not universal affirmative (A)."),
    ("AII", "The major premise is universal negative (E), not A."),
    ("OIE", "The mood is read as major premise, minor premise, conclusion: E, I, O.")],
  "'No cats are dogs' is E; 'Some pets are dogs' is I; 'Some pets are not cats' is O.", "Identify each statement: A, E, I or O.", skill="Application")
L("Question 1(c). Same syllogism.", "Is it valid?", "Valid, since EIO-2 follows all the rules", [
    ("Invalid, because the middle term is undistributed", "The middle term 'dogs' is distributed in the major premise (predicate of an E)."),
    ("Invalid, because it has a negative conclusion from affirmative premises", "One premise is negative, so a negative conclusion is allowed."),
    ("Invalid, because the major term is illicitly distributed", "'Cats' is distributed in the premise (subject of an E) as well as in the conclusion.")],
  "EIO-2 is among the 24 valid forms of traditional logic (checked by brute force).", "Test the middle and the distribution of terms.", skill="Reasoning")
L("Question 1(d). Syllogism: " + SYL2, "Which fallacy does it commit?", "Undistributed middle", [
    ("Illicit major", "The major term 'teachers' is distributed in the conclusion (predicate of an O) and also in the major premise (predicate of an O)."),
    ("Illicit minor", "The minor term 'doctors' is not distributed in the conclusion (subject of an O)."),
    ("Exclusive premises", "Only one premise is negative.")],
  "Middle term 'graduates' is the subject of an O in the major premise (undistributed) and the predicate of an A in the minor premise (undistributed): never distributed. The form is OAO-1, invalid.", "Is the middle term distributed in at least one premise?", skill="Reasoning")
L("Question 1(e). Statement: 'Some students are not lazy.'", "Which term does an O statement distribute?", "Only the predicate ('lazy')", [
    ("Only the subject ('students')", "In an O statement the subject is undistributed."),
    ("Both terms", "Only one term is distributed."),
    ("Neither term", "The predicate of an O is distributed.")],
  "O statements distribute the predicate only.", "Recall the four forms: A distributes the subject, E both, I neither, O the predicate.", skill="Recall")
L("Question 1(f). Statement: 'No politicians are honest.'", "What is its obverse?", "All politicians are non-honest", [
    ("All honest people are politicians", "That is not equivalent."),
    ("Some politicians are honest", "That is its contradictory."),
    ("No honest people are politicians", "That is its converse, not its obverse.")],
  "Obversion: change quality and replace the predicate by its complement. E becomes A: 'All S are non-P'.", "Obversion changes the quality and complements the predicate.", skill="Application")

# ---- Question 2: propositional logic
L("Question 2(a). Formula: (p ⊃ q) ∨ p.", "How is the formula classified by its truth table?", "Tautology", [
    ("Contradiction", "It is not false in every row."),
    ("Contingent", "It is true in every row, so not contingent."),
    ("Equivalence", "A formula is not called an equivalence unless it joins two sides by the biconditional.")],
  "Rows (p q): TT: T; TF: T (p true); FT: T (p ⊃ q true); FF: T (p ⊃ q true). All true.", "Complete the four rows.", skill="Calculation")
L("Question 2(b). Formula: (p ⊃ q) ⊃ p.", "How is the formula classified?", "Contingent", [
    ("Tautology", "It is false in the rows where p is false."),
    ("Contradiction", "It is true where p is true."),
    ("Valid argument", "A formula is not an argument.")],
  "Rows: TT T, TF T, FT F, FF F: true in two rows, false in two.", "Do all rows give the same value?", skill="Calculation")
L("Question 2(c). Argument: p ∨ q; ~p; therefore q.", "Which rule justifies the conclusion?", "Disjunctive syllogism", [
    ("Modus ponens", "Modus ponens uses a conditional."),
    ("Hypothetical syllogism", "That joins two conditionals."),
    ("Affirming the consequent", "That is a fallacy with a conditional.")],
  "If one disjunct is denied, the other is affirmed.", "Which rule uses 'or'?", skill="Recall")
L("Question 2(d). Argument: p ⊃ q; ~p; therefore ~q.", "Is the argument valid?", "Invalid: p false and q true makes both premises true and the conclusion false", [
    ("Valid, by modus tollens", "Modus tollens denies the consequent, not the antecedent."),
    ("Valid, because the premises are true", "Validity depends on form."),
    ("Invalid, because the conclusion is a negation", "Negations can be valid conclusions.")],
  "This is denying the antecedent. Counter-row: p F, q T.", "Search for a row with true premises and a false conclusion.", skill="Reasoning")
L("Question 2(e). Which is equivalent to p ⊃ q?", "Choose the formula.", "~p ∨ q", [
    ("p ∨ ~q", "This is not equivalent."),
    ("~p · q", "This is not equivalent."),
    ("q ⊃ p", "This is the converse, not equivalent.")],
  "p ⊃ q is false only when p is true and q false; the same as ~p ∨ q (checked by brute force).", "Test row TF.", skill="Reasoning")

# ---- Question 3: predicate logic
L("Question 3(a). Symbolise 'No politicians are honest' (Px: x is a politician; Hx: x is honest).", "Which formula is correct?", "(x)(Px ⊃ ~Hx)", [
    ("(x)(Px ⊃ Hx)", "That says all politicians are honest."),
    ("(∃x)(Px · ~Hx)", "That says some politician is not honest."),
    ("(∃x)(Px · Hx)", "That says some politician is honest.")],
  "For anything, if it is a politician, then it is not honest.", "Paraphrase first.", skill="Application")
L("Question 3(b). Symbolise 'Some students are not lazy' (Sx: x is a student; Lx: x is lazy).", "Which formula is correct?", "(∃x)(Sx · ~Lx)", [
    ("(x)(Sx ⊃ ~Lx)", "That says no student is lazy."),
    ("(∃x)(Sx ⊃ ~Lx)", "A conditional under ∃ is true if anything is not a student: wrong form."),
    ("(x)(Sx · ~Lx)", "That says that everything is a student and is not lazy.")],
  "There exists something that is a student and not lazy.", "Which quantifier goes with 'some' and what joins the predicates?", skill="Application")
L("Question 3(c). Negation.", "Which is equivalent to ~(x)Fx?", "(∃x)~Fx", [
    ("(x)~Fx", "That says that everything lacks F."),
    ("(∃x)Fx", "That says that something has F."),
    ("~(∃x)Fx", "That says that nothing has F.")],
  "Not everything is F means that something is not F (checked over finite domains).", "What does 'not everything' leave open?", skill="Reasoning")

# ---- Question 4: text commentary and dissertation method
L("Question 4(a). Passage D (invented): 'A promise made in fear is not a promise but a surrender. A promise has worth only when the one who gives it could have refused. Therefore the law should not enforce agreements signed under threat.'", "What is the thesis?", "Agreements made under threat should not be enforced, because a promise needs freedom to refuse", [
    ("All agreements are worthless", "The text says freedom gives worth, not that all are worthless."),
    ("Fear is a pleasant feeling", "Not the claim."),
    ("The law should punish everyone", "Not the claim.")],
  "The thesis follows 'therefore' and rests on the claim about refusal.", "Which sentence has the conclusion marker?", "The commentary on a philosophical text", "Interpretation")
L("Question 4(b). Same passage D.", "Which is an internal critique?", "The passage does not say how to judge when a threat is serious enough to cancel an agreement", [
    ("The passage is short", "Not a philosophical critique."),
    ("The passage mentions the law", "That is an observation."),
    ("The passage uses the word 'promise'", "That is an observation.")],
  "An internal critique points to a gap or hidden assumption.", "What does the author leave undefined?", "The commentary on a philosophical text", "Application")
L("Question 4(c). Dissertation: 'Is it ever right to disobey the law?'", "Which is the best problematic?", "If law claims our obedience but may be unjust, can conscience ever outrank the law?", [
    ("Laws are made by governments.", "This is background."),
    ("Everyone should obey.", "This is a thesis."),
    ("The Constitution has many articles.", "This is not a problem.")],
  "The problematic expresses the tension at the heart of the question.", "Which option puts two claims in tension?", "The philosophical dissertation", "Application")

# ---- Question 5: systematic philosophy (philosophical problems)
L("Question 5(a). Problem: 'If all my actions are caused, can I be responsible?'", "Which position best answers by redefining freedom as acting from one's own reasons?", "Compatibilism", [
    ("Hard determinism", "It denies that this is enough for responsibility."),
    ("Libertarianism", "It denies that choices are fully caused."),
    ("Fatalism", "Fatalism says outcomes are fixed whatever we choose.")],
  "Compatibilism keeps determinism and redefines freedom.", "Which position keeps both determinism and responsibility?", "Freedom and determinism", "Concept")
L("Question 5(b). Problem: 'Is it fair that a child of rich parents has more opportunities than a child of poor parents?'", "Which principle of Rawls bears most directly on this question?", "Fair equality of opportunity", [
    ("The categorical imperative", "That is Kant's idea."),
    ("The calculus of pleasures", "That is Bentham's idea."),
    ("The harm principle", "That is Mill's idea about liberty.")],
  "Rawls's second principle requires fair equality of opportunity.", "Which principle speaks of opportunity?", "Justice", "Application")

assert len(P3) == 19, len(P3)
_qs = build(P3, 303)
_num = NUM("Question 2(f). How many rows of the truth table of p ∨ (q · r) are true? (The table has eight rows.)", 5,
           steps=[S("Rows (p q r)", text="p true: TTT, TTF, TFT, TFF are all true (4 rows). p false: only FTT has q · r true. That gives 5."),
                  S("Check", text="Brute-force enumeration of all eight rows gives 5 true rows.")],
           tolerance=0, concept="Paper 3", skill="Calculation", hint="Count the rows where p is true, then the rows where p is false but q and r are both true.")
_qs.insert(11, _num)
assert len(_qs) == 20
SETS.append(practice_set(module=M_EXAM, topic="Paper 3", title="Paper 3 practice paper A", lesson="psu2-paper-3-strategy",
                         mock=True, time_limit_minutes=150, questions=_qs))
