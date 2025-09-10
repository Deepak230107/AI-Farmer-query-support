from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Example solutions dictionary
solutions = {
    # Greetings
    "hi": {
        "en": "Hi! How are you?",
        "ml": "ഹായ്! നിങ്ങൾക്ക് സുഖമാണോ?"
    },
    "hello": {
        "en": "Hello! Nice to meet you.",
        "ml": "ഹലോ! നിങ്ങളെ കണ്ടതിൽ സന്തോഷം."
    },

    # ======================
    # FERTILIZERS (50 items)
    # ======================
    "urea": {
        "en": "Apply Urea (46% N) at recommended dose.",
        "ml": "വിളയ്ക്ക് ശുപാർശ ചെയ്ത അളവിൽ യൂറിയ (46% N) പ്രയോഗിക്കുക."
    },
    "dap": {
        "en": "Apply DAP (18:46:0) for nitrogen and phosphorus.",
        "ml": "നൈട്രജനും ഫോസ്ഫറസിനും വേണ്ടി DAP (18:46:0) പ്രയോഗിക്കുക."
    },
    "mop": {
        "en": "Apply Muriate of Potash (60% K₂O) for potassium.",
        "ml": "പൊട്ടാഷ് ആവശ്യം നിറവേറ്റാൻ MOP (60% K₂O) പ്രയോഗിക്കുക."
    },
    "ssp": {
        "en": "Apply Single Super Phosphate (16% P₂O₅) for phosphorus and sulfur.",
        "ml": "ഫോസ്ഫറസിനും സൾഫറിനും SSP (16% P₂O₅) പ്രയോഗിക്കുക."
    },
    "ammonium sulfate": {
        "en": "Use ammonium sulfate for nitrogen and sulfur.",
        "ml": "നൈട്രജനും സൾഫറിനും അമോണിയം സൾഫേറ്റ് ഉപയോഗിക്കുക."
    },
    "calcium ammonium nitrate": {
        "en": "Apply CAN for quick nitrogen supply.",
        "ml": "വേഗത്തിൽ നൈട്രജൻ ലഭിക്കാൻ CAN പ്രയോഗിക്കുക."
    },
    "rock phosphate": {
        "en": "Use rock phosphate in acidic soils for phosphorus.",
        "ml": "ഫോസ്ഫറസിനായി അമ്ലീയ മണ്ണിൽ റോക്ക് ഫോസ്ഫേറ്റ് ഉപയോഗിക്കുക."
    },
    "gypsum": {
        "en": "Apply gypsum for calcium and sulfur.",
        "ml": "കാൽസ്യത്തിനും സൾഫറിനും ജിപ്സം പ്രയോഗിക്കുക."
    },
    "zinc sulfate": {
        "en": "Apply zinc sulfate @ 25 kg/ha if deficiency occurs.",
        "ml": "കുറവ് കണ്ടാൽ ഹെക്ടറിന് 25 കിലോ സിങ്ക് സൾഫേറ്റ് പ്രയോഗിക്കുക."
    },
    "borax": {
        "en": "Apply borax for boron deficiency correction.",
        "ml": "ബോറൺ കുറവ് പരിഹരിക്കാൻ ബോറാക്സ് പ്രയോഗിക്കുക."
    },
    "ferrous sulfate": {
        "en": "Spray ferrous sulfate to correct iron deficiency.",
        "ml": "ഇരുമ്പ് കുറവ് പരിഹരിക്കാൻ ഫെറസ് സൾഫേറ്റ് സ്പ്രേ ചെയ്യുക."
    },
    "magnesium sulfate": {
        "en": "Apply magnesium sulfate for magnesium deficiency.",
        "ml": "മഗ്നീഷ്യം കുറവിന് മഗ്നീഷ്യം സൾഫേറ്റ് പ്രയോഗിക്കുക."
    },
    "ammonium chloride": {
        "en": "Use ammonium chloride as a nitrogen source in rice.",
        "ml": "നൈട്രജൻ ഉറവിടമായി നെല്ലിൽ അമോണിയം ക്ലോറൈഡ് ഉപയോഗിക്കുക."
    },
    "potassium nitrate": {
        "en": "Apply potassium nitrate as a foliar spray.",
        "ml": "ഇലകളിൽ സ്പ്രേ ചെയ്യാൻ പൊട്ടാസ്യം നൈട്രേറ്റ് പ്രയോഗിക്കുക."
    },
    "calcium nitrate": {
        "en": "Apply calcium nitrate to supply nitrogen and calcium.",
        "ml": "നൈട്രജനും കാൽസ്യവും ലഭിക്കാൻ കാൽസ്യം നൈട്രേറ്റ് പ്രയോഗിക്കുക."
    },
    "zinc chelate": {
        "en": "Use zinc EDTA for better absorption.",
        "ml": "മെച്ചപ്പെട്ട ശോഷണത്തിന് സിങ്ക് EDTA ഉപയോഗിക്കുക."
    },
    "copper sulfate": {
        "en": "Apply copper sulfate in deficient soils.",
        "ml": "കുറവുള്ള മണ്ണിൽ കോപ്പർ സൾഫേറ്റ് പ്രയോഗിക്കുക."
    },
    "potash alum": {
        "en": "Apply potash alum in acidic soils for potassium.",
        "ml": "പൊട്ടാഷിനായി അമ്ലീയ മണ്ണിൽ പൊട്ടാഷ് അലും പ്രയോഗിക്കുക."
    },
    "biofertilizer azospirillum": {
        "en": "Use Azospirillum biofertilizer for nitrogen fixation.",
        "ml": "നൈട്രജൻ ഫിക്സേഷനായി അസോസ്പിരില്ലം ബയോഫെർട്ടിലൈസർ ഉപയോഗിക്കുക."
    },
    "rhizobium culture": {
        "en": "Treat legume seeds with Rhizobium culture.",
        "ml": "പയർവിള വിത്തുകൾ റൈസോബിയം കൾച്ചർ കൊണ്ട് ചികിത്സിക്കുക."
    },

    # Add remaining fertilizers up to 50...
    # (micronutrients, organic manure, vermicompost, neem cake, poultry manure, fish manure, seaweed extract, etc.)

    # ======================
    # PESTICIDES (50 items)
    # ======================
    "mancozeb": {
        "en": "Spray Mancozeb for fungal diseases like leaf spot.",
        "ml": "ഇല പാടുകൾ പോലുള്ള ഫംഗൽ രോഗങ്ങൾക്ക് മാൻകോസെബ് സ്പ്രേ ചെയ്യുക."
    },
    "tricyclazole": {
        "en": "Spray Tricyclazole for rice blast control.",
        "ml": "നെല്ലിൽ ബ്ലാസ്റ്റ് നിയന്ത്രിക്കാൻ ട്രൈസൈക്ലസോൾ സ്പ്രേ ചെയ്യുക."
    },

    "validamycin": {
        "en": "Spray Validamycin for rice sheath blight.",
        "ml": "നെല്ലിൽ ഷീത്ത് ബ്ലൈറ്റ് രോഗത്തിന് വാലിഡാമൈസിൻ സ്പ്രേ ചെയ്യുക."
    },
    "copper oxychloride": {
        "en": "Use copper oxychloride for early blight in tomato.",
        "ml": "തക്കാളിയിൽ എർലി ബ്ലൈറ്റ് രോഗത്തിന് കോപ്പർ ഓക്സിക്ലോറൈഡ് പ്രയോഗിക്കുക."
    },
    "carbendazim": {
        "en": "Spray Carbendazim for fruit rot diseases.",
        "ml": "പഴങ്ങൾ കുതിർക്കുന്ന രോഗങ്ങൾക്ക് കാർബൻഡാസിം സ്പ്രേ ചെയ്യുക."
    },
    "hexaconazole": {
        "en": "Apply Hexaconazole for powdery mildew.",
        "ml": "പൗഡറി മിൽഡ്യൂ രോഗത്തിന് ഹെക്സക്കോനസോൾ പ്രയോഗിക്കുക."
    },
    "metalaxyl": {
        "en": "Use Metalaxyl for downy mildew control.",
        "ml": "ഡൗണി മിൽഡ്യൂ രോഗത്തിന് മെറ്റലാക്സിൽ പ്രയോഗിക്കുക."
    },
    "chlorpyrifos": {
        "en": "Apply Chlorpyrifos to control termites and soil pests.",
        "ml": "ഉളുവൻ കീടങ്ങളും മണ്ണിലെ കീടങ്ങളും നിയന്ത്രിക്കാൻ ക്ലോർപൈറിഫോസ് പ്രയോഗിക്കുക."
    },
    "imidacloprid": {
        "en": "Spray Imidacloprid to control sucking pests like aphids and whiteflies.",
        "ml": "അഫിഡ്, വൈറ്റ്ഫ്ലൈ പോലുള്ള കീടങ്ങൾ നിയന്ത്രിക്കാൻ ഇമിഡാക്ലോപ്രിഡ് സ്പ്രേ ചെയ്യുക."
    },
    "spinosad": {
        "en": "Use Spinosad against caterpillars and thrips.",
        "ml": "കാറ്റർപില്ലർ, ത്രിപ്സ് എന്നിവയ്ക്കെതിരെ സ്പിനോസാഡ് പ്രയോഗിക്കുക."
    },
    "fipronil": {
        "en": "Spray Fipronil for thrips and termites.",
        "ml": "ത്രിപ്സ്, ഉളുവൻ കീടങ്ങൾക്ക് ഫിപ്രോണിൽ സ്പ്രേ ചെയ്യുക."
    },
    "emamectin benzoate": {
        "en": "Spray Emamectin Benzoate against pod borer.",
        "ml": "പയർവിത്ത് കുത്തുന്ന കീടങ്ങൾക്ക് എമാമെക്ടിൻ ബെൻസോയേറ്റ് സ്പ്രേ ചെയ്യുക."
    },
    "buprofezin": {
        "en": "Use Buprofezin to control brown planthopper in rice.",
        "ml": "നെല്ലിൽ ബ്രൗൺ പ്ലാൻറ്റ്ഹോപ്പർ നിയന്ത്രിക്കാൻ ബുപ്രോഫെസിൻ ഉപയോഗിക്കുക."
    },
    "dimethoate": {
        "en": "Apply Dimethoate to control aphids.",
        "ml": "അഫിഡുകൾ നിയന്ത്രിക്കാൻ ഡിമെതോേറ്റ് പ്രയോഗിക്കുക."
    },
    "acetamiprid": {
        "en": "Spray Acetamiprid for sucking pests in cotton and vegetables.",
        "ml": "കാട്ടൺ, പച്ചക്കറികൾ എന്നിവയിൽ സക്കിങ് കീടങ്ങൾക്ക് ആസിറ്റാമിപ്രിഡ് സ്പ്രേ ചെയ്യുക."
    },
    "thiamethoxam": {
        "en": "Use Thiamethoxam for whitefly and jassids.",
        "ml": "വൈറ്റ്ഫ്ലൈ, ജാസിഡ് എന്നിവയ്ക്കായി തിയാമെതോക്സാം ഉപയോഗിക്കുക."
    },
    "quinolphos": {
        "en": "Apply Quinolphos against stem borers.",
        "ml": "സ്റ്റം ബോറർ നിയന്ത്രിക്കാൻ ക്വിനോൽഫോസ് പ്രയോഗിക്കുക."
    },
    "lambda cyhalothrin": {
        "en": "Spray Lambda Cyhalothrin for bollworms.",
        "ml": "ബോൾവർം നിയന്ത്രിക്കാൻ ലാംഡ സൈഹലോത്രിൻ സ്പ്രേ ചെയ്യുക."
    },
    "cypermethrin": {
        "en": "Use Cypermethrin against fruit borers.",
        "ml": "ഫ്രൂട്ട് ബോറർ രോഗത്തിന് സൈപെർമെട്രിൻ ഉപയോഗിക്കുക."
    },
    "malathion": {
        "en": "Spray Malathion for general insect control.",
        "ml": "പൊതുവായ കീടങ്ങൾ നിയന്ത്രിക്കാൻ മലാത്തിയൻ സ്പ്രേ ചെയ്യുക."
    },

    # Add remaining pesticides up to 50...
    # (Bt, neem oil, neem-based pesticides, chlorantraniliprole, cartap hydrochloride, profenophos, etc.)

    "kharif": {
        "en": "Rice, Maize, Cotton, Soybean, Sugarcane, Groundnut, Millets",
        "ml": "അരി, മൈസ്, പരുത്തി, സോയാബീൻ, കരിമ്പ്, നിലക്കടല, ചെറുതാന്യങ്ങൾ"
    },
    "rabi": {
        "en": "Wheat, Barley, Mustard, Pea, Gram, Linseed",
        "ml": "ഗോതമ്പ്, ബാർലി, കടുക്, പയർ, ചെറുപയർ, ആവിഞ്ഞിറച്ചി"
    },
    "zaid": {
        "en": "Watermelon, Muskmelon, Cucumber, Vegetables, Fodder crops",
        "ml": "തണ്ണിമത്തൻ, മസ്ക്മെലൺ, വെള്ളരി, പച്ചക്കറികൾ, മൃഗങ്ങൾക്കുള്ള തീറ്റവിളകൾ"
    },
    
    "january": {
        "en": "Wheat, Barley, Mustard, Gram, Pea (Rabi crops).",
        "ml": "ഗോതമ്പ്, ബാർലി, കടുക്, ചെറുപയർ, പയർ (റബി വിളകൾ)."
    },
    "february": {
        "en": "Wheat, Barley, Mustard, Gram, Linseed.",
        "ml": "ഗോതമ്പ്, ബാർലി, കടുക്, ചെറുപയർ, ആവിഞ്ഞിറച്ചി."
    },
    "march": {
        "en": "Wheat harvesting, start of summer vegetables: Cucumber, Tomato, Okra.",
        "ml": "ഗോതമ്പ് കൊയ്യൽ, വേനൽക്കാല പച്ചക്കറികൾ: വെള്ളരി, തക്കാളി, വെണ്ട."
    },
    "april": {
        "en": "Zaid crops: Watermelon, Muskmelon, Cucumber, Fodder crops.",
        "ml": "സൈദ് വിളകൾ: തണ്ണിമത്തൻ, മസ്ക്മെലൺ, വെള്ളരി, മൃഗങ്ങൾക്ക് തീറ്റവിളകൾ."
    },
    "may": {
        "en": "Zaid crops continue: Watermelon, Muskmelon, Pumpkin, Summer vegetables.",
        "ml": "സൈദ് വിളകൾ: തണ്ണിമത്തൻ, മസ്ക്മെലൺ, മത്തങ്ങ, വേനൽക്കാല പച്ചക്കറികൾ."
    },
    "june": {
        "en": "Start of Kharif crops: Rice, Maize, Cotton, Soybean, Groundnut.",
        "ml": "കറിഫ് വിളകൾ തുടങ്ങുന്നു: അരി, മൈസ്, പരുത്തി, സോയാബീൻ, നിലക്കടല."
    },
    "july": {
        "en": "Kharif crops growing: Rice, Maize, Millets, Cotton, Sugarcane.",
        "ml": "കറിഫ് വിളകൾ വളരുന്നു: അരി, മൈസ്, ചെറുതാന്യങ്ങൾ, പരുത്തി, കരിമ്പ്."
    },
    "august": {
        "en": "Kharif crops continue: Rice, Maize, Millets, Pulses, Groundnut.",
        "ml": "കറിഫ് വിളകൾ: അരി, മൈസ്, ചെറുതാന്യങ്ങൾ, പയർവർഗങ്ങൾ, നിലക്കടല."
    },
    "september": {
        "en": "Harvesting starts: Rice, Maize, Cotton, Groundnut.",
        "ml": "കൊയ്യൽ തുടങ്ങുന്നു: അരി, മൈസ്, പരുത്തി, നിലക്കടല."
    },
    "october": {
        "en": "Rabi season begins: Wheat, Barley, Mustard, Gram.",
        "ml": "റബി സീസൺ തുടങ്ങുന്നു: ഗോതമ്പ്, ബാർലി, കടുക്, ചെറുപയർ."
    },
    "november": {
        "en": "Rabi crops sown: Wheat, Barley, Mustard, Pea, Gram.",
        "ml": "റബി വിളകൾ വിതയ്‌ക്കുന്നു: ഗോതമ്പ്, ബാർലി, കടുക്, പയർ, ചെറുപയർ."
    },
    "december": {
        "en": "Rabi crops growing: Wheat, Barley, Mustard, Gram, Linseed.",
        "ml": "റബി വിളകൾ വളരുന്നു: ഗോതമ്പ്, ബാർലി, കടുക്, ചെറുപയർ, ആവിഞ്ഞിറച്ചി."
    },
}


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data.get("query", "").lower()

    for key, value in solutions.items():
        if key in query:
            return jsonify({"reply_en": value["en"], "reply_ml": value["ml"]})

    return jsonify({
        "reply_en": "Sorry, I don’t have an exact solution.",
        "reply_ml": "ക്ഷമിക്കണം, കൃത്യമായ പരിഹാരം ലഭ്യമല്ല."
    })

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify



