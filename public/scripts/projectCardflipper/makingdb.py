names = [
    "0. The Fool", 
    "I. The Magician", 
    "II. The Priestess", 
    "III. The Empress", 
    "IV. The Emperor", 
    "V. The Hierophant", 
    "VI. The Lovers", 
    "VII. The Chariot", 
    "VIII. Justice", 
    "IX. The Hermit", 
    "X. The Wheel of Fortune", 
    "XI. Strength", 
    "XII. The Hanged Man", 
    "XIII. Death", 
    "XIV. Temperance", 
    "XV. The Devil", 
    "XVI. The Tower", 
    "XVII. The Star", 
    "XVIII. The Moon", 
    "XIX. The Sun", 
    "XX. Judgement", 
    "XXI. The World"
]

images = [r'./00\ -\ Fool.jpg', 
    r'./01\ -\ Magician.jpg', 
    r'./02\ -\ HighPriestess.jpg', 
    r'./03\ -\ Empress.jpg', 
    r'./04\ -\ Emperor.jpg', 
    r'./05\ -\ Hierophant.jpg', 
    r'./06\ -\ TheLovers.jpg', 
    r'./07\ -\ Chariot.jpg', 
    r'./08\ -\ Strength.jpg', 
    r'./09\ -\ Hermit.jpg',
    '', 
    r'./11\ -\ Justice.jpg', 
    r'./12\ -\ HangedMan.jpg', 
    r'./13\ -\ Death.jpg',
    '', 
    r'./15\ -\ Devil.jpg', 
    r'./16\ -\ Tower.jpg', 
    r'./17\ -\ Star.jpg', 
    r'./18\ -\ Moon.jpg', 
    r'./19\ -\ Sun.jpg', 
    r'./20\ -\ Judgement.jpg',
    ''
    ]

titles = ["The path taken through the great mysteries of life", 
    "As above, so below", 
    "Divine law", 
    "The repository of all things nurturing and sustaining", 
    "Sterility of regulation, and unyielding power", 
    "The Teacher of Wisdom", 
    "No return from making bad decisions, and the consequences of innocence lost, would be more widely understood from this imagery", 
    "Celestial influences", 
    "A balanced decision", 
    "Withdrawal from events and relationship to introspect and gather strength", 
    "R-O-T-A", 
    "Fortitude or Lust", 
    "Divine and the Universe", 
    "Death-Rebirth", 
    "Virtue temperance", 
    "Dogme et Rituel de la Haute Magie", 
    "Dislodged and crumbling", 
    "One foot in the water and one foot on the land", 
    "The imagination apart from life of the spirit", 
    "The child of life holds a red flag",
    "Of sallow complexion stand, arms spread, looking up at the angel in awe", 
    "It is completeness."]

descriptions = [
        "UPRIGHT: Folly, mania, extravagance, intoxication, delirium, frenzy, bewrayment. REVERSED: Negligence, absence, distribution, carelessness, apathy, nullity, vanity.",
        "UPRIGHT: Potential and tapping into one's talents. REVERSED: Potential and talents are unfocused and unmanifested.", 
        "UPRIGHT: Secrets, mystery, the future as yet unrevealed; the woman who interests the Querent, the Querent herself, silence, tenacity; mystery, wisdom, science. REVERSED: Passion, moral or physical ardor, conceit, surface knowledge.", 
        "UPRIGHT: Fruitfulness, action, initiative, length of days; the unknown, clandestine; also difficulty, doubt, ignorance. REVERSED: Light, truth, the unraveling of involved matters, public rejoicings; according to another reading, vacillation.", 
        "UPRIGHT: Authority, establishment, structure, a father figure. REVERSED: Domination, excessive control, lack of discipline, inflexibility", 
        "UPRIGHT: Marriage, alliance, captivity, servitude; by another account, mercy, and goodness; inspiration; the man to whom the Querent has recourse. REVERSED: Society, good understanding, concord, over kindness, weakness.", 
        "UPRIGHT: Attraction, love, beauty, trials overcome. REVERSED: Failure, foolish designs. Another account speaks of marriage frustrated and contrarieties of all kinds.", 
        "UPRIGHT: Succour, providence; also war, triumph, presumption, vengeance, trouble. REVERSED: Riot, quarrel, dispute, litigation, defeat.",
        "UPRIGHT: Equity, rightness, probity, executive; triumph of the deserving side in law. REVERSED: Law in all its departments, legal complications, bigotry, bias, excessive severity.", 
        "UPRIGHT: Prudence, circumspection; also and especially treason, dissimulation, roguery, corruption. REVERSED: Concealment, disguise, policy fear, unreasoned caution.", 
        "UPRIGHT: Destiny, fortune, success, elevation, luck, felicity. REVERSED: Increase, abundance, superfluity", 
        "UPRIGHT: Power, energy, action, courage, magnanimity; also complete success and honours. REVERSED: Despotism, abuse of power, weakness, discord, sometimes even disgrace.", 
        "UPRIGHT: Wisdom, circumspection, discernment, trials, sacrifice, intuition, divination, prophecy. REVERSED: Selfishness, the crowd, body politic.", 
        "UPRIGHT: End, mortality, destruction, corruption; also, for a man, the loss of a benefactor; for a woman, many contrarieties; for a maid, failure of marriage projects. REVERSED: Inertia, sleep, lethargy, petrifaction, somnambulism; hope destroyed.", 
        "UPRIGHT: Economy, moderation, frugality, management, accommodation. REVERSED: Things connected with churches, religions, sects, the priesthood, sometimes even the priest who will marry Querent; also disunion, unfortunate combinations, competing interests.", 
        "UPRIGHT: Ravage, violence, vehemence, extraordinary efforts, force, fatality; that which is predestined but is not for this reason evil. REVERSED: Evil fatality, weakness, pettiness, blindness.", 
        "UPRIGHT: Misery, distress, indigence, adversity, calamity, disgrace, deception, ruin. It is a card in particular of unforeseen catastrophe. REVERSED: Negligence, absence, distribution, carelessness, distraction, apathy, nullity, vanity.", 
        "UPRIGHT: Hope and bright prospects, REVERSED: Loss, theft, privation, abandonment; another reading says: arrogance, haughtiness, impotence", 
        "UPRIGHT: Hidden enemies, danger, calumny, darkness, terror, deception, occult forces, error. REVERSED: Instability, inconstancy, silence, lesser degrees of deception and error.", 
        "UPRIGHT: Material happiness, fortunate marriage, contentment. REVERSED: The same in a lesser sense.", 
        "UPRIGHT: UPRIGHT: Judgement, rebirth, inner calling, absolution. REVERSED: Self-doubt, inner critic, ignoring the call", 
        "UPRIGHT: Assured success, recompense, voyage, route, emigration, flight, change of place. REVERSED: Inertia, fixity, stagnation, permanence." 
    ]

for i in range(1,21):
    a = {"_id": i, "Name": names[i], "Image": images[i], "Title": titles[i], "Description": descriptions[i]}
    print(a)
    #print(names, images, titles, descriptions)























