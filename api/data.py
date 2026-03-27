qa_data = [
    {
        "question": "lung opacity chest x-ray",
        "answer": """1. Observations:
Increased opacity in the lung field.

2. Possible Findings:
May indicate infection, fluid accumulation, or inflammation.

3. Differential Diagnosis:
- Pneumonia
- Pulmonary edema
- Atelectasis

4. Recommendation:
Clinical correlation and further imaging may be required.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "fracture x-ray",
        "answer": """1. Observations:
Discontinuity or break in bone cortex with a lucent fracture line.

2. Possible Findings:
Indicates bone fracture or crack with possible displacement.

3. Differential Diagnosis:
- Acute fracture
- Stress fracture
- Pathological fracture

4. Recommendation:
Orthopedic evaluation and possible immobilization advised.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "brain hemorrhage ct",
        "answer": """1. Observations:
Hyperdense (bright) region within the brain parenchyma on non-contrast CT.

2. Possible Findings:
Suggestive of acute intracranial bleeding.

3. Differential Diagnosis:
- Intracerebral hemorrhage
- Subdural hematoma
- Epidural hematoma

4. Recommendation:
Immediate clinical evaluation and urgent neurosurgical review required.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "hypodense lesion ct",
        "answer": """1. Observations:
Area of lower density (dark) compared to surrounding brain tissue on CT.

2. Possible Findings:
May indicate fluid accumulation, cyst, or ischemic tissue damage.

3. Differential Diagnosis:
- Infarction (ischemic stroke)
- Arachnoid or epidermoid cyst
- Necrotic tumor

4. Recommendation:
Further imaging with contrast or MRI diffusion sequences may clarify the nature.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "hyperintensity mri",
        "answer": """1. Observations:
Bright (hyperintense) signal area on T2 or FLAIR weighted MRI sequences.

2. Possible Findings:
Indicates increased water content, inflammation, or abnormal tissue.

3. Differential Diagnosis:
- Vasogenic edema
- Demyelination (Multiple Sclerosis)
- Tumor or metastasis

4. Recommendation:
Correlation with DWI to exclude acute infarction; contrast-enhanced MRI if mass lesion suspected.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "ligament tear mri",
        "answer": """1. Observations:
Disruption or signal discontinuity within the ligament on T2-weighted MRI.

2. Possible Findings:
Suggests partial or complete ligament injury or tear.

3. Differential Diagnosis:
- Partial tear
- Complete tear
- Mucoid degeneration / sprain

4. Recommendation:
Orthopedic consultation recommended; clinical stability tests (e.g., Lachman for ACL).

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "pleural effusion x-ray",
        "answer": """1. Observations:
Blunting of the costophrenic angle; meniscus sign; fluid-level opacity.

2. Possible Findings:
Fluid accumulation in the pleural space.

3. Differential Diagnosis:
- Transudative effusion (CHF, cirrhosis)
- Exudative effusion (pneumonia, malignancy)
- Hemothorax

4. Recommendation:
Lateral decubitus view or ultrasound for volume quantification and assessment.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "kidney stones ct",
        "answer": """1. Observations:
Hyperdense (bright) structures in the renal pelvis, ureter, or bladder on non-contrast CT.

2. Possible Findings:
Indicates presence of urinary calculi causing potential obstruction.

3. Differential Diagnosis:
- Renal calculi (calcium oxalate, uric acid)
- Ureteric stones
- Phleboliths (pelvic veins)

4. Recommendation:
Urological consultation advised; assess for hydronephrosis and degree of obstruction.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "brain tumor mri",
        "answer": """1. Observations:
Abnormal mass with altered signal intensity on T1, T2, and FLAIR MRI sequences.

2. Possible Findings:
Suggests presence of intracranial neoplasm with possible surrounding edema.

3. Differential Diagnosis:
- Primary glioma (GBM, astrocytoma)
- Brain metastasis
- Meningioma

4. Recommendation:
Contrast-enhanced MRI for further characterization; neurosurgical and oncology referral.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "stroke ct findings",
        "answer": """1. Observations:
Hypodense (dark) or hyperdense (bright) regions in brain territory on non-contrast CT.

2. Possible Findings:
Indicates ischemic or hemorrhagic stroke depending on density pattern.

3. Differential Diagnosis:
- Ischemic stroke (hypodense)
- Hemorrhagic stroke (hyperdense)
- Hyperdense MCA sign (dense clot)

4. Recommendation:
Immediate medical attention required; CTA for vessel occlusion assessment (thrombectomy planning).

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "pneumothorax x-ray",
        "answer": """1. Observations:
Visible visceral pleural line with absence of lung markings peripheral to it.

2. Possible Findings:
Indicates air in the pleural space causing lung collapse.

3. Differential Diagnosis:
- Simple spontaneous pneumothorax
- Traumatic pneumothorax
- Tension pneumothorax (tracheal shift present)

4. Recommendation:
Check for tracheal deviation (tension); immediate clinical attention required.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "osteoporosis x-ray",
        "answer": """1. Observations:
Reduced bone density with thinning of the cortical bone and trabeculae.

2. Possible Findings:
Indicates weakened bone mineral density with fracture risk.

3. Differential Diagnosis:
- Osteoporosis
- Osteopenia
- Hyperparathyroidism

4. Recommendation:
Bone density test (DEXA scan) recommended; endocrinology referral.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "pulmonary embolism ct",
        "answer": """1. Observations:
Intraluminal filling defects in the pulmonary arteries on CTPA.

2. Possible Findings:
Indicates blockage of pulmonary blood flow by thrombus.

3. Differential Diagnosis:
- Acute pulmonary embolism
- Chronic thromboembolic disease
- Tumor embolus

4. Recommendation:
Urgent anticoagulation assessment; evaluate for right heart strain markers on CT.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "appendicitis ct scan",
        "answer": """1. Observations:
Enlarged appendix (>6mm diameter) with wall thickening and periappendiceal fat stranding.

2. Possible Findings:
Suggests acute inflammation of the appendix.

3. Differential Diagnosis:
- Acute appendicitis
- Periappendiceal abscess
- Mesenteric adenitis

4. Recommendation:
Surgical consultation recommended; correlate with Alvarado score.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "stroke mri findings",
        "answer": """1. Observations:
Diffusion restriction (bright DWI + dark ADC) in the affected brain territory.

2. Possible Findings:
Indicates acute ischemic stroke with cytotoxic edema.

3. Differential Diagnosis:
- Acute ischemic stroke
- Transient ischemic attack (TIA)
- Hypoglycemia (mimics stroke on MRI)

4. Recommendation:
Immediate neurological evaluation; CTA for large vessel occlusion assessment.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "meniscus tear mri",
        "answer": """1. Observations:
Abnormal T2 signal reaching the articular surface of the meniscus on knee MRI.

2. Possible Findings:
Suggests meniscal tear or degeneration (Grade 3 signal).

3. Differential Diagnosis:
- Medial or lateral meniscus tear
- Bucket-handle tear (if displaced fragment)
- Degenerative meniscal changes

4. Recommendation:
Orthopedic consultation advised; consider arthroscopy if symptoms persist.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "scoliosis x-ray",
        "answer": """1. Observations:
Lateral curvature of the spine exceeding 10 degrees on standing radiograph.

2. Possible Findings:
Indicates abnormal spinal alignment with possible rotational deformity.

3. Differential Diagnosis:
- Adolescent idiopathic scoliosis
- Degenerative scoliosis (adult)
- Neuromuscular scoliosis

4. Recommendation:
Measure Cobb angle on standing full-spine radiographs; spine specialist consultation.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "liver cirrhosis ct",
        "answer": """1. Observations:
Nodular and irregular liver surface contour; hypertrophy of caudate lobe; splenomegaly; ascites.

2. Possible Findings:
Suggests chronic liver parenchymal damage with portal hypertension.

3. Differential Diagnosis:
- Liver cirrhosis
- Chronic hepatitis
- Budd-Chiari syndrome

4. Recommendation:
HCC screening with multiphasic CT or MRI; hepatology consultation.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "spinal cord compression mri",
        "answer": """1. Observations:
Narrowed spinal canal with focal T2 high signal change within the spinal cord.

2. Possible Findings:
Indicates myelopathy due to external compression on the cord.

3. Differential Diagnosis:
- Disc herniation
- Extradural tumor or metastasis
- Spinal stenosis

4. Recommendation:
Urgent neurological consultation required if acute neurological deficit is present.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "calcification ct imaging",
        "answer": """1. Observations:
Focal high-density (bright) areas with Hounsfield Units >100 HU in soft tissue.

2. Possible Findings:
Indicates calcium deposits within tissue or vessels.

3. Differential Diagnosis:
- Dystrophic calcification (chronic infection, old hematoma)
- Metastatic calcification (hypercalcemia)
- Tumoral calcification (e.g., meningioma, teratoma)

4. Recommendation:
Clinical context is essential; correlate with serum calcium and tissue diagnosis if required.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "mri",
        "answer": """1. Observations:
MRI (Magnetic Resonance Imaging) uses magnetic fields and radio waves — no ionizing radiation.

2. Possible Findings:
Core sequences used in clinical MRI:
- T1: Fat = bright, Water = dark. Best for anatomy.
- T2: Water = bright. Best for pathology (edema, inflammation).
- FLAIR: Suppresses CSF — best for periventricular lesions.
- DWI/ADC: Diffusion restriction — acute ischemia or abscess.
- T1 + Gadolinium: Blood-brain barrier breakdown, tumors.

3. Differential Diagnosis:
MRI is superior for:
- Brain: Tumors, MS, stroke, infections
- Spine: Disc herniation, cord compression
- Joints: Ligament, meniscus, rotator cuff
- Liver and Prostate: Focal lesion characterization

4. Recommendation:
Always confirm metallic implant safety before scanning. Contrast requires renal function check (eGFR >30).

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "x-ray",
        "answer": """1. Observations:
X-Ray (Plain Radiograph) uses ionizing radiation to produce 2D projection images.

2. Possible Findings:
Tissue densities visible on X-Ray:
- White (radiopaque): Bone, metal, contrast media
- Gray: Soft tissue, water, solid organs
- Black (radiolucent): Air (lungs), fat

Common applications:
- Chest (CXR): Pneumonia, effusion, pneumothorax, heart failure
- Bones and Joints: Fractures, dislocations, arthritis
- Abdomen (AXR): Bowel obstruction, free air, calcifications
- Spine: Alignment, compression fractures

3. Differential Diagnosis:
Findings on X-Ray depend on the clinical question:
- Opacity: Consolidation, effusion, atelectasis
- Hyperlucency: Pneumothorax, emphysema
- Bone lesion: Fracture, lytic/sclerotic lesion

4. Recommendation:
Always obtain two views at 90 degrees. PA view is standard for CXR (less magnification than AP).

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "ct",
        "answer": """1. Observations:
CT (Computed Tomography) uses X-rays with computer reconstruction to produce cross-sectional images.

2. Possible Findings:
Hounsfield Units (HU) for tissue identification:
- Air: -1000 HU | Fat: -100 to -50 HU | Water: 0 HU
- Soft tissue: 20-80 HU | Acute blood: 50-80 HU
- Bone: 400-1000 HU

Window settings:
- Brain: W80/L40 | Lung: W1500/L-600 | Bone: W2000/L400

3. Differential Diagnosis:
CT is preferred for:
- Emergency trauma, hemorrhage detection
- Lung: Nodules, HRCT for ILD, CTPA for PE
- Abdomen: Appendicitis, renal stones, aortic pathology
- Head: Stroke, hemorrhage, fractures

4. Recommendation:
Always review CT in multiple windows. Use contrast only when clinically indicated and renal function permits.

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "ct scan",
        "answer": """1. Observations:
CT Scan uses X-rays with computer processing to create high-resolution cross-sectional images.

2. Possible Findings:
Key CT imaging principles:
- Hyperdense (bright): Acute blood, calcium, contrast
- Hypodense (dark): Edema, fat, old infarct, cyst
- Isodense: Same HU as surrounding tissue

3. Differential Diagnosis:
CT scan is best for:
- Head: Hemorrhage vs. ischemia, fractures
- Chest: PE (CTPA), lung nodules, pneumonia
- Abdomen: Appendicitis, kidney stones, bowel
- Vascular: Aortic dissection, aneurysm

4. Recommendation:
CT is fast and widely available. Use for emergencies. Always consider radiation dose (ALARA principle).

This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "CT Contrast safety protocols",
        "answer": """Observations:
Use of iodinated contrast in CT imaging requires patient screening.

Possible Findings:
Risk of allergic reactions or contrast-induced nephropathy.

Differential Considerations:
- Contrast allergy
- Renal impairment
- Previous adverse reactions

Recommendation:
Check renal function (creatinine), ensure hydration, and review allergy history before administration.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "How to identify HRCT Lung patterns",
        "answer": """Observations:
Presence of ground-glass opacities, reticulations, or nodules.

Possible Findings:
Suggests interstitial or inflammatory lung disease.

Differential Diagnosis:
- Interstitial lung disease
- Pulmonary fibrosis
- Infection

Recommendation:
Correlation with clinical history and pulmonary function tests.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "How to evaluate Neck Trauma in CT",
        "answer": """Observations:
Assessment of cervical spine alignment and soft tissues.

Possible Findings:
Fractures, soft tissue swelling, or vascular injury.

Differential Diagnosis:
- Cervical fracture
- Ligament injury
- Hematoma

Recommendation:
Urgent evaluation and stabilization if trauma suspected.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "How to identify a Spine Fracture on CT",
        "answer": """Observations:
Discontinuity in vertebral body or alignment changes.

Possible Findings:
Indicates vertebral fracture.

Differential Diagnosis:
- Compression fracture
- Burst fracture
- Pathological fracture

Recommendation:
Orthopedic or neurosurgical consultation advised.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "How to detect Brain Infarct on CT",
        "answer": """Observations:
Hypodense area in affected brain region.

Possible Findings:
Indicates ischemic infarction.

Differential Diagnosis:
- Ischemic stroke
- Edema
- Old infarct

Recommendation:
Immediate neurological assessment required.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What is the CT Windowing guide for clinicians",
        "answer": """Observations:
Adjustment of window width and level for tissue visualization.

Possible Findings:
Enhances visibility of soft tissue, lung, or bone structures.

Differential Considerations:
- Lung window
- Bone window
- Soft tissue window

Recommendation:
Use appropriate window settings based on diagnostic requirement.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What is the standard CT Urogram protocol",
        "answer": """Observations:
Multiphasic imaging including non-contrast, nephrographic, and excretory phases.

Possible Findings:
Evaluates urinary tract structures.

Differential Diagnosis:
- Stones
- Tumors
- Obstruction

Recommendation:
Follow proper contrast timing and hydration protocol.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "How to evaluate a Knee Ligament in MRI",
        "answer": """Observations:
Continuity and signal intensity of ligaments.

Possible Findings:
Indicates ligament injury or tear.

Differential Diagnosis:
- ACL tear
- PCL injury
- Sprain

Recommendation:
Orthopedic consultation recommended.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "How to identify a Spine Disc herniation on MRI",
        "answer": """Observations:
Disc protrusion compressing adjacent structures.

Possible Findings:
Indicates herniated disc.

Differential Diagnosis:
- Disc bulge
- Herniation
- Degeneration

Recommendation:
Clinical correlation and spine specialist consultation.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What is the difference between T1 and T2 in MRI",
        "answer": """Observations:
T1 shows anatomy; T2 highlights fluid and pathology.

Possible Findings:
Different tissue contrasts based on sequence.

Differential Considerations:
- T1-weighted imaging
- T2-weighted imaging

Recommendation:
Use both sequences for comprehensive evaluation.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "How to interpret MRI Diffusion ADC maps",
        "answer": """Observations:
Areas of restricted diffusion appear bright on DWI and dark on ADC.

Possible Findings:
Indicates acute ischemia or cellular injury.

Differential Diagnosis:
- Stroke
- Tumor
- Abscess

Recommendation:
Correlate with clinical findings and other sequences.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What is the significance of FLAIR in MRI",
        "answer": """Observations:
Suppresses fluid signal to highlight lesions.

Possible Findings:
Improves visibility of edema and lesions.

Differential Diagnosis:
- Multiple sclerosis
- Infarction
- Inflammation

Recommendation:
Use in brain imaging for lesion detection.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What are the common Abdominal CT signs",
        "answer": """Observations:
Abnormal organ size, density changes, or fluid collections.

Possible Findings:
May indicate infection, inflammation, or mass lesions.

Differential Diagnosis:
- Appendicitis
- Tumor
- Abscess
- Bowel obstruction

Recommendation:
Further clinical and laboratory correlation advised.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What are the CT Sinus anatomy basics",
        "answer": """Observations:
Visualization of maxillary, ethmoid, frontal, and sphenoid sinuses.

Possible Findings:
Helps identify sinus structure and abnormalities.

Differential Diagnosis:
- Sinusitis
- Polyps
- Mucosal thickening

Recommendation:
Evaluate sinus symmetry and air-fluid levels.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What are the CT Bone Scan findings",
        "answer": """Observations:
Changes in bone density and structure.

Possible Findings:
Indicates fractures, lesions, or degeneration.

Differential Diagnosis:
- Fracture
- Tumor
- Infection

Recommendation:
Correlate with clinical symptoms and history.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "How to perform a Multiphasic CT Liver scan",
        "answer": """Observations:
Imaging done in arterial, portal venous, and delayed phases.

Possible Findings:
Helps detect liver lesions and vascular patterns.

Differential Diagnosis:
- Hepatocellular carcinoma
- Hemangioma
- Metastasis

Recommendation:
Use contrast timing properly for accurate diagnosis.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What is the CT Radiation Dose (ALARA principle)",
        "answer": """Observations:
Radiation exposure minimized while maintaining image quality.

Possible Findings:
Ensures patient safety during imaging.

Differential Considerations:
- Dose optimization
- Patient safety protocols

Recommendation:
Follow ALARA principle to reduce unnecessary exposure.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What are the Prostate PI-RADS criteria in MRI",
        "answer": """Observations:
Assessment of prostate lesions using standardized scoring.

Possible Findings:
Helps identify risk of prostate cancer.

Differential Diagnosis:
- Benign lesion
- Suspicious tumor

Recommendation:
Use PI-RADS scoring for structured reporting.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "How to identify a Shoulder Labrum tear on MRI",
        "answer": """Observations:
Irregular labrum contour with signal changes.

Possible Findings:
Indicates labral tear or injury.

Differential Diagnosis:
- SLAP tear
- Degenerative changes

Recommendation:
Orthopedic evaluation recommended.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "How to evaluate Liver Hemangioma on MRI",
        "answer": """Observations:
Well-defined lesion with characteristic enhancement.

Possible Findings:
Suggests benign vascular tumor.

Differential Diagnosis:
- Hemangioma
- Metastasis

Recommendation:
Follow-up imaging may be required.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What are the Breast MRI imaging protocols",
        "answer": """Observations:
Use of contrast-enhanced dynamic sequences.

Possible Findings:
Helps detect lesions and vascular patterns.

Differential Diagnosis:
- Benign lesion
- Malignant tumor

Recommendation:
Follow standardized breast MRI protocol.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What are the basic MRI Sequence types",
        "answer": """Observations:
Different sequences provide varied tissue contrast.

Possible Findings:
Used for detailed tissue analysis.

Differential Considerations:
- T1
- T2
- FLAIR
- DWI

Recommendation:
Use multiple sequences for accurate diagnosis.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "How to identify Myelitis signs on MRI",
        "answer": """Observations:
Signal changes in spinal cord.

Possible Findings:
Indicates inflammation of spinal cord.

Differential Diagnosis:
- Myelitis
- Multiple sclerosis

Recommendation:
Neurological evaluation required.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    },
    {
        "question": "What are the basics of Pelvis MRI anatomy",
        "answer": """Observations:
Visualization of pelvic organs and structures.

Possible Findings:
Helps detect abnormalities in pelvic region.

Differential Diagnosis:
- Tumor
- Infection
- Structural abnormality

Recommendation:
Use appropriate MRI sequences for evaluation.

Disclaimer:
This analysis is AI-assisted and should be reviewed by a qualified radiologist or physician."""
    }
]