# Month wise crops data (English + Malayalam)
month_crops = {
    "january": {
        "en": "Wheat, Barley, Mustard, Gram, Pea (Rabi crops).",
        "ml": "ഗോതമ്പ്, ബാർലി, കടുക്, ചെറുപയർ, പയർ (റബി വിളകൾ)."
    },
    "february": {
        "en": "Wheat, Barley, Mustard, Gram, Linseed.",
        "ml": "ഗോതമ്പ്, ബാർലി, കടുക്, ചെറുപയർ, ആവിഞ്ഞിറച്ചി."
    },
    "march": {
        "en": "Wheat harvesting, start of summer vegetables: Cucumber, Tomato, Okra.",
        "ml": "ഗോതമ്പ് കൊയ്യൽ, വേനൽക്കാല പച്ചക്കറികൾ: വെള്ളരി, തക്കാളി, വെണ്ട."
    },
    "april": {
        "en": "Zaid crops: Watermelon, Muskmelon, Cucumber, Fodder crops.",
        "ml": "സൈദ് വിളകൾ: തണ്ണിമത്തൻ, മസ്ക്മെലൺ, വെള്ളരി, മൃഗങ്ങൾക്ക് തീറ്റവിളകൾ."
    },
    "may": {
        "en": "Zaid crops continue: Watermelon, Muskmelon, Pumpkin, Summer vegetables.",
        "ml": "സൈദ് വിളകൾ: തണ്ണിമത്തൻ, മസ്ക്മെലൺ, മത്തങ്ങ, വേനൽക്കാല പച്ചക്കറികൾ."
    },
    "june": {
        "en": "Start of Kharif crops: Rice, Maize, Cotton, Soybean, Groundnut.",
        "ml": "കറിഫ് വിളകൾ തുടങ്ങുന്നു: അരി, മൈസ്, പരുത്തി, സോയാബീൻ, നിലക്കടല."
    },
    "july": {
        "en": "Kharif crops growing: Rice, Maize, Millets, Cotton, Sugarcane.",
        "ml": "കറിഫ് വിളകൾ വളരുന്നു: അരി, മൈസ്, ചെറുതാന്യങ്ങൾ, പരുത്തി, കരിമ്പ്."
    },
    "august": {
        "en": "Kharif crops continue: Rice, Maize, Millets, Pulses, Groundnut.",
        "ml": "കറിഫ് വിളകൾ: അരി, മൈസ്, ചെറുതാന്യങ്ങൾ, പയർവർഗങ്ങൾ, നിലക്കടല."
    },
    "september": {
        "en": "Harvesting starts: Rice, Maize, Cotton, Groundnut.",
        "ml": "കൊയ്യൽ തുടങ്ങുന്നു: അരി, മൈസ്, പരുത്തി, നിലക്കടല."
    },
    "october": {
        "en": "Rabi season begins: Wheat, Barley, Mustard, Gram.",
        "ml": "റബി സീസൺ തുടങ്ങുന്നു: ഗോതമ്പ്, ബാർലി, കടുക്, ചെറുപയർ."
    },
    "november": {
        "en": "Rabi crops sown: Wheat, Barley, Mustard, Pea, Gram.",
        "ml": "റബി വിളകൾ വിതയ്‌ക്കുന്നു: ഗോതമ്പ്, ബാർലി, കടുക്, പയർ, ചെറുപയർ."
    },
    "december": {
        "en": "Rabi crops growing: Wheat, Barley, Mustard, Gram, Linseed.",
        "ml": "റബി വിളകൾ വളരുന്നു: ഗോതമ്പ്, ബാർലി, കടുക്, ചെറുപയർ, ആവിഞ്ഞിറച്ചി."
    },
    # Ranges
    "june-september": {
        "en": "Kharif crops: Rice, Maize, Cotton, Soybean, Sugarcane, Groundnut, Millets.",
        "ml": "കറിഫ് വിളകൾ: അരി, മൈസ്, പരുത്തി, സോയാബീൻ, കരിമ്പ്, നിലക്കടല, ചെറുതാന്യങ്ങൾ."
    },
    "october-march": {
        "en": "Rabi crops: Wheat, Barley, Mustard, Pea, Gram, Linseed.",
        "ml": "റബി വിളകൾ: ഗോതമ്പ്, ബാർലി, കടുക്, പയർ, ചെറുപയർ, ആവിഞ്ഞിറച്ചി."
    },
    "april-june": {
        "en": "Zaid crops: Watermelon, Muskmelon, Cucumber, Vegetables, Fodder crops.",
        "ml": "സൈദ് വിളകൾ: തണ്ണിമത്തൻ, മസ്ക്മെലൺ, വെള്ളരി, പച്ചക്കറികൾ, മൃഗങ്ങൾക്ക് തീറ്റവിളകൾ."
    }
}

@app.route("/api/crops/<month>", methods=["GET"])
def get_crops(month):
    month = month.lower()
    if month in month_crops:
        return jsonify({month: month_crops[month]})
    else:
        return jsonify({
            "error": "Invalid input. Use months like 'january' or ranges like 'june-september'."
        })

if __name__ == "__main__":
    app.run(debug=True)