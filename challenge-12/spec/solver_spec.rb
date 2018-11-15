require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(ternary_if) }

  describe "Test case #1" do
    let(:ternary_if) { "121" }
    let(:expected_output) { 3 } # "ABA", "AU" and "LA"

    it { is_expected.to eq(expected_output) }
  end

  describe "Test case #2" do
    let(:ternary_if) { "1234" }
    let(:expected_output) { 3 } # "ABCD", "LCD" and "AWD"

    it { is_expected.to eq(expected_output) }
  end
end
