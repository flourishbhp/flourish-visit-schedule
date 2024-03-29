from edc_visit_schedule import Schedule
from ..caregiver_visits.cohort_c_visits import visit2000

# Enrollment Schedules
c_enrollment1_schedule_1 = Schedule(
    name='c_enrol1_schedule1',
    sequence='1',
    verbose_name='Cohort C(First Child(ren)) Enrollment Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_enrollment1_schedule_1.add_visit(visit=visit2000)

c_enrollment2_schedule_1 = Schedule(
    name='c_enrol2_schedule1',
    sequence='1',
    verbose_name='Cohort C(Second Child(ren)) Enrollment Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_enrollment2_schedule_1.add_visit(visit=visit2000)

c_enrollment3_schedule_1 = Schedule(
    name='c_enrol3_schedule1',
    sequence='1',
    verbose_name='Cohort C(Third Child(ren)) Enrollment Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_enrollment3_schedule_1.add_visit(visit=visit2000)
