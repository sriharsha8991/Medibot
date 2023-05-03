import streamlit as st
import random


medicine = {
    "headache": "paracetamol",
    "cough": "Dolo250",
    "fever": "dolo650",
    "sore throat": "benzocaine throat lozenges",
    "nasal congestion": "oxymetazoline",
    "runny nose": "chlorpheniramine",
    "sneezing": "loratadine",
    "earache": "ibuprofen",
    "toothache": "acetaminophen",
    "stomach ache": "antacids",
    "nausea": "ondansetron",
    "vomiting": "promethazine",
    "diarrhea": "loperamide",
    "constipation": "docusate sodium",
    "back pain": "ibuprofen",
    "joint pain": "acetaminophen",
    "muscle pain": "naproxen",
    "menstrual cramps": "ibuprofen",
    "irregular menstruation": "hormonal birth control",
    "anxiety": "alprazolam",
    "depression": "sertraline",
    "insomnia": "zolpidem",
    "migraine": "sumatriptan",
    "allergic reaction": "epinephrine",
    "fatigue": "caffeine",
    "dizziness": "meclizine",
    "shortness of breath": "albuterol",
    "chest pain": "aspirin",
    "heartburn": "omeprazole",
    "indigestion": "simethicone",
    "acid reflux": "ranitidine",
    "high blood pressure": "amlodipine",
    "low blood pressure": "fludrocortisone",
    "hypoglycemia": "glucose tablets",
    "hyperglycemia": "insulin",
    "asthma": "fluticasone",
    "bronchitis": "azithromycin",
    "pneumonia": "amoxicillin",
    "sinus infection": "amoxicillin",
    "urinary tract infection": "trimethoprim-sulfamethoxazole",
    "yeast infection": "miconazole",
    "hemorrhoids": "witch hazel",
    "cold sores": "acyclovir",
    "eczema": "hydrocortisone",
    "psoriasis": "coal tar",
    "dry eyes": "artificial tears",
    "conjunctivitis (pink eye)": "erythromycin ointment",
    "athlete's foot": "terbinafine",
    "ringworm": "clotrimazole",
    "jock itch": "miconazole",
    "sunburn": "aloe vera",
    "minor burns": "silver sulfadiazine",
    "cuts and scrapes": "neosporin",
    "insect bites": "hydrocortisone",
    "poison ivy/oak/sumac": "calamine lotion",
    "motion sickness": "dimenhydrinate",
    "vertigo": "meclizine",
    "mild anxiety": "valerian root",
    "panic attacks": "alprazolam",
    "ADHD": "methylphenidate",
    "bipolar disorder": "lithium",
    "schizophrenia": "risperidone",
    "gout": "colchicine",
    "osteoarthritis": "acetaminophen",
    "rheumatoid arthritis": "methotrexate",
    "mild to moderate pain": "ibuprofen",
    "moderate to severe pain": "oxycodone"


}
# Possible responses for the bot
greetings = ["Hey there!", "Hi, how can I help you?", "Hello!","Hey how are you?"]
thanks = ["You're welcome!", "happy to help you!", "Glad to be of assistance!"]
unknown = ["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure what you mean."]

# Define the bot's conversation flow
def conversation():
    st.sidebar.markdown("""# Medi_Bot
                        ### By Sriharsha Velicheti""")
    st.sidebar.markdown("---")
    st.sidebar.markdown("""* HEADACHE
* COUGH
* FEVER
* SORE THROAT
* NASAL CONGESTION
* RUNNY NOSE
* SNEEZING
* EARACHE
* TOOTHACHE
* STOMACH ACHE
* NAUSEA
* VOMITING
* DIARRHEA
* CONSTIPATION
* BACK PAIN
* JOINT PAIN
* MUSCLE PAIN
* MENSTRUAL CRAMPS
* IRREGULAR MENSTRUATION
* ANXIETY
* DEPRESSION
* INSOMNIA
* MIGRAINE
* ALLERGIC REACTION
* FATIGUE
* DIZZINESS
* SHORTNESS OF BREATH
* CHEST PAIN
* HEARTBURN
* INDIGESTION
* ACID REFLUX
* HIGH BLOOD PRESSURE
* LOW BLOOD PRESSURE
* HYPOGLYCEMIA
* HYPERGLYCEMIA
* ASTHMA
* BRONCHITIS
* PNEUMONIA
* SINUS INFECTION
* URINARY TRACT INFECTION
* YEAST INFECTION
* HEMORRHOIDS
* COLD SORES
* ECZEMA
* PSORIASIS
* DRY EYES
* CONJUNCTIVITIS (PINK EYE)
* ATHLETE'S FOOT
* RINGWORM
* JOCK ITCH
* SUNBURN
* MINOR BURNS
* CUTS AND SCRAPES
* INSECT BITES
* POISON IVY/OAK/SUMAC
* MOTION SICKNESS
* VERTIGO
* MILD ANXIETY
* PANIC ATTACKS
* ADHD
* BIPOLAR DISORDER
* SCHIZOPHRENIA
* GOUT
* OSTEOARTHRITIS
* RHEUMATOID ARTHRITIS
* MILD TO MODERATE PAIN
* MODERATE TO SEVERE PAIN
""")

    st.title("Medi_Bot")

    # Greet the user
    st.write(random.choice(greetings))


    # Ask for the user's symptom

    symptom = st.text_input(f"What symptom or problem are you experiencing?",placeholder="Enter your disease from the given database")
    if symptom:
        if symptom.lower() in medicine.keys():
            # Check if the symptom is in the list of known symptoms
            
            
            if symptom.lower() in medicine:
                st.write(f"The recommended medicine for {symptom.lower()} is '{medicine[symptom.lower()]}.'")

                # Ask how long the user has been experiencing the symptom
                days = st.text_input("How long have you been experiencing this symptom (in days)?",placeholder='Enter a number')

                if days:
                    try:
                        days = int(days)
                        if days <= 3:
                            st.write("You can take the prescribed medicine for 3 days, 2 doses per day. You should start feeling better soon!")
                        else:
                            st.write("You should consult a doctor to get a proper diagnosis for your condition.")
                            st.write(random.choice(thanks))
                    except ValueError:
                        st.write("Please enter a valid number of days.")
                        
            else:
                st.write(random.choice(unknown))
        else:
            st.write("Sorry please try to match the disease in our database")
            st.write(random.choice(thanks))


    # Say goodbye
    
        

if __name__ == "__main__":
    conversation()

