import React from 'react';
import './Report.css'; // Import the CSS file

function Report({ report }) {
  return (
    <div className="report-container">
      {Object.entries(report).filter(([key]) => key !== 'WARNINGS').map(([org, projects], index) => (
        <div key={`org-${index}`} className="report-organization">
          <h2 className="report-organization-title">{org}</h2>
          {report.WARNINGS && report.WARNINGS.length > 0 ? (
            <div className="report-warnings">
              <h3 className="report-warnings-title">Warnings</h3>
              <table className="report-table">
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Category</th>
                    <th>Severity</th>
                    <th>Recommendation</th>
                  </tr>
                </thead>
                <tbody>
                  {report.WARNINGS.map((warning, warningIndex) => (
                    <tr key={`warning-${warningIndex}`}>
                      <td>{warning.name}</td>
                      <td>{warning.category}</td>
                      <td>{warning.severity}</td>
                      <td>{warning.recommendation}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="report-no-warnings">
              <p>No warnings found for this organization.</p>
            </div>
          )}
          <table className="report-table">
            <thead>
              <tr>
                <th>Project</th>
                <th>Details</th>
              </tr>
            </thead>
            <tbody>
              {projects.map((project, projectIndex) => (
                <tr key={`project-${projectIndex}`}>
                  <td>{Object.keys(project)[0]}</td>
                  <td>
                    <table>
                      <tbody>
                        {Object.entries(Object.values(project)[0]).map(([key, value]) => (
                          <tr key={key}>
                            <td>{key}</td>
                            <td>
                              {key === 'AdminNumber' ? (
                                <span>{value}</span>
                              ) : key === 'Admins' ? (
                                <ul>
                                  {value.map((admin, index) => (
                                    <li key={index}>{admin}</li>
                                  ))}
                                </ul>
                              ) : (
                                Array.isArray(value) ? value.join(', ') : value
                              )}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ))}
    </div>
  );
}

export default Report;
