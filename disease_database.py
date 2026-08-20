"""
Disease Information Database
Contains comprehensive information about plant diseases including
descriptions, symptoms, treatments, and prevention methods.
"""

DISEASE_DATABASE = {
    'Healthy': {
        'name': 'Healthy Plant',
        'description': 'The plant shows no signs of disease and is in good health.',
        'severity_level': 'None',
        'severity_color': '#00AA00',  # Green
        'symptoms': [
            'Green and vibrant foliage',
            'Normal growth pattern',
            'No visible spots or lesions',
            'Strong stem and leaves',
            'No discoloration'
        ],
        'causes': 'N/A - Plant is disease-free',
        'treatments': [
            'Continue regular watering schedule',
            'Maintain proper sunlight exposure',
            'Ensure good soil drainage',
            'Apply balanced fertilizer monthly'
        ],
        'prevention': [
            'Water at the base to keep leaves dry',
            'Remove dead leaves promptly',
            'Maintain good air circulation',
            'Avoid overcrowding plants',
            'Monitor regularly for early signs of disease'
        ],
        'recommended_actions': [
            'Continue current care routine',
            'No treatment needed',
            'Regular monitoring recommended'
        ],
        'time_to_recovery': 'N/A',
        'crop_loss_risk': 'Low (0-5%)'
    },
    
    'Early_Blight': {
        'name': 'Early Blight',
        'description': 'Early Blight is a fungal disease caused by Alternaria solani. It primarily affects the older leaves of tomato plants and can cause significant crop loss if left untreated.',
        'severity_level': 'Medium',
        'severity_color': '#FFA500',  # Orange
        'symptoms': [
            'Small, dark, circular spots on lower leaves',
            'Spots with concentric ring pattern (target-like)',
            'Yellowing around the affected areas',
            'Spots gradually enlarge (0.25-0.5 inches)',
            'Leaves may drop off prematurely',
            'Starts on lower leaves and progresses upward',
            'Brown lesions with yellow halos'
        ],
        'causes': 'Fungal infection caused by Alternaria solani spores, favored by warm, wet conditions',
        'treatments': [
            'Remove affected leaves immediately (cut 6 inches below lowest affected leaf)',
            'Apply fungicide: copper fungicide or mancozeb',
            'Spray every 7-10 days during growing season',
            'Use sulfur-based fungicides for organic approach',
            'Increase air circulation by pruning lower branches',
            'Water at soil level, avoid wetting foliage'
        ],
        'prevention': [
            'Plant disease-resistant varieties',
            'Space plants adequately for air circulation',
            'Use drip irrigation or soaker hoses',
            'Mulch soil to prevent soil splash',
            'Remove infected plant debris',
            'Rotate crops yearly',
            'Avoid handling wet plants',
            'Clean tools between plants'
        ],
        'recommended_actions': [
            'Immediately remove infected leaves',
            'Apply fungicide treatment',
            'Improve air circulation',
            'Adjust watering method',
            'Monitor plant daily'
        ],
        'time_to_recovery': '2-4 weeks with treatment',
        'crop_loss_risk': 'Medium (15-40%)',
        'spreads_via': 'Water splash, contaminated tools, wind',
        'weather_conditions': 'Warm (65-80°F) and humid environments'
    },
    
    'Late_Blight': {
        'name': 'Late Blight',
        'description': 'Late Blight is a serious fungal disease caused by Phytophthora infestans. It is one of the most destructive plant diseases worldwide and can destroy entire crops rapidly, especially in cool, wet conditions.',
        'severity_level': 'High',
        'severity_color': '#DD0000',  # Red
        'symptoms': [
            'Water-soaked spots on leaves that appear oily',
            'Spots start as small, dark patches',
            'White mold appears on undersides of leaves',
            'Spots enlarge rapidly in wet conditions',
            'Entire leaf can turn black and die',
            'Stems show long, sunken lesions',
            'Fruit develops brown, sunken lesions',
            'Rapid plant collapse possible within days',
            'Dead leaves remain attached to plant'
        ],
        'causes': 'Oomycete pathogen (Phytophthora infestans) that thrives in cool (50-70°F), wet conditions',
        'treatments': [
            'Remove and destroy affected plant parts completely',
            'Apply copper-based fungicides immediately',
            'Use Chlorothalonil or mancozeb fungicides',
            'Apply anti-oomycete fungicides: Metalaxyl or Ridomil',
            'Spray every 5-7 days in wet conditions',
            'May require severe pruning of affected areas',
            'In severe cases, destroy entire plant',
            'Increase air circulation - prune heavily'
        ],
        'prevention': [
            'Plant resistant varieties (highly recommended)',
            'Avoid overhead irrigation',
            'Use drip irrigation exclusively',
            'Water early morning at ground level',
            'Improve drainage in growing area',
            'Remove lower leaves to improve air flow',
            'Avoid planting in low areas that collect moisture',
            'Clean up all plant debris at end of season',
            'Rotate crops for 3+ years',
            'Scout plants regularly during wet weather'
        ],
        'recommended_actions': [
            'URGENT: Remove infected plant parts immediately',
            'Apply fungicide treatment within 24 hours',
            'Dramatically improve air circulation',
            'Stop overhead watering completely',
            'Use ground-level irrigation only',
            'Monitor plant every day for spread',
            'Consider removing entire plant if >50% infected',
            'Isolate from other plants'
        ],
        'time_to_recovery': '3-6 weeks with aggressive treatment (may not recover)',
        'crop_loss_risk': 'Very High (50-100%)',
        'spreads_via': 'Water splash, wind, contaminated soil/tools, water-borne spores',
        'weather_conditions': 'Cool (50-70°F), wet, humid - spreads rapidly in these conditions',
        'critical_note': 'This is the most dangerous disease - immediate action required!'
    }
}


