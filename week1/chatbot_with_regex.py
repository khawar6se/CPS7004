import re
class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if re.search(rule["condition"], text, re.IGNORECASE):
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."

# Example usage
rule_engine = RuleEngine()



rule_engine.add_rule(r'\bsuggest a travel destination\b', 'How about visiting Japan?')
rule_engine.add_rule(r'\brecommend a place to visit\b', 'You might enjoy Italy!')
rule_engine.add_rule(r'\bwhere should I travel\b', 'Try exploring New Zealand!')
rule_engine.add_rule(r'\bi want to travel\b', 'Consider a trip to Greece.')
rule_engine.add_rule(r'\bgive me a travel idea\b', 'Bali is a beautiful destination.')
rule_engine.add_rule(r'\bsuggest a country to visit\b', 'Thailand is perfect for adventure and beaches.')
rule_engine.add_rule(r'\bbest country to travel\b', 'Switzerland is stunning all year round.')
rule_engine.add_rule(r'\btravel recommendation\b', 'Portugal has great food and scenery.')
rule_engine.add_rule(r'\bgood place for vacation\b', 'Try the Maldives for a luxurious beach getaway.')
rule_engine.add_rule(r'\bsummer vacation idea\b', 'How about a road trip along the Amalfi Coast?')
rule_engine.add_rule(r'\bwinter travel destination\b', 'You might enjoy skiing in Austria.')
rule_engine.add_rule(r'\bbest cities to visit\b', 'Paris, Tokyo, and New York are top picks.')
rule_engine.add_rule(r'\bromantic getaway\b', 'Santorini is perfect for couples.')
rule_engine.add_rule(r'\btravel alone\b', 'Vietnam is safe and ideal for solo travelers.')
rule_engine.add_rule(r'\btravel with kids\b', 'Orlando, Florida is great for family fun.')
rule_engine.add_rule(r'\bgood beach vacation\b', 'The Seychelles are breathtaking.')
rule_engine.add_rule(r'\bmountain destination\b', 'Try visiting Banff in Canada.')
rule_engine.add_rule(r'\btravel on a budget\b', 'Go to Mexico – it’s affordable and beautiful.')
rule_engine.add_rule(r'\bluxury travel\b', 'Dubai offers high-end experiences.')
rule_engine.add_rule(r'\bcheap places to travel\b', 'India is budget-friendly and full of culture.')
rule_engine.add_rule(r'\bcultural travel\b', 'Morocco is rich in heritage and history.')
rule_engine.add_rule(r'\bsuggest a nature spot\b', 'Costa Rica is great for eco-tourism.')
rule_engine.add_rule(r'\badventure travel\b', 'Try hiking in Patagonia.')
rule_engine.add_rule(r'\bsuggest a city break\b', 'Barcelona is a lively city to explore.')
rule_engine.add_rule(r'\bbest travel for food\b', 'You should visit Thailand for street food.')
rule_engine.add_rule(r'\bbest travel for wine\b', 'Visit Bordeaux in France.')
rule_engine.add_rule(r'\bfamous travel destinations\b', 'Try the Eiffel Tower in Paris.')
rule_engine.add_rule(r'\bhidden travel gems\b', 'Check out Slovenia – underrated and gorgeous.')
rule_engine.add_rule(r'\btravel to Europe\b', 'Prague is affordable and beautiful.')
rule_engine.add_rule(r'\btravel to Asia\b', 'Kyoto, Japan offers amazing traditions.')
rule_engine.add_rule(r'\btravel to Africa\b', 'South Africa has great wildlife safaris.')
rule_engine.add_rule(r'\btravel to America\b', 'Visit San Francisco or Miami.')
rule_engine.add_rule(r'\btravel to Australia\b', 'Sydney and the Great Barrier Reef are must-sees.')
rule_engine.add_rule(r'\btravel to South America\b', 'Peru is perfect for history and hiking.')
rule_engine.add_rule(r'\btravel to Canada\b', 'Don’t miss the beauty of Vancouver and Banff.')
rule_engine.add_rule(r'\btrip idea\b', 'Try a boat cruise in Norway’s fjords.')
rule_engine.add_rule(r'\bweekend getaway\b', 'Visit Charleston, South Carolina.')
rule_engine.add_rule(r'\b3 day trip\b', 'How about Lisbon, Portugal?')
rule_engine.add_rule(r'\broad trip ideas\b', 'Route 66 in the US is iconic.')
rule_engine.add_rule(r'\bfamous landmarks\b', 'Visit the Great Wall of China!')
rule_engine.add_rule(r'\bnature vacation\b', 'Yosemite National Park is amazing.')
rule_engine.add_rule(r'\bwildlife travel\b', 'Go on a safari in Kenya.')
rule_engine.add_rule(r'\bdesert destination\b', 'Try Wadi Rum in Jordan.')
rule_engine.add_rule(r'\barctic travel\b', 'Explore Iceland’s glaciers.')
rule_engine.add_rule(r'\bscenic travel spot\b', 'New Zealand’s South Island is breathtaking.')
rule_engine.add_rule(r'\brural travel\b', 'The Scottish Highlands are peaceful.')
rule_engine.add_rule(r'\bhistorical sites\b', 'Visit Rome and its ancient ruins.')
rule_engine.add_rule(r'\blake vacation\b', 'Lake Como in Italy is perfect.')
rule_engine.add_rule(r'\briver cruise\b', 'Cruise the Danube through Central Europe.')
rule_engine.add_rule(r'\bsuggest islands\b', 'Try the Azores in Portugal.')
rule_engine.add_rule(r'\bmust visit countries\b', 'Japan, Italy, and Peru are all amazing.')
rule_engine.add_rule(r'\btravel safely\b', 'Consider Singapore – it’s very safe.')
rule_engine.add_rule(r'\bI like hiking\b', 'Try the Inca Trail in Peru.')
rule_engine.add_rule(r'\bI love beaches\b', 'Try Boracay in the Philippines.')
rule_engine.add_rule(r'\bI love snow\b', 'Visit Hokkaido in Japan.')
rule_engine.add_rule(r'\bbest airports\b', 'Singapore Changi is world-renowned.')
rule_engine.add_rule(r'\bcheap Europe travel\b', 'Try visiting Budapest.')
rule_engine.add_rule(r'\bcity for nightlife\b', 'Berlin is known for its clubs.')
rule_engine.add_rule(r'\bwhere to go in December\b', 'Try Christmas markets in Germany.')
rule_engine.add_rule(r'\bwhere to go in summer\b', 'Greece is great in July and August.')
rule_engine.add_rule(r'\btrip for nature lovers\b', 'Go to New Zealand’s Milford Sound.')
rule_engine.add_rule(r'\btrip for photographers\b', 'Try Iceland for dramatic landscapes.')
rule_engine.add_rule(r'\bquiet travel destinations\b', 'Go to Bhutan – serene and peaceful.')
rule_engine.add_rule(r'\bbest travel countries 2024\b', 'Japan, Colombia, and Slovenia.')
rule_engine.add_rule(r'\btravel like a local\b', 'Try Vietnam and eat at local markets.')
rule_engine.add_rule(r'\bI want to relax\b', 'Bora Bora is the ultimate chill spot.')
rule_engine.add_rule(r'\broad trips in Europe\b', 'Try the Romantic Road in Germany.')
rule_engine.add_rule(r'\bI want adventure\b', 'Nepal is amazing for trekking.')
rule_engine.add_rule(r'\bbest places for diving\b', 'The Great Barrier Reef is top tier.')
rule_engine.add_rule(r'\bscuba diving travel\b', 'Go to the Maldives.')
rule_engine.add_rule(r'\bromantic cities\b', 'Venice is dreamy.')
rule_engine.add_rule(r'\bplaces with great food\b', 'You can’t go wrong with Italy.')
rule_engine.add_rule(r'\btravel during spring\b', 'Visit the Netherlands for tulips.')
rule_engine.add_rule(r'\btravel during fall\b', 'Try New England in the USA for autumn colors.')
rule_engine.add_rule(r'\bweek-long vacation\b', 'Travel across Croatia’s coast.')
rule_engine.add_rule(r'\bquick flight destination\b', 'Reykjavik is only 5 hours from NYC.')
rule_engine.add_rule(r'\boffbeat destinations\b', 'Try Albania – beautiful and less crowded.')
rule_engine.add_rule(r'\bUNESCO sites\b', 'Visit Machu Picchu in Peru.')
rule_engine.add_rule(r'\bI want to see animals\b', 'Galápagos Islands are perfect.')
rule_engine.add_rule(r'\bbest travel for art\b', 'Florence, Italy is a top destination.')
rule_engine.add_rule(r'\barchitecture travel\b', 'Barcelona has stunning Gaudi architecture.')
rule_engine.add_rule(r'\broad trip usa\b', 'Try the Pacific Coast Highway.')
rule_engine.add_rule(r'\btravel to islands\b', 'Visit Zanzibar off the coast of Tanzania.')
rule_engine.add_rule(r'\btravel to volcanoes\b', 'Try Mount Etna in Sicily.')
rule_engine.add_rule(r'\btravel for relaxation\b', 'Go to a spa retreat in Bali.')
rule_engine.add_rule(r'\btravel to waterfalls\b', 'See Iguazu Falls in Argentina.')
rule_engine.add_rule(r'\btravel with pets\b', 'Oregon is very pet-friendly.')
rule_engine.add_rule(r'\btravel for coffee\b', 'Colombia is the place to go.')
rule_engine.add_rule(r'\btravel for tea\b', 'Try Sri Lanka’s tea regions.')
rule_engine.add_rule(r'\bwinter sports travel\b', 'Go to the French Alps.')
rule_engine.add_rule(r'\bsuggest an island escape\b', 'Try Palawan in the Philippines.')
rule_engine.add_rule(r'\bgood honeymoon destinations\b', 'Maldives, Hawaii, and Italy.')
rule_engine.add_rule(r'\bski destinations\b', 'Try Zermatt in Switzerland.')
rule_engine.add_rule(r'\bgood travel for seniors\b', 'Cruises or European river tours are great.')
rule_engine.add_rule(r'\bplaces with beautiful lakes\b', 'Lake Bled in Slovenia is magical.')
rule_engine.add_rule(r'\bbest deserts to visit\b', 'Sahara in Morocco or Atacama in Chile.')


while True:
    user_input = input("You: ")
    response = rule_engine.apply_rules(user_input)
    print(response)
    
    if user_input.lower() == "goodbye":
      break