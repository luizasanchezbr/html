document.addEventListener('DOMContentLoaded', function() {
    // Initialize Flatpickr
    flatpickr("#flatpickr", {
        dateFormat: "d/m/Y",
        minDate: new Date().fp_incr(-360), // Allow selection up to 360 days in the past
        maxDate: new Date().fp_incr(360), // Allow selection up to 360 days in the future
        disableMobile: true,
        locale: "pt", // Set locale to Portuguese
        // Custom Portuguese translations
        localize: {
            ...flatpickr.l10ns.pt,
            firstDayOfWeek: 0, // Start week on Sunday
            rangeSeparator: " até ",
            weekAbbreviation: "Sem",
            scrollTitle: "Role para alterar",
            toggleTitle: "Clique para alternar",
        }
    });
});