import React from "react";
import {
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogContentText,
  TextField,
  DialogActions,
} from "@mui/material";

export default function ShareDialog() {
  const [open, setOpen] = React.useState(false);
  const [loading, setLoading] = React.useState(false); // Track loading state
  const [sent, setSent] = React.useState(false); // Track if the report was sent
  const [error, setError] = React.useState(null); // Track errors (optional)

  const handleClickOpen = () => {
    setOpen(true);
    setSent(false); // Reset the "sent" state when the dialog opens
  };

  const handleClose = () => {
    setOpen(false);
    setError(null); // Clear error message when closing the dialog
    setLoading(false); // Reset loading state when closing
    setSent(false); // Reset sent state when closing
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData(event.currentTarget);
    const formJson = Object.fromEntries(formData.entries());
    const email = formJson.email;

    setLoading(true);

    try {
      const response = await fetch(
        `http://localhost:5000/report/share?recipient=${encodeURIComponent(
          email
        )}`,
        {
          method: "GET",
          credentials: "include", // Include session cookies
        }
      );

      if (!response.ok) {
        throw new Error("Failed to share the report. Please try again.");
      }

      const data = await response.json();
      console.log("Success:", data);

      // Indicate success
      setSent(true);

      // Close the dialog after a short delay
      setTimeout(() => {
        handleClose();
      }, 1500); // Adjust delay time as needed
    } catch (error) {
      console.error("Error:", error);
      setError("Failed to share the report. Please try again."); // Set error message
    } finally {
      setLoading(false); // Reset loading state
    }
  };

  return (
    <React.Fragment>
      <Button variant="outlined" onClick={handleClickOpen}>
        Share Report
      </Button>
      <Dialog
        open={open}
        onClose={handleClose}
        PaperProps={{
          component: "form",
          onSubmit: handleSubmit,
        }}
      >
        <DialogTitle>Send to a Friend</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Let someone know what you're up to. Enter their email address to
            send them your roll call.
          </DialogContentText>
          <TextField
            autoFocus
            required
            margin="dense"
            id="email"
            name="email"
            label="Email Address"
            type="email"
            fullWidth
            variant="standard"
            disabled={loading || sent} // Disable input when loading or sent
          />
          {error && (
            <p style={{ color: "red", marginTop: "10px" }}>
              {error}
            </p>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} disabled={loading}>
            Nevermind
          </Button>
          <Button type="submit" disabled={loading || sent}>
            {loading ? "Sending..." : sent ? "Sent!" : "Send"}
          </Button>
        </DialogActions>
      </Dialog>
    </React.Fragment>
  );
}



