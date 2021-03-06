from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.cliniciannotes',
        required=False, additional=False),
    name='caregiver_crf_prn')

crf_pre_consent = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.sociodemographicdata'),
    name='pre_flourish')

a_crf_2000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=2, model='flourish_caregiver.medicalhistory'),
    Crf(show_order=3, model='flourish_caregiver.maternalhivinterimhx',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.hivviralloadandcd4',
        required=False),
    Crf(show_order=5, model='flourish_caregiver.arvsprepregnancy',
        required=False),
    Crf(show_order=6, model='flourish_caregiver.maternalarvduringpreg',
        required=False),
    Crf(show_order=7, model='flourish_caregiver.substanceusepriorpregnancy',),
    Crf(show_order=8, model='flourish_caregiver.caregiverclinicalmeasurements'),
    Crf(show_order=9, model='flourish_caregiver.caregiverphqdeprscreening',
        required=False),
    Crf(show_order=10, model='flourish_caregiver.caregiverphqreferral',
        required=False),
    Crf(show_order=11, model='flourish_caregiver.caregiveredinburghdeprscreening',
        required=False),
    Crf(show_order=12, model='flourish_caregiver.caregiveredinburghreferral',
        required=False),
    Crf(show_order=13, model='flourish_caregiver.caregivergadanxietyscreening'),
    Crf(show_order=14, model='flourish_caregiver.caregivergadreferral',
        required=False),
    Crf(show_order=15, model='flourish_caregiver.tbhistorypreg',
        required=False),
    Crf(show_order=16, model='flourish_caregiver.tbscreenpreg',
        required=False),
    Crf(show_order=17, model='flourish_caregiver.tbpresencehouseholdmembers',
        required=False),
    Crf(show_order=18, model='flourish_caregiver.ultrasound',
        required=False),
    Crf(show_order=19, model='flourish_caregiver.cliniciannotes'),
    name='cohort_a_enrollment')

bc_crf_2000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=2, model='flourish_caregiver.medicalhistory'),
    Crf(show_order=3, model='flourish_caregiver.hivviralloadandcd4',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.caregiverclinicalmeasurements'),
    Crf(show_order=5, model='flourish_caregiver.obstericalhistory',
        required=False),
    Crf(show_order=6, model='flourish_caregiver.caregiverphqdeprscreening'),
    Crf(show_order=7, model='flourish_caregiver.caregiverphqreferral',
        required=False),
    Crf(show_order=8, model='flourish_caregiver.caregivergadanxietyscreening'),
    Crf(show_order=9, model='flourish_caregiver.caregivergadreferral',
        required=False),
    Crf(show_order=10, model='flourish_caregiver.hivdisclosurestatusa',
        required=False),
    Crf(show_order=11, model='flourish_caregiver.hivdisclosurestatusb',
        required=False),
    Crf(show_order=12, model='flourish_caregiver.hivdisclosurestatusc',
        required=False),
    Crf(show_order=13, model='flourish_caregiver.hivdisclosurestatusd',
        required=False),
    Crf(show_order=14, model='flourish_caregiver.cliniciannotes'),
    name='cohort_bc_enrollment')

crf_2000d = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.maternalarvduringpreg',
        required=False),
    Crf(show_order=2, model='flourish_caregiver.caregiverclinicalmeasurements'),
    Crf(show_order=3, model='flourish_caregiver.substanceuseduringpregnancy'),
    Crf(show_order=4, model='flourish_caregiver.maternaldiagnoses'),
    Crf(show_order=5, model='flourish_caregiver.cliniciannotes'),
#     Crf(show_order=6, model='flourish_caregiver.maternalinterimidccdata'),
    name='birth')

crf_2001 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=2, model='flourish_caregiver.medicalhistory'),
    Crf(show_order=3, model='flourish_caregiver.hivdisclosurestatusa',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.hivdisclosurestatusb',
        required=False),
    Crf(show_order=5, model='flourish_caregiver.hivdisclosurestatusc',
        required=False),
    Crf(show_order=6, model='flourish_caregiver.hivdisclosurestatusd',
        required=False),
    name='quarterly_calls')

crf_3000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=2, model='flourish_caregiver.medicalhistory'),
    Crf(show_order=3, model='flourish_caregiver.hivviralloadandcd4',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.caregiverclinicalmeasurements'),
    Crf(show_order=5, model='flourish_caregiver.caregiveredinburghdeprscreening',
        required=False),
    Crf(show_order=6, model='flourish_caregiver.hivdisclosurestatusa',
        required=False),
    Crf(show_order=7, model='flourish_caregiver.hivdisclosurestatusb',
        required=False),
    Crf(show_order=8, model='flourish_caregiver.hivdisclosurestatusc',
        required=False),
    Crf(show_order=9, model='flourish_caregiver.hivdisclosurestatusd',
        required=False),
    Crf(show_order=10, model='flourish_caregiver.cliniciannotes'),
    name='follow_up')
