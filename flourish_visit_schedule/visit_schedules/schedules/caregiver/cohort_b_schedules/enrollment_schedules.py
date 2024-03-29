from edc_visit_schedule import Schedule
from ..caregiver_visits.cohort_b_visits import visit2000

# Enrollment Schedules
b_enrollment1_schedule_1 = Schedule(
    name='b_enrol1_schedule1',
    sequence='1',
    verbose_name='Cohort B(First Child(ren)) Enrollment Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortbenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_enrollment1_schedule_1.add_visit(visit=visit2000)

b_enrollment2_schedule_1 = Schedule(
    name='b_enrol2_schedule1',
    sequence='1',
    verbose_name='Cohort B(Second Child(ren)) Enrollment Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortbenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_enrollment2_schedule_1.add_visit(visit=visit2000)

b_enrollment3_schedule_1 = Schedule(
    name='b_enrol3_schedule1',
    sequence='1',
    verbose_name='Cohort B(Third Child(ren)) Enrollment Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortbenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_enrollment3_schedule_1.add_visit(visit=visit2000)
