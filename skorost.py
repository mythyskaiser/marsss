import time
import krpc

conn = krpc.connect(name='Vessel speed')
vessel = conn.space_center.active_vessel
srf_frame = vessel.orbit.body.reference_frame
thrust = conn.space_center.active_vessel

while True:
    srf_speed = vessel.flight(srf_frame).speed
    altitude = vessel.flight(srf_frame).mean_altitude
    print('Thrust: %d kN ,Surface speed = %.1f m/s, Altitude = %.1f m' %
          (thrust.thrust/1000, srf_speed, altitude))
    time.sleep(1)

