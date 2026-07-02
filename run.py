import time

from boatos.core.config import load_config
from boatos.core.databus import DataBus
from boatos.core.logger import log
from boatos.services.navigation import NavigationService
from boatos.services.engine import EngineService
from boatos.services.electrical import ElectricalService
from boatos.services.system_status import SystemStatusService
from boatos.ui.terminal_dashboard import TerminalDashboard


def main():
    config = load_config()
    bus = DataBus()

    services = [
        NavigationService(bus),
        EngineService(bus),
        ElectricalService(bus),
        SystemStatusService(bus),
    ]

    ui = TerminalDashboard(bus, config)
    refresh_rate = float(config.get("refresh_rate", 1.0))

    log("BoatOS v0.3 startar")

    try:
        while True:
            for service in services:
                service.update()
            ui.render()
            time.sleep(refresh_rate)
    except KeyboardInterrupt:
        log("BoatOS avslutas")


if __name__ == "__main__":
    main()