def get_disease_info(disease_class):
    """
    Retrieve disease information by class name.
    
    Args:
        disease_class (str): Disease class name (e.g., 'Early_Blight', 'Late_Blight', 'Healthy')
    
    Returns:
        dict: Disease information dictionary or None if not found
    """
    return DISEASE_DATABASE.get(disease_class, None)


def get_all_diseases():
    """
    Get all diseases in the database.
    
    Returns:
        dict: Complete disease database
    """
    return DISEASE_DATABASE


def format_disease_report(disease_class, confidence=None):
    """
    Format a detailed disease report.
    
    Args:
        disease_class (str): Disease class name
        confidence (float): Confidence score (0-1)
    
    Returns:
        str: Formatted text report
    """
    disease_info = get_disease_info(disease_class)
    
    if not disease_info:
        return f"Unknown disease class: {disease_class}"
    
    confidence_pct = (confidence * 100) if confidence else 0
    
    report = f"""
╔════════════════════════════════════════════════════════════════════════════╗
║                       PLANT DISEASE DETECTION REPORT                       ║
╚════════════════════════════════════════════════════════════════════════════╝

📋 DIAGNOSIS INFORMATION
{'─' * 76}
Disease Detected:        {disease_info['name']}
Confidence Level:        {confidence_pct:.2f}%
Severity Level:          {disease_info['severity_level']}

📝 DESCRIPTION
{'─' * 76}
{disease_info['description']}

🔍 SYMPTOMS OBSERVED
{'─' * 76}
"""
    for i, symptom in enumerate(disease_info['symptoms'], 1):
        report += f"  {i}. {symptom}\n"
    
    report += f"""
🦠 DISEASE CAUSE
{'─' * 76}
{disease_info['causes']}

💊 TREATMENT OPTIONS
{'─' * 76}
"""
    for i, treatment in enumerate(disease_info['treatments'], 1):
        report += f"  {i}. {treatment}\n"
    
    report += f"""
🛡️  PREVENTION METHODS
{'─' * 76}
"""
    for i, prevention in enumerate(disease_info['prevention'], 1):
        report += f"  {i}. {prevention}\n"
    
    report += f"""
⚠️  RECOMMENDED ACTIONS (Priority)
{'─' * 76}
"""
    for i, action in enumerate(disease_info['recommended_actions'], 1):
        report += f"  {i}. {action}\n"
    
    report += f"""
📊 RISK ASSESSMENT
{'─' * 76}
Recovery Time:           {disease_info['time_to_recovery']}
Crop Loss Risk:          {disease_info['crop_loss_risk']}
"""
    
    if 'spreads_via' in disease_info:
        report += f"Spreads Via:             {disease_info['spreads_via']}\n"
    
    if 'weather_conditions' in disease_info:
        report += f"Favorable Conditions:    {disease_info['weather_conditions']}\n"
    
    if 'critical_note' in disease_info:
        report += f"\n🚨 CRITICAL NOTE: {disease_info['critical_note']}\n"
    
    report += f"\n{'═' * 76}\n"
    
    return report


def get_severity_color(disease_class):
    """
    Get the color code for disease severity visualization.
    
    Args:
        disease_class (str): Disease class name
    
    Returns:
        str: Hex color code
    """
    disease_info = get_disease_info(disease_class)
    return disease_info['severity_color'] if disease_info else '#888888'
