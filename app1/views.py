from django.shortcuts import render 
from . import Virtual_Doctor_Copy1 as vd



# Create your views here.
def first(request):
    return render (request,'index.html')

def checkup(request):
    return render (request,'project.html')

def virtualdoc(request):
	dict2={}
	#arr=['blister', 'irritation_in_anus', 'diarrhoea  ', 'watering_from_eyes', 'fluid_overload', 'sweating', 'bladder_discomfort', 'headach', 'enlarged_thyroid', 'weakness_of_one_body_side', 'polyuria', 'weight_loss', 'toxic_look_(typhos)', 'excessive_hunger', 'congestion', 'cold_hands_and_feets', 'yellow_urine', 'ails', 'itching', 'continuous_sneezing', 'drying_and_tingling_lips', 'continuous_feel_of_urine', 'neck_pain', 'belly_pain', 'pus_filled_pimples', 'passage_of_gases', 'lethargy', 'loss_of_smell', 'weight_gain', 'silver_like_dusting', 'swollen_legs', 'shivering', 'prominent_veins_on_calf', 'pain_behind_the_eyes', 'pain_during_bowel_movements', 'stiff_neck', 'puffy_face_and_eyes', 'sunken_eyes', 'unsteadiness', 'throat_irritation', 'small_dents_in_nails', 'yellowing_of_eyes', 'chest_pain', 'bloody_stool', 'redness_of_eyes', 'dischromic _patches', 'nodal_skin_eruptions', 'runny_nose', 'loss_of_balance', 'constipation', 'nausea', 'mucoid_sputum', 'skin_peeling', 'joint_pain ', 'passages of gasses', 'foul_smell_ofurine', 'indigestion', 'dizziness', 'red_sore_around_nose', 'sinus_pressure', 'fast_heart_rate', 'hip_joint_pain', 'spinning_movements', 'chills', 'muscle_weakness', 'swollen_blood_vessels', 'spotting_urination', 'slurred_speech', 'visual_disturbances', 'breathlessness', 'burning_micturition', 'muscle_pain', 'coma', 'diarrhoea',
#'cramps', 'scurring', 'anxiety', 'internal_itching', 'stomach_bleeding', 'dehydration', 'loss_of_appetite', 'high_fever', 'vomiting', 'increased_appetite', 'restlessness', 'blood_in_sputum', 'bruising', 'belly_pain', 'depression', 'mild_fever', 'yellow_crust_ooze', 'dark_urine', 'diarrhoea ', 'obesity', 'irregular_sugar_level', 'receiving_unsterile_injections', 'acidity', 'history_of_alcohol_consumption', 'altered_sensorium', 'back_pain', 'skin_rash', 'painful_walking', 'brittle_n', 'toxic_look_(typhos) ', 'yellowish_skin', 'patches_in_throat', 'swelled_lymph_nodes', 'ulcers_on_tongue', 'swelling_of_stomach', 'stomach_pain uation', 'red_spots_over_body', 'extra_marital_contacts', 'distention_of_stomach', 'acute_liver_failure', 'blurred_and_distorted_vision', 'movement_stiffness', 'cough', 'palpitations', 'abnormal_menstruation', 'muscle_wasting', 'swelling_joints', 'knee_pain', 'joint_pain', 'weakness_in_limbs', 'lack_of_concentration', 'blackheads', 'receiving_blood_transfusion', 'irritability', 'stomach_pain', 'phlegm', 'pain_in_anal_region', 'malaise', 'rusty_sputum']
	#if request.method == 'POST':
	res=request.GET.getlist('checks[]')
	a=vd.starter(res)
	dict2={'data':a,'symptom':res}
	return render(request,'components.html',dict2)  